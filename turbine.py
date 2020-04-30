"""
Turbine Package

"""


class Turbine():
	"""
	Model a steam turbine based upon a number of specified operating conditions
	"""

	from iapws import IAPWS97

	def __init__(self, **kwargs):
		"""
		Essential Arguments: P_1, T_1, P_2
		Optional Arguments: m_act, m_max, m_rat, Q, W, eff_mech

		Possible Combinations:
			m_act, m_max
			m_act, m_rat
			m_max, Q
			m_rat, Q
			m_max, W
			m_rat, W
			Q
			W

		"""


		# Input Verification
		for arg in kwargs:
			try: 
				float(kwargs[arg])
			except: 
				return print(f"Invalid Input... {krawgs[arg]}")


		# Define essential arguments
		if 'P_1' in kwargs:
			self.P_1 = kwargs['P_1']
		else:
			return print("Essential Argument not Specified (P_1).")

		if 'T_1' in kwargs:
			self.T_1 = kwargs['T_1']
		else:
			return print("Essential Argument not Specified (T_1).")

		if 'P_2' in kwargs:
			self.P_2 = kwargs['P_2']
		else:
			return print("Essential Argument not Specified (P_2).")


		# Define optional arguments
		if 'eff_mech' in kwargs:
			self.eff_mech = kwargs['eff_mech']

		if 'm_act' in kwargs:
			self.m_act = kwargs['m_act']
		else:
			self.m_act = None

		if 'm_max' in kwargs:
			self.m_max = kwargs['m_max']
		else:
			self.m_max = None

		if 'm_rat' in kwargs:
			self.m_rat = kwargs['m_rat']
		else:
			self.m_rat = None

		if 'Q' in kwargs:
			self.Q = kwargs['Q']
		else: self.Q = None

		if 'W' in kwargs:
			self.W = kwargs['W']
		else:
			self.W = None


		# Identify and solve problem
		if self.m_act == self.m_max == self.m_rat == self.Q == self.W == None:
			return print("No problem has been specified.\nClass Incomplete.")

		## Simple Spec'd Turbine
		elif self.m_act != None:
			if self.m_max != None:
				if self.m_rat != None or self.Q != None or self.W != None: #Try better
					return print("Problem is overspecified.")
				#Call simple spec (with max flow)
			elif self.m_rat != None:
				if self.Q != None or self.W != None: #Try better
					return print("Problem is overspecified.")
				#Call simple spec (with max flow ratio)
			else:
				#call simple spec (operating at max flow)

		## Target Heat at Outlet, assuming full condensation
		elif self.Q != None:
			if self.m_max != None:
				if self.m_rat != None or self.W != None: #Try better
					return print("Problem is overspecified.")
				#call heat spec (with max flow)
			elif self.m_rat != None:
				if self.W != None:
					return print("Problem is overspecified.")
				#call heat spec (with max flow ratio)
			else:
				#call heat spec (operating at max flow)

		## Target Work from Turbine
		elif self.W != None:
			if self.m_max != None:
				if self.m_rat != None:
					return print("Problem is overspecified.")
				# call work spec (with max flow)
			elif self.m_rat != None:
				# call work spec (with max flow ratio)
			else:
				# call work spec (operating at max flow)
		else:
			return print("No problem identified.")

		# Define Class types.
		# e.g et and outlet conditions, work, heat available, 

		# Define turbine str for print (nice little diagram)

