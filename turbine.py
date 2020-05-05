"""
Turbine Package

"""
from iapws import IAPWS97
from MainFunctions import (simple, workspec, heatspec, non_specd)
from MainFunctions.errors import InputError


class Turbine():
    """
    Model a steam turbine based upon a number of specified operating conditions
    """
    def __init__(self, **kwargs):
        """
        Essential Arguments: P_1, T_1, P_2
        Optional Arguments: m_act, m_max, m_rat, Q, W, eff_mech

        Possible Combinations:
            m_act, m_max
            m_act, m_rat
            m_max, Q
            m_rat, Q
            Q
            m_max, W
            m_rat, W
            W
        """

        # Input Verification
        for arg in kwargs:
            try:
                float(kwargs[arg])
            except ValueError:
                raise InputError(f"Invalid Input: {arg} = {kwargs[arg]}"
                                 " must be a number")

        # Define essential arguments
        if 'P_1' in kwargs:
            P_1 = kwargs['P_1']
        else:
            raise InputError("Essential argument not defined (P_1).")

        if 'T_1' in kwargs:
            T_1 = kwargs['T_1']
        else:
            raise InputError("Essential argument not defined (T_1).")

        if 'P_2' in kwargs:
            P_2 = kwargs['P_2']
        else:
            raise InputError("Essential argument not defined (P_2).")

        # Define optional arguments
        eff_mech = kwargs.get('eff_mech', 0.97)
        m_act = kwargs.get('m_act', None)
        m_max = kwargs.get('m_max', None)
        m_rat = kwargs.get('m_rat', None)
        Q = kwargs.get('Q', None)
        W = kwargs.get('W', None)

        # Define IAPWS97 class items
        inlet = IAPWS97(P=(P_1/10), T=(T_1+273.15))  # Inlet conditions
        outlet_IS = IAPWS97(P=(P_2/10), s=inlet.s)  # Isentropic expansion
        cond = IAPWS97(P=(P_2/10), x=0)  # Condensate

        # Variable list
        variables = [m_act, Q, W, m_max, m_rat]
        # print(variables)
        var_bool = [x is not None for x in variables]

        # Check that a problem has been specififed
        non_specd(var_bool)

        # Simple Spec'd Turbine
        if var_bool[0]:
            #with m_max
            if var_bool[3]:
                outlet = simple(inlet, outlet_IS, m_act, m_max, eff_mech)

            # with m_rat
            elif var_bool[4]:
                m_max = m_act * m_rat
                outlet = simple(inlet, outlet_IS, m_act, m_max, eff_mech)

            # full capacity
            else:
                m_max = m_act
                outlet = simple(inlet, outlet_IS, m_act, m_max, eff_mech)

        # Target Heat at Outlet, assuming full condensation
        # Find outlet then define m_act and m_max
        if var_bool[1]:
            # with m_max
            if var_bool[3]:
                outlet = heatspec(inlet, cond, Q, eff_mech, m_max=m_max)
                m_act = Q / (outlet.h - cond.h)

            # with m_rat
            elif var_bool[4]:
                outlet = heatspec(inlet, cond, Q, eff_mech, m_rat=m_rat)
                m_act = Q / (outlet.h - cond.h)
                m_max = m_act * m_rat

            # full capacity
            else:
                outlet = heatspec(inlet, cond, Q, eff_mech, m_rat=1)
                m_act = Q / (outlet.h - cond.h)
                m_max = m_act

        # Target Work from Turbine
        # Find outlet then define m_act and m_max
        if var_bool[2]:
            # with m_max
            if var_bool[3]:
                outlet = workspec(inlet, outlet_IS, W, eff_mech, m_max=m_max)
                m_act = W / (eff_mech * (inlet.h - outlet.h))

            # with m_rat
            elif var_bool[4]:
                outlet = workspec(inlet, outlet_IS, W, eff_mech, m_rat=m_rat)
                m_act = W / (eff_mech * (inlet.h - outlet.h))
                m_max = m_act * m_rat

            # full capacity
            else:
                outlet = workspec(inlet, outlet_IS, W, eff_mech, m_rat=1)
                m_act = W / (eff_mech * (inlet.h - outlet.h))
                m_max = m_act

        # Define the parameters
        self.m_act = m_act
        self.m_max = m_max
        self.eff_mech = eff_mech
        self.inlet = inlet
        self.outlet = outlet
        self.outlet_IS = outlet_IS
        self.cond = cond

    # def __str__(self):
        # Print a little diagramm showing the turbine and main conditions

    def work(self):
        """
        Calculate the shaft power produced by the Turbine
        """
        return self.m_act * self.eff_mech * (self.inlet.h - self.outlet.h)

    def heat(self):
        """
        Calculate the heat content of the outlet stream, assuming full
        condensation.
        """
        return self.m_act * (self.outlet.h - self.cond.h)

    def efficiency_IS(self):
        """
        Calculate the isentropic efficiency of a given Turbine.
        """
        return ((self.inlet.h - self.outlet.h) /
                (self.inlet.h - self.outlet_IS.h))

    # def part_load(self, capacity):
        """
        Return a new Turbine class object based upon the part load perfomance
        of an existing turbine (self), operating at part load capacity.

        Parameters
        ----------
        self : Turbine
            Predetermined Turbine class object.
        capacity : float
            The ratio betweent the operating mass flowrate and maximum design
            flowrate. e.g. a turbine operating at half load would be at 0.5
            capacity.

        Returns
        -------
        plt : Turbine
            Returns part-load turbine (plt) as a new Turbine class object.
        """
        # m_act = self.m_max * capacity

        # Part load turbine may have to be new, sepperate module function
        # plt = __init__(P_1=self.inlet.P, T_1=self.inlet.T, P_2=self.outlet.P,
        # m_act=m_act, m_max=self.m_max)
        # return plt
