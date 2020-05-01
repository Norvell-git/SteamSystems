"""
Function to find outlet conditions of a steam turbine where the
	required heat content of the outlet is given

Input: Q, (m_max or m_rat)

Return: outlet(IAPWS97)

Assuming: inlet(IAPWS97), outlet_IS(IAPWS97), and cond(IAPWS97) are defined

"""

import MoreFunctions.base

def heatspec(**max):
	
