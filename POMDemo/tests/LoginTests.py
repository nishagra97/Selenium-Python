from selenium import webdriver # To import the webdriver
from selenium.webdriver.common.by import By # to import By
import time # to import the time
import unittest

class LoginTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()  # call the webdriver
        cls.driver.implicitly_wait(10)

    def test_login_valid(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.find_element(By.NAME, "username").send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
        self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[1]/div[3]/ul/li/span").click()
        self.driver.find_element(By.LINK_TEXT, "Logout").click()
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")
