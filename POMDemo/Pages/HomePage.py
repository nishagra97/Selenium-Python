from selenium.webdriver.common.by import By

from POMDemo.Locators.locators import Locators # import the class locators


class HomePage: # create a class


    def __init__(self, driver): # create the construction
        self.driver = driver # call the driver
        self.about_button_XPATH  = Locators.about_button_XPATH # use the locator
        self.logout_button_LINK_TEXT = Locators.logout_button_LINK_TEXT # use the locator

    def about(self): # create the function to call  the methods
        self.driver.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/header/div[1]/div[3]/ul/li/span").click()

    def click_logout(self):
        self.driver.find_element(By.LINK_TEXT,"Logout").click()
