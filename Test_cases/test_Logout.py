import time
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from Page_objects.Login_Logout_page import Login_page
from Utilities.Read_data import Readconfig
from Utilities.Logger import LogGenerator

class Test_Logout:
    base_url= Readconfig.getUrl()
    username= Readconfig.getUsername()
    password= Readconfig.getPassword()
    log= LogGenerator.loggen()

    @allure.feature("OrangeHRM login")
    @allure.title("Title OrangeHRM login")
    @allure.step("Step 1")
    def test_Logout(self,setup):
        self.log.info("LogOut Test Execution Started")
        self.driver = setup
        self.log.info("URL Entering")
        self.driver.get(self.base_url)
        self.lp = Login_page(self.driver)
        time.sleep(3)
        self.log.info("Entering Username-->" + self.username)
        self.lp.enterUsername(self.username)
        self.log.info("Entering Password-->" + self.password)
        self.lp.enterPassword(self.password)
        self.log.info("Clicking on Login Button")
        self.lp.clickLogin()
        time.sleep(3)
        self.log.info("Clicking on Logout Button")
        self.lp.clickLogout()
        time.sleep(3)

        if self.lp.status_logout()==True:
            print("Logout successful")
            self.log.info("LogOut test case passed")
            self.log.info("Capturing Screenshot for test case passed")
            self.lp.save_Screenshot("\Test_loginOut_Pass.png")
            self.driver.close()
            assert True
        else:
            print("LogOut failed")
            self.log.info("LogOut test case failed")
            self.log.info("Capturing Screenshot for test case failed")
            self.lp.save_Screenshot("\Test_logOut_Fail.png")
            self.driver.close()
            assert False

        self.log.info("LogOut test execution completed")









