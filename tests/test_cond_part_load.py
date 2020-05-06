"""
Part load condensing turbine tests.

Tests used to verify the three turbine models: simple, heatspec, workspec

Based upon a simple turbine model sized with 20% extra capacity (Case 2)
    Mechanical Effieciency = 0.97 [default]
    Input Inlet PRESSURE (bara) =  10
    Input Inlet TEMPERATURE (degC) =  300
    Input Outlet PRESSURE (bara) =  0.1
    Input Actual Mass Flow (kg/s) =  10
    Input Max Mass Flow (kg/s) =  12
    Shaft Work (Willans) 6375.3476 kW
    Shaft Work (Entropy) 6375.3476 kW
    Isentropic Efficiency 0.827267
    Heat Content 22026.3856 kW
    Isentropic Efficiency 0.827267
    Outlet: T=45.81, x=0.9208

Tests should be accurate within a relative tolerance of 1% for variables:
 - Q
 - W
 - Isentropic Efficiency
"""

from pytest import approx

from steamy import Turbine


# Case 2 - Part Load (t):
t_P_1 = 10
t_T_1 = 300
t_P_2 = 0.1
t_m_act = 10
t_m_rat = 1.2
t_m_max = 12
t_Q = 22026.3856
t_W = 6375.3476
t_eff_IS = 0.827267

def test_simple_max():
    test_turbine = Turbine(P_1=t_P_1, T_1=t_T_1, P_2=t_P_2,
                           m_act=t_m_act, m_max=t_m_max)

    assert test_turbine.work() == approx(t_W, rel=1e-2)
    assert test_turbine.heat() == approx(t_Q, rel=1e-2)
    assert test_turbine.efficiency_IS() == approx(t_eff_IS, rel=1e-2)

def test_simple_rat():
    test_turbine = Turbine(P_1=t_P_1, T_1=t_T_1, P_2=t_P_2,
                           m_act=t_m_act, m_rat=t_m_rat)

    assert test_turbine.work() == approx(t_W, rel=1e-2)
    assert test_turbine.heat() == approx(t_Q, rel=1e-2)
    assert test_turbine.efficiency_IS() == approx(t_eff_IS, rel=1e-2)

def test_heat_max():
    test_turbine = Turbine(P_1=t_P_1, T_1=t_T_1, P_2=t_P_2,
                           Q=t_Q, m_max=t_m_max)

    assert test_turbine.work() == approx(t_W, rel=1e-2)
    assert test_turbine.m_act == approx(t_m_act, rel=1e-2)
    assert test_turbine.efficiency_IS() == approx(t_eff_IS, rel=1e-2)

def test_heat_rat():
    test_turbine = Turbine(P_1=t_P_1, T_1=t_T_1, P_2=t_P_2,
                           Q=t_Q, m_rat=t_m_rat)

    assert test_turbine.work() == approx(t_W, rel=1e-2)
    assert test_turbine.m_act == approx(t_m_act, rel=1e-2)
    assert test_turbine.efficiency_IS() == approx(t_eff_IS, rel=1e-2)

def test_work_max():
    test_turbine = Turbine(P_1=t_P_1, T_1=t_T_1, P_2=t_P_2,
                           W=t_W, m_max=t_m_max)

    assert test_turbine.heat() == approx(t_Q, rel=1e-2)
    assert test_turbine.m_act == approx(t_m_act, rel=1e-2)
    assert test_turbine.efficiency_IS() == approx(t_eff_IS, rel=1e-2)

def test_work_rat():
    test_turbine = Turbine(P_1=t_P_1, T_1=t_T_1, P_2=t_P_2,
                           W=t_W, m_rat=t_m_rat)

    assert test_turbine.heat() == approx(t_Q, rel=1e-2)
    assert test_turbine.m_act == approx(t_m_act, rel=1e-2)
    assert test_turbine.efficiency_IS() == approx(t_eff_IS, rel=1e-2)
