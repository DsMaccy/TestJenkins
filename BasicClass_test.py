import unittest
from .BasicClass import BasicClass

def test_DoSomething():
    obj = BasicClass()
    assert obj.doSomething() == "Hello World"
def test_success():
    obj = BasicClass()
    assert True
# def test_fail():
#     obj = BasicClass()
#     assert False
