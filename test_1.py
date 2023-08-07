import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

class Test_Credence_001:
    def test_sum(self):
        a=6
        b=9
        sum=a+b
        print("Sum:",sum)
        if sum==15:
            assert True
        else:
            assert False
