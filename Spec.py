from WasRun import WasRun
from TestCase import TestCase
class TestCaseTest(TestCase):
	def setUp(self):
		self.test= WasRun("testMethod")
	def testRunning(self):
		self.test.run()
		assert(self.test.wasRun)
	def testSetUp(self):
		self.test.run()
		assert(self.test.wasSetUp)
		

def reportGreenBar():
		print "======================================="
		print "Green baar! Fuck Yea!"
		print "======================================="
	
TestCaseTest("testSetUp").run()
TestCaseTest("testRunning").run()
