import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class Login_page:
    txt_username_name = (By.NAME, "username")
    txt_password_name = (By.NAME, "password")
    btn_login_class_name = (By.CLASS_NAME, "oxd-button")
    link_profile_class_name = (By.CLASS_NAME, "oxd-userdropdown-name")
    link_logout_link_text = (By.LINK_TEXT, "Logout")

    def __init__(self, driver):
        self.driver = driver

    def enterUsername(self, username):
        self.driver.find_element(*Login_page.txt_username_name).send_keys(username)

    def enterPassword(self, password):
        self.driver.find_element(*Login_page.txt_password_name).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(*Login_page.btn_login_class_name).click()

    def clickLogout(self):
        self.driver.find_element(*Login_page.link_profile_class_name).click()
        time.sleep(3)
        self.driver.find_element(*Login_page.link_logout_link_text).click()

    def status_login(self):
        try:
            self.driver.find_element(By.CLASS_NAME, "oxd-userdropdown-tab")
            return True
        except NoSuchElementException:
            return False

    def status_logout(self):
        if self.driver.current_url=="https://opensource-demo.orangehrmlive.com/web/index.php/auth/login":
            return True
        else:
            return False

    def save_Screenshot(self, name):
        self.driver.save_screenshot("D:\Sagar Study\pythonProject\OrangeHRM\Screenshots" + name)
