from selenium.webdriver.common.by import By
from POMDemo.Locators.locators import Locators # import the locators

class LoginPage():  # create a class

    def __init__(self, driver):  # create the construction
        self.driver = driver  # call the driver
        self.username_textbox_name = Locators.username_textbox_name # use the locator
        # self.username_textbox_name = self.driver.find_element(By.NAME, "username")
        self.password_textbox_name = Locators.password_textbox_name # use the locator
        # self.password_textbox_name = self.driver.find_element(By.NAME, "password")
        self.login_button_XPATH = Locators.login_button_XPATH # use the locator

    def enter_username(self):  # create the function to call  the methods
        self.driver.find_element(By.NAME, "username").send_keys(self.username_textbox_name)

    def enter_password(self):
        self.driver.find_element(By.NAME, "password").send_keys(self.password_textbox_name)

    def click_login(self):
        self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()


