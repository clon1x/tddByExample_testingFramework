from TestFramework import TestCase, WasRun

class TestCaseTest(TestCase):
    def testRunning(self):
        test = WasRun("testMethod")
        assert(not test.wasRun)
        test.run()
        assert(test.wasRun)

    def testSetup(self):
        test = WasRun("testMethod")
        test.run()
        assert(test.wasSetUp)


TestCaseTest("testRunning").run()
TestCaseTest("testSetup").run()

print("Tests finished Ok")