"""
This class models login page objects
"""

from .Base_Page import Base_Page
import conf.locators_conf as locators
from utils.Wrapit import Wrapit

class werfolks_main_menu_object:
    "Page object for the menu"
    
    #locators
    add_icon = locators.werfolks_add_button
    logout_button =locators.werfolks_signout
    profile_icon = locators.werfolks_profileicon
    add_post = locators.werfolks_add_post
    #Add_post = locators.werfolks_add_post

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def click_add_icon(self):
        "Click on 'Add' button in the menu "
        result_flag = self.click_element(self.add_icon)
        self.conditional_write(result_flag,
            positive='Clicked on the "Add" button',
            negative='Failed to click on "Add" button',
            level='debug')

        return result_flag
    

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def click_profile_icon(self):
        "Click on profile button"
        result_flag = self.click_element(self.profile_icon)
        self.conditional_write(result_flag,
            positive='Clicked on the profile menu',
            negative='Failed to click on profile menu',
            level='debug')

        return result_flag
    
     
    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def addpost(self):
        "Click on 'Add post menu"
        result_flag = self.click_element(self.add_post)
        self.conditional_write(result_flag,
            positive='Clicked on the Add post menu',
            negative='Failed to click on Add post menu',
            level='debug')

        return result_flag

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def Logout(self):
        "Click on Logout menu"
        result_flag = self.click_element(self.logout_button)
        self.conditional_write(result_flag,
            positive='Clicked on the Logout menu',
            negative='Failed to click on Logout menu',
            level='debug')

        return result_flag

   