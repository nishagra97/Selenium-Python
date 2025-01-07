import os  # This code is to run from CL
import sys  # This code is to run from CL
import time  # to import the time
import unittest
from selenium import webdriver  # To import the webdriver
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "..")) # This code is to run from CL  and the number of dots represent here the nested folders.you can increase or decrease the dots.
from POMDemo.Pages.LoginPage import LoginPage
from POMDemo.Pages.HomePage import HomePage
import HtmlTestRunner


class LoginTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()  # call the webdriver
        cls.driver.implicitly_wait(10)

    def test_login_valid(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# locators for login page

        LoginP = LoginPage(driver)
        LoginP.enter_username()
        LoginP.enter_password()
        LoginP.click_login()

# locators for home page

        Home = HomePage(driver)
        Home.about()
        Home.click_logout()

        # self.driver.find_element(By.NAME, "username").send_keys("Admin")
        # self.driver.find_element(By.NAME, "password").send_keys("admin123")
        # self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
        # self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[1]/div[3]/ul/li/span").click()
        # self.driver.find_element(By.LINK_TEXT, "Logout").click()
        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")




if __name__ == '__main__': # This code is to run from CL
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/nisha/OneDrive/Documents/Interview_prep_2024/Python/PythonByRaghav/code/PageObjectModel/Reports'))        # This code is to run from CL
