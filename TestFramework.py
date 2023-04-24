class TestCase:
    def __init__(self, name) -> None:
        self.name = name

    def setUp(self):
        pass
    
    def run(self):
        self.setUp()
        exec ("self." + self.name + "()")

class WasRun(TestCase):
    def __init__(self, name) -> None:
        self.wasRun = None
        TestCase.__init__(self, name)
        
    def testMethod(self):
        self.wasRun = 1

    def setUp(self):
        self.wasSetUp = 1
