"""
This class models the Login thenre after homepage.
Class consists of login page object, Homepage objects and posts page objects
"""
from .Base_Page import Base_Page
from .werfolks_login_object import Werfolks_login_Object
from .werfolks_postspage_object import Werfolks_postspage_Object
from .werfolks_main_menu_object import werfolks_main_menu_object
from .werfolks_add_post_page_Object import werfolks_add_post_page_Object
from utils.Wrapit import Wrapit

class Werfolks_page(Base_Page,Werfolks_login_Object,Werfolks_postspage_Object,
                    werfolks_main_menu_object,werfolks_add_post_page_Object):

    "Page Object for the contact page"

    def start(self):
        "Use this method to go to specific URL -- if needed"
        url = 'page/login'
        self.open(url)

