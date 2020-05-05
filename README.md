# SteamTurbine
**WIP** Model a simple steam turbine using Willans Line model and IAPWS-IF97 steam tables.

Modelling parameters taken from Sun and Smith 2015 (Performance Modeling of New and Existing Steam Turbines).

## *Class* turbine.Turbine(\*\*kwargs)
#### Essential Parameters:
`P_1`   - Turbine Inlet Pressure (bara)

`P_2`   - Turbine Outlet Pressure (bara)

`T_1`   - Turbine Inlet Temperature (degC)

#### Optional Parameters:
`m_act` - Actual mass flowrate of steam (kg/s)

`m_rat` - Ratio of actual to maximum flowrate (kg/kg)

`m_max` - Maximum flowrate of steam through the turbine (kg/s)

`Q`     - Useful heat content of the outlet stream (kW)

`W`     - Shaft work produced by the turbine (kW)

## Dependencies:
* iapws (built using v1.4.1)
* numpi-scipy

## To do

* Include more methods
* Create tests for condensing turbine
* Documentation
