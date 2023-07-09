from selenium.webdriver.common.by import By
from Pages.base_page import BaseClass


class LoginPage(BaseClass):
    """
    LoginPage class
    """
    Home_Page_Text = [By.XPATH, "//h2[contains(text(),'Test login')]"]
    User_Input_Text_Box = [By.XPATH, "//input[@name='username']"]
    Password_Input_Text_Box = [By.XPATH, "//input[@name='password']"]
    Submit_Button = [By.XPATH, "//button[@id='submit']"]
    Error_Message = [By.XPATH, "//div[@id='error']"]
    Logout_Button = [By.XPATH, "//a[contains(text(),'f')]"]

    def __init__(self, driver):
        """
        constructor for LoginPage Class
        """
        super().__init__(driver)
        self.driver = driver

    def get_text_home(self):
        """
        method is get text from home
        """
        return self.get_text(self.Home_Page_Text)

    def login_user_input_box_clear(self):
        """
        method is clear Username input box
        """
        return self.clear_text(self.User_Input_Text_Box)

    def username_input(self, username):
        """
        method is username enter for input box
        :param username: {str}
        """
        return self.send_text(self.User_Input_Text_Box, username)

    def login_password_input_box_clear(self):
        """
        method is clear password input box
        """
        return self.clear_text(self.Password_Input_Text_Box)

    def password_input(self, Password):
        """
        method is password enter for input box
        :param Password: {str}
        """
        return self.send_text(self.Password_Input_Text_Box, Password)

    def click_submit_button(self):
        """
        method is click on submit button
        """
        return self.click(self.Submit_Button)

    def get_error_message(self):
        """
        method is get error message
        """
        return self.get_text(self.Error_Message)

    def get_text_successfully_login(self):
        return self.get_text(self.Logout_Button)

    def logout_button_visible(self):
        return self.is_visible_check(self.Logout_Button)
