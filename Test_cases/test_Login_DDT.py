import time
import allure
import openpyxl
from Page_objects.Login_Logout_page import Login_page
from Utilities.Read_data import Readconfig
from Utilities.Logger import LogGenerator
from Utilities import XL_Utils

class Test_Login:
    base_url= Readconfig.getUrl()
    username= Readconfig.getUsername()
    password= Readconfig.getPassword()
    log= LogGenerator.loggen()
    path= "D:\Sagar Study\pythonProject\OrangeHRM\Test_cases\Test_data\Login_data.xlsx"

    @allure.feature("OrangeHRM login")
    @allure.title("Title OrangeHRM login")
    @allure.step("Step 1")
    def test_login(self,setup):
        self.log.info("Login Test Execution Started")
        self.driver = setup
        self.log.info("URL Entering")
        self.driver.get(self.base_url)
        self.lp= Login_page(self.driver)
        self.rows= XL_Utils.getRowcount(self.path,"Sheet1")
        loginStatus=[]
        for r in range (2,self.rows+1):
            self.username= XL_Utils.readData(self.path,"Sheet1",r,1)
            self.password= XL_Utils.readData(self.path,"Sheet1",r,2)
            self.exp_result= XL_Utils.readData(self.path,"Sheet1",r,3)
            time.sleep(3)
            self.log.info("Entering Username-->"+ self.username)
            self.lp.enterUsername(self.username)
            self.log.info("Entering Password-->"+ self.password)
            self.lp.enterPassword(self.password)
            self.log.info("Clicking on Login Button")
            self.lp.clickLogin()
            time.sleep(3)

            if self.lp.status_login()==True:
                XL_Utils.writeData(self.path,"Sheet1",r,4,"Pass")
                if self.exp_result=="Pass":
                    loginStatus.append("Pass")
                    XL_Utils.writeData(self.path,'Sheet1',r,4,"Pass")
                    self.lp.save_Screenshot("\Test_login_DDT__Pass.png")
                    self.log.info("Clicking on Logout Button")
                    self.lp.clickLogout()
                elif self.exp_result=="Fail":
                    loginStatus.append("Fail")
                    XL_Utils.writeData(self.path, 'Sheet1', r, 4, "Fail")
                    self.lp.save_Screenshot("\Test_login_DDT_Fail.png")
                    self.log.info("Clicking on Logout Button")
                    self.lp.clickLogout()
            elif self.lp.status_login()==False:
                XL_Utils.writeData(self.path,"Sheet1",r,4,"Fail")
                if self.exp_result=="Fail":
                    loginStatus.append("Fail")
                    XL_Utils.writeData(self.path,'Sheet1',r,4,"Fail")
                    self.lp.save_Screenshot("\Test_login_DDT_Fail.png")
                    self.driver.refresh()
                elif self.exp_result=="Fail":
                    loginStatus.append("Fail")
                    XL_Utils.writeData(self.path, 'Sheet1', r, 4, "Pass")
                    self.lp.save_Screenshot("\Test_login_DDT_Fail.png")
                    self.lp.clickLogout()
        self.log.info("Login_DDT Test Execution Completed")
        self.driver.close()
        print(loginStatus)
        if "Fail" not in loginStatus:
            self.log.info("Testcases test_login_DDT_003 is passed")
            assert True
        else:
            self.log.info("Testcases test_login_DDT_003 is failed")
            assert False
