import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_Credence_003:
    @pytest.mark.skipif
    def test_CredKart_Login_008(self):
        driver = webdriver.Chrome()
        driver.get("https://automation.credence.in/login")
        driver.find_element(By.XPATH, "//input[@id='email']").send_keys("Credencetesttest1@test.com")
        driver.find_element(By.XPATH, "//input[@id='password']").send_keys("Credence@123")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()

        act_title = driver.title
        exp_title = "CredKart"
        if act_title == exp_title:
            print("Login is Passed")
        else:
            print("Login is Failed")
