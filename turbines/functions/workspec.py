"""
Function to find outlet conditions of a steam turbine where the
    required shaft work is given

Input: Q, (m_max or m_rat)

Return: outlet(IAPWS97)

Assuming: inlet(IAPWS97) and outlet_IS(IAPWS97) are defined

"""
from iapws import IAPWS97
from .functions import (f_abc, f_dh_IS, f_n, f_Wint, f_W, f_h_2)

def workspec(inlet, outlet_IS, W_tar, eff_mech, **max):
    
    m_rat = max.get('m_rat', None)
    m_max = max.get('m_max', None)

    # Constants
    abc = f_abc(inlet.P*10, outlet_IS.P*10)  # abc is calculated in bara
    a = abc[0]
    b = abc[1]
    c = abc[2]
    dh_IS = f_dh_IS(inlet, IAPWS97(P=outlet_IS.P, s=inlet.s))

    # Initial guess for mass flowrate
    m_act = W_tar / (eff_mech * (inlet.h - outlet_IS.h))

    h_out_i1 = f_h_2(inlet, W_tar, eff_mech, m_act)

    # initialise convergence parameters
    i = 0
    tol = 1e-5  # Absolute tolerance
    h_err = tol + 10  # Make sure initial error > tol

    while h_err > tol:

        # Check loop number, not sure if this is the right exception
        i += 1
        if i > 100:
            raise StopIteration("After 100 iteration turbine not converged.")

        # Set max flowrate
        if not m_rat == None:
            m_max = m_act * m_rat

        # Model turbine
        n = f_n(a, b, c, dh_IS, m_max)
        W_int = f_Wint(a, b, c, dh_IS, m_max)
        W_calc = f_W(m_act, n, W_int)

        # Comment in/out to track iteration
        # print(f"i={i}, W={W_calc:.2f}, h_2={h_out_i1:.2f}, m={m_act:.2f}")
        
        # Update convergence criteria
        h_out_i2 = f_h_2(inlet, W_calc, eff_mech, m_act)
        h_err = abs(h_out_i2 - h_out_i1)
        h_out_i1 = h_out_i2

        # Set new flowrate
        m_act = W_tar / (eff_mech * (inlet.h - h_out_i2))

    # comment in/out to show final figures
    # print(f"\nFinal Iteration\ni={i}, W={W_calc:.2f}, h_2={h_out_i1:.2f}, m={m_act:.2f}")

    return IAPWS97(P=outlet_IS.P, h=h_out_i2)
