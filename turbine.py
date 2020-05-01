"""
Turbine Package

"""
from iapws import IAPWS97
from MainFunctions.simplespec import simple

class Turbine():
	"""
	Model a steam turbine based upon a number of specified operating conditions
	"""

	#from MainFunctions.heatspec import heatspec
	#from MainFunctions.workspec import workspec


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
			except: 
				return print(f"Invalid Input... {kwargs[arg]}")


		# Define essential arguments
		if 'P_1' in kwargs:
			P_1 = kwargs['P_1']
		else:
			return print("Essential Argument not Specified (P_1).")

		if 'T_1' in kwargs:
			T_1 = kwargs['T_1']
		else:
			return print("Essential Argument not Specified (T_1).")

		if 'P_2' in kwargs:
			P_2 = kwargs['P_2']
		else:
			return print("Essential Argument not Specified (P_2).")


		# Define optional arguments
		if 'eff_mech' in kwargs:
			eff_mech = kwargs['eff_mech']
		else:
			eff_mech = 0.97

		if 'm_act' in kwargs:
			m_act = kwargs['m_act']
		else:
			m_act = None

		if 'm_max' in kwargs:
			m_max = kwargs['m_max']
		else:
			m_max = None

		if 'm_rat' in kwargs:
			m_rat = kwargs['m_rat']
		else:
			m_rat = None

		if 'Q' in kwargs:
			Q = kwargs['Q']
		else: Q = None

		if 'W' in kwargs:
			W = kwargs['W']
		else:
			W = None


		# Define known parameters
		inlet = IAPWS97(P = (P_1/10), T = (T_1+273.15))
		outlet_IS = IAPWS97(P = (P_2/10), s = inlet.s)
		cond = IAPWS97(P = (P_2/10), x = 0)

		

		# Identify and solve problem
		if m_act == m_max == m_rat == Q == W == None:
			return print("No problem has been specified.")

			
		## Simple Spec'd Turbine
		elif m_act != None:
			if m_max != None:
				if m_rat != None or Q != None or W != None: #Try better
					return print("Problem is overspecified.")

				outlet = simple(inlet, outlet_IS, m_act, m_max, eff_mech)

			elif m_rat != None:
				if Q != None or W != None: #Try better
					return print("Problem is overspecified.")

				m_max = m_act * m_rat
				outlet = simple(inlet, outlet_IS, m_act, m_max, eff_mech)

			else:

				m_max = m_act
				outlet = simple(inlet, outlet_IS, m_act, m_max, eff_mech)
				

		## Target Heat at Outlet, assuming full condensation
		elif Q != None:
			if m_max != None:
				if m_rat != None or W != None: #Try better
					return print("Problem is overspecified.")

				outlet = heatspec(m_max = m_max)

			elif m_rat != None:
				if W != None:
					return print("Problem is overspecified.")

				outlet = heatspec(m_rat = m_rat)

			else:
				
				outlet = heatspec(m_rat = 1)


		## Target Work from Turbine
		elif W != None:
			if m_max != None:
				if m_rat != None:
					return print("Problem is overspecified.")
				outlet = workspec(m_max = m_max)

			elif m_rat != None:
				outlet = workspec(m_rat = m_rat)

			else:
				outlet = workspec(m_rat = 1)

		# No problem found
		else:
			return print("No problem identified.")

		# Define the parameters

		self.P_1 = P_1
		self.T_1 = T_1
		self.h_1 = inlet.h
		self.s_1 = inlet.s

		self.P_2 = P_2
		self.T_2 = outlet.T
		self.h_2 = outlet.h
		self.s_2 = outlet.s

		self.Q = m_act * (outlet.h - cond.h)
		self.W = (inlet.h - outlet.h) * (eff_mech * m_act)
		# 	e.g et and outlet conditions, work, heat available, 


		# Define turbine str for print (nice little diagram)

