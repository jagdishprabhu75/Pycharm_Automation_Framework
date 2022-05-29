import pytest
from pages.login_page import Login_Page
from utilities.xl_operation import read_excel


@pytest.mark.usefixtures("setup")
@pytest.mark.parametrize("username, password", read_excel())
class Test_Mercury_Login:
    def test_login(self, username, password):
        login = Login_Page(self.driver)
        login.enter_username(username)
        login.enter_password(password)
        login.click_login()
        login.sign_off()