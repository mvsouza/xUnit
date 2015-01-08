from TestResult import TestResult
class TestCase:
	def __init__(self, name):
		self.name= name
	def setUp(self):
		self.wasSetUp = 1
	def run(self):
		result = TestResult()
		result.testStarted()
		self.setUp()
		method = getattr(self, self.name)
		method()
		self.tearDown()
		return TestResult()
	def tearDown(self):
		pass