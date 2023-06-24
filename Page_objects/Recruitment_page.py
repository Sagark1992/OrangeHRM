import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class Recruitment_page:
    txt_username_name = (By.NAME, "username")
    txt_password_name = (By.NAME, "password")
    btn_login_class_name = (By.CLASS_NAME, "oxd-button")
    link_recruitment_xpath = (By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[5]/a")
    button_add_xpath= (By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button')
    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()

    def clickRecruitment(self):
        self.driver.find_element(*Recruitment_page.link_recruitment_xpath).click()
        time.sleep(3)


    def clickAdd(self):
        self.driver.find_element(*Recruitment_page.button_add_xpath).click()
        time.sleep(2)

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
