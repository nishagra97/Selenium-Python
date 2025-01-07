from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest

class TestSample(): #in pytest, class should start with Test
    @pytest.fixture() # to run this particular test everytime
    def test_setup(self): # This function is used for pytest
        global driver # make the driver global so its accessible to all
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.maximize_window()
        yield
        driver.close()
        driver.quit()
        print("Test Completed")

    def test_login(self,test_setup): # makesure it stars with test

        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.find_element(By.NAME, "username").send_keys("Admin")
        driver.find_element(By.NAME, "password").send_keys("admin123")
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()

    # def test_teardown():
    #     driver.close()
    #     driver.quit()
    #     print("Test Completed")