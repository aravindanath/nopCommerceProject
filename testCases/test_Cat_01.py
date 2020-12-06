import pytest
from selenium import webdriver

from pageObjects.CatlogPage import CatlogPage
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import time

class Test_CAT_001:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger=LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_homePageTitle(self,setup):
        self.logger.info("*************** Test_CAT_001 *****************")
        self.logger.info("****Started Home page title test ****")
        self.driver = setup
        self.logger.info("****Opening URL****")
        self.driver.get(self.baseURL)
        act_title=self.driver.title

        if act_title=="Your store. Login":
            self.logger.info("**** Home page title test passed ****")
            self.driver.close()
            assert True
        else:
            self.logger.error("**** Home page title test failed****")
            self.driver.save_screenshot("..//Screenshots//"+"test_homePageTitle.png")
            self.driver.close()
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self,setup):

        self.logger.info("****Started Login Test****")
        self.driver = setup
        self.driver.get(self.baseURL)
        # Login page object
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.lp.verifyLoggedInUser()

        act_title=self.driver.title
        # if act_title=="Dashboard / nopCommerce administration":
        #     self.logger.info("****Login test passed ****")
        #     self.driver.close()
        #     assert True
        # else:
        #     self.logger.error("****Login test failed ****")
        #     self.driver.save_screenshot("..//Screenshots//" + "test_homePageTitle.png")
        #     self.driver.close()
        #     assert False

        self.cp = CatlogPage(self.driver)
        time.sleep(5)
        self.cp.searchProductCategories("Computers")
        self.driver.save_screenshot("..//Screenshots//" + "test_Cat.png")
        self.driver.close()




