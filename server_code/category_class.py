# create a class for creating categories

# this class should be able to have:
# members
# broadcastable
# can see
# is visible to
# filters
# IP:Port


# note that it is necessaty to save every instance of this
# class to any variable, otherwise it shall be deleted from
# the registry!!!!!!!!!!


class category():
	"""docstring for category"""
	# Registry of all the categories
	instances = []
	def __init__(self,
		name,
		members = [],
		broadcastable = False,
		cansee = [],
		#isvisibleto = [],
		#filters = [],
		IP = []
	 ):
		self.name = name
		self.members = members
		self.broadcastable = broadcastable
		self.cansee = cansee
		#self.isvisibleto = []
		#self.filters = filters
		self.IP = IP
		#from weakref import proxy
		#self.proxy = proxy(self)
		#category.instances.append(self.proxy)
		category.instances.append(self)
	def __del__(self):
		# Remove from the registry
		#category.instances.remove(self.proxy)
		#print('deleted {0}'.format(self.name))
		try:
			category.instances.remove(self)
		except:
			pass
		#print('removed {0}'.format(self.name))





