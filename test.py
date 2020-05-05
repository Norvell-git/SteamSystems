"""
test1 for turbine model
for a fully sppec'd turbine
"""
from turbine import Turbine

pres=20

testturbine = Turbine(P_1=80, T_1=500, P_2=pres, W=3004.63, m_rat=1.2)

#print(f"Work = {testturbine.W:.2f} kW")
#print(f"Outlet Temp = {testturbine.outlet.T:.2f} degC")

eff_IS = (testturbine.inlet.h - testturbine.outlet.h)/(testturbine.inlet.h - testturbine.outlet_IS.h)

Q = testturbine.m_act * (testturbine.outlet.h - testturbine.cond.h)

print(f"P_2 = {pres:.2f} bara,    Eff = {eff_IS:.2f},    T_2 = {testturbine.outlet.T:.2f},    h_2 = {testturbine.outlet.h:.2f},    Q = {Q:.2f}")  

# ,    W = {testturbine.W:.2f} kW

#print(f"Work = {testturbine:.2f} kW")
