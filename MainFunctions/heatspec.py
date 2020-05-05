"""
Function to find outlet conditions of a steam turbine where the
    required heat content of the outlet is given

Input: Q, (m_max or m_rat)

Return: outlet(IAPWS97)

Assuming: inlet(IAPWS97) and outlet_IS(IAPWS97) are defined

"""
from iapws import IAPWS97
from .MoreFunctions import (f_abc, f_dh_IS, f_n, f_Wint, f_W, f_h_2)

def heatspec(inlet, cond, Q, eff_mech, **max):

    m_rat = max.get('m_rat', None)
    m_max = max.get('m_max', None)

    # Constants
    abc = f_abc(inlet.P*10, cond.P*10)  # abc is calculated in bara
    a = abc[0]
    b = abc[1]
    c = abc[2]
    dh_IS = f_dh_IS(inlet, IAPWS97(P=cond.P, s=inlet.s))

    # Initial guess for mass flowrate
    m_act = Q / (inlet.h - cond.h)

    # initialise convergence parameters
    i = 0
    tol = 1e-5  # Absolute tolerance
    h_out_i1 = 0
    h_err = tol + 10  # Make sure initial error > tol

    while h_err > tol:

        # Check loop number, not sure if this is the right exception
        i += 1
        if i > 100:
            raise StopIteration("After 100 iteration turbine not converged.")

        # Set max flowrate
        if not m_rat == None:
            m_max = m_act * m_rat

        # comment in/out to track iterator
        # print(f"i={i}, hi={h_out_i1:.2f}, m={m_act:.2f}")

        # Model turbine
        n = f_n(a, b, c, dh_IS, m_max)
        W_int = f_Wint(a, b, c, dh_IS, m_max)
        W = f_W(m_act, n, W_int)

        # Update loop criteria
        h_out_i2 = inlet.h - W / (m_act * eff_mech)
        h_err = abs(h_out_i2 - h_out_i1)
        h_out_i1 = h_out_i2

        # Set new flowrate
        m_act = Q / (h_out_i2 - cond.h)

        print(f"{m_act:.3f}   {W:.2f}")
    # comment in/out to show final figures
    # print(f"\nFinal Iteration\ni={i}, hi={h_out_i1:.2f}, m={m_act:.2f}")

    return IAPWS97(P=cond.P, h=h_out_i2)