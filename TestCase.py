class TestCase:
	def __init__(self, name):
		self.name= name
	def setUp(self):
		self.wasSetUp = 1
	def run(self):
		self.setUp()
		method = getattr(self, self.name)
		method()