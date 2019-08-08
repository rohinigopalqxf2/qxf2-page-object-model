"""
This class models login page objects
"""

from .Base_Page import Base_Page
import conf.locators_conf as locators
from utils.Wrapit import Wrapit

class Werfolks_login_Object:
    "Page object for the Login and homepage"
    
    #locators
    username = locators.werfolks_username
    password = locators.werfolks_password
    login_button = locators.werfolks_login
    logout_button =locators.werfolks_signout
    profile_icon = locators.werfolks_profileicon

    @Wrapit._exceptionHandler
    def set_username(self,username):
        "Set the username on the login page"
        result_flag = self.set_text(self.username,username)
        self.conditional_write(result_flag,
            positive='Set the username to: %s'%username,
            negative='Failed to set the username in the login',
            level='debug')

        return result_flag

    @Wrapit._exceptionHandler
    def set_password(self,password):
        "Set the password on the login"
        result_flag = self.set_text(self.password,password)
        self.conditional_write(result_flag,
            positive='Set the password to: %s'%password,
            negative='Failed to set the password in the login',
            level='debug')

        return result_flag

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def click_Login(self):
        "Click on 'Login' button"
        result_flag = self.click_element(self.login_button)
        self.conditional_write(result_flag,
            positive='Clicked on the "Login" button',
            negative='Failed to click on "Login" button',
            level='debug')

        return result_flag

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def get_login_button(self):
        "Get the login button control"
        result_flag = self.check_element_present(self.login_button)
        self.conditional_write(result_flag,
            positive='Get the "Login" button',
            negative='Failed to find on "Login" button',
            level='debug')

        return result_flag

   
