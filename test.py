import unittest
from BasicClass import BasicClass

class TestBasicClass(unittest.TestCase):
    def testDoSomething(self):
        obj = BasicClass()
        assert obj.doSomething() == "Hello World"

if __name__ == "__main__":
    unittest.main()