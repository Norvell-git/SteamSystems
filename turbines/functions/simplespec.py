"""
Simple function to find outlet conditions of a steam turbine
    for a fully spec'd turbine

Input: m_act, m_max

Return: outlet(IAPWS97)

Assuming: inlet(IAPWS97) and outlet_IS(IAPWS97) are defined
"""

from iapws import IAPWS97

from .base import (f_abc, f_dh_IS, f_n, f_Wint, f_W, f_h_2)

def simple(inlet, outlet_IS, m_act, m_max, eff_mech):

    abc = f_abc(inlet.P*10, outlet_IS.P*10)  # Output in bara
    a = abc[0]
    b = abc[1]
    c = abc[2]

    dh_IS = f_dh_IS(inlet, outlet_IS)

    n = f_n(a, b, c, dh_IS, m_max)
    Wint = f_Wint(a, b, c, dh_IS, m_max)

    W = f_W(m_act, n, Wint)

    h_2 = f_h_2(inlet, W, eff_mech, m_act)

    return IAPWS97(P=(outlet_IS.P), h=h_2)
