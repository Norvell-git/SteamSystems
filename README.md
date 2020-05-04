# SteamTurbine
**WIP** Model a simple steam turbine using Willans Line model and IAPWS-IF97 steam tables.

Modelling parameters taken from Sun and Smith 2015 (Performance Modeling of New and Existing Steam Turbines).

## *Class* turbine.Turbine(\*\*kwargs)
### Essential Parameters:
P_1, P_2  - Pressurse (inlet, outlet) bara

T_1       - Temperature (inlet) degC

### Optional Parameters:
m_act     - Actual mass flowrate of steam (kg/s)

m_rat     - Ratio of actual to maximum flowrate

m_max     - Maximum flowrate of steam through the turbine (kg/s)

Q         - Heat content of the outlet stream (kW)

## Dependencies:
* iapws (built using v1.4.1)
* numpi-scipy

## To do

* Implement work spec model

