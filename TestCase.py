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
		try:
			method = getattr(self, self.name)
			method()
		except:
			result.testFailed()
		self.tearDown()
		return TestResult()
	def tearDown(self):
		pass