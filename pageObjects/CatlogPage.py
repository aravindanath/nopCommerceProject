
import time
class CatlogPage:
    # Catlog Page

    catlog_Menu_xpath ="//span[text()='Catalog']"
    categories_xpath ="//span[text()='Categories']"
    categoriesNameSearch_xpath="//input[@id='SearchCategoryName']"
    categores_Search_xpath ="//button[@id='search-categories']"


    # Business Logic
    def __init__(self,driver):
        self.driver=driver

    def searchProductCategories(self, product):
        self.driver.find_element_by_xpath(self.catlog_Menu_xpath).click()
        time.sleep(2)
        self.driver.find_element_by_xpath(self.categories_xpath).click()
        self.driver.find_element_by_xpath(self.categoriesNameSearch_xpath).send_keys(product)
        self.driver.find_element_by_xpath(self.categores_Search_xpath).click()



    def verifyLoggedInUser(self):
        name = self.driver.find_element_by_xpath(self.logged_In_userName_xpath).text
        print("Logged in user is : ", name)