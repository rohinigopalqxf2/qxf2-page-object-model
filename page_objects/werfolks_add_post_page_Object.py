"""
This class models the events page
"""

from .Base_Page import Base_Page
import conf.locators_conf as locators
from utils.Wrapit import Wrapit

class werfolks_add_post_page_Object:
    "Page object for the posts page"
    
    #locators
    new_post_heading = locators.werfolks_newpost_heading
    post_name = locators.werfolks_post_name
    post_desc = locators.werfolks_post_desc
    post_loc = locators.werfolks_post_loc
    post_category=locators.werfolks_post_category
    post_visibility = locators.werfolks_select_visibility
    post_submit = locators.werfolks_new_post_submit
    
    @Wrapit._exceptionHandler    
    def check_heading(self):
        "Check if the heading exists"
        result_flag = self.check_element_present(self.new_post_heading)
        self.conditional_write(result_flag,
            positive='Correct heading present on redirected page',
            negative='Heading on redirect page is INCORRECT!!',
            level='debug')

        return result_flag
   
    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def click_add_post(self):
        "Click on 'add new post link'"
        result_flag = self.click_element(self.add_post)
        self.conditional_write(result_flag,
            positive='Clicked on the "add new post" ',
            negative='Failed to click on " add new post" ',
            level='debug')

        return result_flag

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def select_post_category(self,option_text):
        "Click on post category"
        result_flag = self.select_dropdown_option(self.post_category,option_text)
        self.conditional_write(result_flag,
            positive='Selected the post category" ',
            negative='Failed to select post category',
            level='debug')

        return result_flag

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def select_post_visibility(self,visibility_text):
        "Select post visibility'"
        result_flag = self.select_dropdown_option(self.post_visibility,visibility_text)
        self.conditional_write(result_flag,
            positive='Selected post visibility option" ',
            negative='Failed to select post visibility',
            level='debug')

        return result_flag

    @Wrapit._exceptionHandler
    def set_post_name(self,name):
        "Set the post name"
        result_flag = self.set_text(self.post_name,name)
        self.conditional_write(result_flag,
            positive='Set the post name to: %s'%name,
            negative='Failed to set the post name',
            level='debug')

        return result_flag

    @Wrapit._exceptionHandler
    def set_post_desc(self,desc):
        "Set the post description"
        result_flag = self.set_text(self.post_desc,desc)
        self.conditional_write(result_flag,
            positive='Set the post description to: %s'%desc,
            negative='Failed to set the post description',
            level='debug')

        return result_flag
    
    @Wrapit._exceptionHandler
    def set_post_loc(self,loc):
        "Set the post location"
        result_flag = self.set_text(self.post_loc,loc)
        self.conditional_write(result_flag,
            positive='Set the post location to: %s'%loc,
            negative='Failed to set the post location',
            level='debug')

        return result_flag

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def click_submit_post(self):
        "Click on submit to create the post"
        result_flag = self.click_element(self.post_submit)
        self.conditional_write(result_flag,
            positive='Clicked on the "submit latest post" ',
            negative='Failed to click on "Submit latest post" button',
            level='debug')

        return result_flag