import unittest
from BasicClass import BasicClass

class TestBasicClass(unittest.TestCase):
    def testDoSomething(self):
        obj = BasicClass()
        assert obj.doSomething() == "Hello World"
    def newTest(self):
        assert True

if __name__ == "__main__":
    unittest.main()