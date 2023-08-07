import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
class Test_Credence_002:
    def test_add(self):
        a=2
        b=8
        add=a+b
        print("Add:",str(add))
        if add==10:
            assert True
        else:
            assert False

    def test_mul(self):
        a=8
        b=7
        mul=a*b
        print("Mul:",str(mul))
        if mul==56:
            assert True
        else:
            assert False