from WasRun import WasRun
from TestCase import TestCase

class TestCaseTest(TestCase):
	def testTemplateMethod(self):
		test= WasRun("testMethod")
		test.run()
		assert("setUp testMethod tearDown " == test.log)
	def testResult(self):
		test= WasRun("testMethod")
		result= test.run()
		assert("1 run, 0 failed" == result.summary())
	def testFailedResult(self):
		test= WasRun("testBrokenMethod")
		result= test.run()
		assert("1 run, 1 failed" == result.summary)
	def testFailedResultFormatting(self):
		result= TestResult()
		result.testStarted()
		result.testFailed()
		assert("1 run, 1 failed" == result.summary())
def reportGreenBar():
		print "======================================="
		print "Green baar! Fuck Yea!"
		print "======================================="
	
TestCaseTest("testTemplateMethod").run()
TestCaseTest("testResult").run()
TestCaseTest("testFailedResult").run()