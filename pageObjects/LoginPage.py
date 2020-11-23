class LoginPage:
    # Login Page
    textbox_username_id = "Email"
    textbox_password_id = "Password"
    button_login_xpath = "//input[@value='Log in']"
    link_logout_linktext = "Logout"
    logged_In_userName_xpath = "//li[@class='account-info']"

    # Business Logic
    def __init__(self,driver):
        self.driver=driver

    def setUserName(self, username):
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element_by_link_text(self.link_logout_linktext).click()

    def verifyLoggedInUser(self):
        name = self.driver.find_element_by_xpath(self.logged_In_userName_xpath).text
        print("Logged in user is : ", name)