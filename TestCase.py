class TestCase:
	def __init__(self, name):
		self.name= name
	def setUp(self):
		self.wasSetUp = 1
	def run(self, result):
		result.testStarted()
		self.setUp()
		method = getattr(self, self.name)
		method()
		self.tearDown()
	def tearDown(self):
		pass