"""
Condensing turbine operating at full load.

Tests used to verify the three turbine models: simple, heatspec, workspec

For a turbine operating at full capacity (Case 1)
    Mechanical Effieciency = 0.97 [default]
    Input Inlet PRESSURE (bara) =  10
    Input Inlet TEMPERATURE (degC) =  300
    Input Outlet PRESSURE (bara) =  0.1
    Input Actual Mass Flow (kg/s) =  12
    Input Max Mass Flow (kg/s) =  12
    Shaft Work (Willans) 7671.6389 kW
    Shaft Work (Entropy) 7671.6389 kW
    Isentropic Efficiency 0.829562
    Heat Content 26409.7846 kW
    Isentropic Efficiency 0.829562
    Outlet: T=45.81, x=0.9200

Tests should be accurate within a relative tolerance of 1% for variables:
 - Q
 - W
 - Isentropic Efficiency
"""

from pytest import approx

from steamy import Turbine


# Case 1 - Test Full Load (tf):
tf_P_1 = 10
tf_T_1 = 300
tf_P_2 = 0.1
tf_m_act = 12
tf_Q = 26409.7846
tf_W = 7671.6389
tf_eff_IS = 0.829562

def test_simple_full():
    test_turbine = Turbine(P_1=tf_P_1, T_1=tf_T_1, P_2=tf_P_2, m_act=tf_m_act)

    assert test_turbine.work() == approx(tf_W, rel=1e-2)
    assert test_turbine.heat() == approx(tf_Q, rel=1e-2)
    assert test_turbine.efficiency_IS() == approx(tf_eff_IS, rel=1e-2)

def test_heat_full():
    test_turbine = Turbine(P_1=tf_P_1, T_1=tf_T_1, P_2=tf_P_2, Q=tf_Q)

    assert test_turbine.work() == approx(tf_W, rel=1e-2)
    assert test_turbine.m_act == approx(tf_m_act, rel=1e-2)
    assert test_turbine.efficiency_IS() == approx(tf_eff_IS, rel=1e-2)

def test_work_full():
    test_turbine = Turbine(P_1=tf_P_1, T_1=tf_T_1, P_2=tf_P_2, W=tf_W)

    assert test_turbine.heat() == approx(tf_Q, rel=1e-2)
    assert test_turbine.m_act == approx(tf_m_act, rel=1e-2)
    assert test_turbine.efficiency_IS() == approx(tf_eff_IS, rel=1e-2)
