"""
This class models the posts page
"""

from .Base_Page import Base_Page
import conf.locators_conf as locators
from utils.Wrapit import Wrapit

class Werfolks_postspage_Object:
    "Page object for the Posts page"
    
    #locators
    latestpost_link = locators.werfolks_latestpost_link
    new_postheading = locators.werfolks_latestpost_heading
    latest_postheading = locators.werfolks_latestpost_heading

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def latestpost(self):
        "Click on 'Latest post link'"
        result_flag = self.click_element(self.latestpost_link)
        self.conditional_write(result_flag,
            positive='Clicked on the "latest post" ',
            negative='Failed to click on "latest post" link',
            level='debug')

        return result_flag
   
    @Wrapit._exceptionHandler    
    def check_heading(self):
        "Check if the Latest post heading exists"
        result_flag = self.check_element_present(self.new_postheading)
        self.conditional_write(result_flag,
            positive='Correct heading present on redirect page',
            negative='Heading on redirect page is INCORRECT!!',
            level='debug')

        return result_flag

    @Wrapit._exceptionHandler    
    def check_heading_post(self):
        "Check if the post heading exists"
        result_flag = self.check_element_present(self.latest_postheading)
        self.conditional_write(result_flag,
            positive='Correct heading present on redirect page',
            negative='Heading on redirect page is INCORRECT!!',
            level='debug')

        return result_flag