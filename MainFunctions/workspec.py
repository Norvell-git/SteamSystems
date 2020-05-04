"""
Function to find outlet conditions of a steam turbine where the
    required shaft work is given

Input: Q, (m_max or m_rat)

Return: outlet(IAPWS97)

Assuming: inlet(IAPWS97) and outlet_IS(IAPWS97) are defined

"""
from iapws import IAPWS97
from MainFunctions.MoreFunctions import base

def heatspec(inlet, outlet_IS, W, eff_mech, **max):
    print("no finished yet!")
