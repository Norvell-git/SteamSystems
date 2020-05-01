"""
Simple function to find outlet conditions of a steam turbine
	for a fully spec'd turbine

Input: m_act, m_max

Return: outlet(IAPWS97)

Assuming: inlet(IAPWS97) and outlet_IS(IAPWS97) are defined
"""

from iapws import IAPWS97
from MainFunctions.MoreFunctions import base

def simple(inlet, outlet_IS, m_act, m_max, eff_mech):

	a = base.abc(inlet.P, outlet_IS.P)[0]
	b = base.abc(inlet.P, outlet_IS.P)[1]
	c = base.abc(inlet.P, outlet_IS.P)[2]

	dh_IS = base.dh_IS(inlet, outlet_IS)

	n = base.n(a, b, c, dh_IS, m_max)
	Wint = base.Wint(a, b, c, dh_IS, m_max)

	W = base.W(m_act, n, Wint)

	h_2 = base.h_2(inlet, W, eff_mech, m_act)

	return IAPWS97(P = (outlet_IS.P/10), h = h_2)
