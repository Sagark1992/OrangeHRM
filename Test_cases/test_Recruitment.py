import time
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from Page_objects.Login_Logout_page import Login_page
from Utilities.Read_data import Readconfig
from Utilities.Logger import LogGenerator
from Page_objects.Recruitment_page import Recruitment_page

class Test_Recruitment:
    base_url= Readconfig.getUrl()
    username= Readconfig.getUsername()
    password= Readconfig.getPassword()
    log= LogGenerator.loggen()

    @allure.feature("OrangeHRM Recruitment")
    @allure.title("Title OrangeHRM Recruitment")
    @allure.step("Step 1")
    def test_login(self,setup):
        self.log.info("Recruitment Test Execution Started")
        self.driver = setup
        self.log.info("URL Entering")
        self.driver.get(self.base_url)
        self.lp= Login_page(self.driver)
        time.sleep(3)
        self.log.info("Entering Username-->"+ self.username)
        self.lp.enterUsername(self.username)
        self.log.info("Entering Password-->"+ self.password)
        self.lp.enterPassword(self.password)
        self.log.info("Clicking on Login Button")
        self.lp.clickLogin()
        time.sleep(3)
        self.rp= Recruitment_page(self.driver)
        self.rp.clickRecruitment()
        self.rp.clickAdd()














        # if self.lp.status_login()==True:
        #     print("Login successful")
        #     self.log.info("Login test case passed")
        #     self.log.info("Capturing Screenshot for test case passed")
        #     self.lp.save_Screenshot("\Test_login_Pass.png")
        #     self.driver.close()
        #     assert True
        # else:
        #     print("Login failed")
        #     self.log.info("Login test case failed")
        #     self.log.info("Capturing Screenshot for test case failed")
        #     self.lp.save_Screenshot("\Test_login_Fail.png")
        #     self.driver.close()
        #     assert False
        #
        # self.log.info("Login test execution completed")
