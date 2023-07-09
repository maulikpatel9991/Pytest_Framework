import time
import pytest
from Pages.login_page import LoginPage
from Config.read_data import read_data_ini
from pytest_csv_params.decorator import csv_params

"""
All Testcase Run Order Wise
User Different Marks 1)parameterize 2)xfail
Read Data From Csv File using CSV Params
"""


@pytest.mark.usefixtures("use_get_driver")
class TestLogin:
    """
    TestLogin Class Define
    """

    @pytest.fixture(autouse=True)
    def classObject(self):
        self.login_page = LoginPage(self.driver)

    @pytest.mark.order(0)
    def test_home_page_text(self) -> None:
        """
         Test Home Page Text method is get text from home page after compare actual-result and expected result
        """
        # self.login_page = LoginPage(self.driver)
        actual_result = self.login_page.get_text_home()
        result = "did not match expected value {} but got {}".format(read_data_ini('Home_Page_Text', 'text'),
                                                                     actual_result)
        assert actual_result == read_data_ini('Home_Page_Text', 'text'), pytest.fail("Fail {}".format(result))

    """
    Below test case get value for Parametrize mark
    """

    @pytest.mark.order(1)
    @pytest.mark.parametrize("User_Name, Password",
                             [('maulik', 'maulik'), ('student', 'pass'), ('Student', 'Password123')], )
    def test_Negative_username_password(self, User_Name: str, Password: str) -> None:
        """
        This method is first get value which I have to define in the parameter-marks under list after
        enter both value in input box check validations.
        :param User_Name: {str}   get User_Name which I have defined in the parameter-marks under list
        :param Password:  {str}   get Password which I have defined in the parameter-marks under list
        """
        # self.login_page = LoginPage(self.driver)
        self.login_page.login_user_input_box_clear()
        self.login_page.username_input(User_Name)
        time.sleep(3)
        self.login_page.login_password_input_box_clear()
        self.login_page.password_input(Password)
        self.login_page.click_submit_button()
        message = ["Your username is invalid!", "Your password is invalid!"]
        error_message = self.login_page.get_error_message()
        assert True if error_message in message else False

    """
    Below Test case get value for csv file using csv params
    """

    @pytest.mark.order(2)
    @csv_params(
        data_file="Config/user_credentials.csv",
        id_col="id",
    )
    def test_csvfile_read_data_username_password(self,
                                                 username, password
                                                 ) -> None:
        """
        This method is first get value which I have to define in the CSV FILE after
        enter both value in input box check validations.
        :param username: get username which I have defined in the csv file
        :param password: get password which I have defined in the csv file
        :return:
        """
        # self.login_page = LoginPage(self.driver)
        self.login_page.login_user_input_box_clear()
        self.login_page.username_input(username)
        time.sleep(3)
        self.login_page.login_password_input_box_clear()
        self.login_page.password_input(password)
        self.login_page.click_submit_button()
        message = ["Your username is invalid!", "Your password is invalid!"]
        error_message = self.login_page.get_error_message()
        assert True if error_message in message else False

    @pytest.mark.order(3)
    def test_login(self):
        self.login_page.login_user_input_box_clear()
        self.login_page.username_input("student")
        self.login_page.login_password_input_box_clear()
        self.login_page.password_input("Password123")
        self.login_page.click_submit_button()
        time.sleep(10)
        self.login_page.logout_button_visible()