"""
Basic functions required for turbine models
"""

def abc(P_1, P_2):
    """
    Modelling parameters from Sun and Smith 2015
    """
    if P_2 < 1.013:
        a = 1.3150    - 1.6347e-3 * P_1 - 0.36798   * P_2
        b = - 437.77  + 29.007    * P_1 + 10.359    * P_2
        c = 7.8863e-2 + 5.2833e-4 * P_1 - 0.70315   * P_2
    else:
        a = 1.1880    - 2.9564e-4 * P_1 + 4.6473e-3 * P_2
        b = 449.98    + 5.6702    * P_1 - 11.505    * P_2
        c = 0.20515   - 6.9517e-4 * P_1 + 2.8446e-3 * P_2
    return [a, b, c]

def dh_IS(inlet, outlet_IS):
    """
    Calculate isentropice entropy change
    """
    return inlet.h - outlet_IS.h

def n(a, b, c, dh_IS, m_max):
    """
    gradient of Willans Line
    """
    return (1+c)/a * (dh_IS - b/m_max)

def Wint(a, b, c, dh_IS, m_max):
    """
    y-intercept of Willans Line
    """
    return (c/a)*(m_max*dh_IS - b)

def W(m_act, n, Wint):
    """
    Calculate shaft power
    """
    return m_act * n - Wint

def h_2(inlet, W, eff_mech, m_act):
    """
    Outlet entropy from shaft power
    """
    return inlet.h - W / (eff_mech * m_act)
