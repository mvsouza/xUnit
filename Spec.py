from WasRun import WasRun
from TestCase import TestCase
class TestCaseTest(TestCase):
	def testRunning(self):
		test= WasRun("testMethod")
		assert(not test.wasRun)
		test.run()
		assert(test.wasRun)
		print "======================================="
		print "Green baar! Fuck Yea!"
		print "======================================="

TestCaseTest("testRunning").run()