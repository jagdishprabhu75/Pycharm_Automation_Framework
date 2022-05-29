from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common import by
from selenium.webdriver.common.alert import Alert


class Login_Page:
    USERNAME_TEXTBOX_NAME = "userName"
    PASSWORD_TEXTBOX_NAME = "password"
    LOGIN_BUTTON_NAME = "submit"
    SIGNOFF_LINK_XPATH = "//a[text()='SIGN-OFF']"

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(by.By.NAME, self.USERNAME_TEXTBOX_NAME).click()
        self.driver.find_element(by.By.NAME, self.USERNAME_TEXTBOX_NAME).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(by.By.NAME, self.PASSWORD_TEXTBOX_NAME).send_keys(password)

    def click_login(self):
        self.driver.find_element(by.By.NAME, self.LOGIN_BUTTON_NAME).click()
        self.driver.find_element(by.By.CSS_SELECTOR, "h3").click()

    def sign_off(self):
        #Alert.dismiss()
        try:
            self.driver.find_element(by.By.XPATH, self.SIGNOFF_LINK_XPATH).click()
        except NoSuchElementException:
            print("No such element found")

#dismiss-button