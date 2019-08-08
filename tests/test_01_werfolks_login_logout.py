"""
This is Automation test written for client prospecting actiivity done on werfolks.com
Our automated test will do the following:
    #open werolks.com's login page
    #Using existing credentials login to the app 
    # To ensure the login was successful - we check for login button again to ensure we have logged in successfully
    # To reach logout button, we need to click on profile icon first to get the menu containing logout button - another way to check login is succeeful
"""
import os,sys,time
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from page_objects.PageFactory import PageFactory
from utils.Option_Parser import Option_Parser
import conf.werfolks_conf as conf
import conf.testrail_caseid_conf as testrail_file


def test_werfolks_login(base_url,browser,browser_version,os_version,os_name,remote_flag,testrail_flag,tesults_flag,test_run_id,remote_project_name,remote_build_name):

    "Run the test"
    try:
        #Initalize flags for tests summary
        expected_pass = 0
        actual_pass = -1

        #1. Create a test object and fill the example form.
        test_obj = PageFactory.get_page_object("Werfolks login page",base_url=base_url)

        #2. Setup and register a driver
        start_time = int(time.time())	#Set start_time with current time
        test_obj.register_driver(remote_flag,os_name,os_version,browser,browser_version,remote_project_name,remote_build_name)

        
        #4. Get the test details from the conf file
        username  = conf.username
        password  = conf.password

        #5. Set username in form
        result_flag = test_obj.set_username(username) 
        test_obj.log_result(result_flag,
                            positive="Name was successfully set to: %s\n"%username,
                            negative="Failed to set name: %s \nOn url: %s\n"%(username,test_obj.get_current_url()))
        time.sleep(15)
        #6. Set password in form
        result_flag = test_obj.set_password(password) 
        
        test_obj.log_result(result_flag,
                            positive="password was successfully set to: %s\n"%password,
                            negative="Failed to set password: %s \nOn url: %s\n"%(password,test_obj.get_current_url()))

        time.sleep(15)
        #7. Click on Login button
        result_flag = test_obj.click_Login()

        test_obj.log_result(result_flag,
                            positive="Successfully submitted the form\n",
                            negative="Failed to submit the form \nOn url: %s"%test_obj.get_current_url())


        time.sleep(15)
        
        page_title = test_obj.get_page_title()
        print(page_title)

        #7. check if login button is present to check if the not present then login is successful

        login_flag = test_obj.get_login_button()
        if login_flag == False if result_flag == True else result_flag  == False:
            test_obj.log_result(result_flag,
                                positive="Login button not found hence login Successful!\n",
                                negative="Fail: Login Failed!")
        
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))
        time.sleep(15)

        """
        #commenting these 2 testcases as I have added above test case to check for login button after successful login
        
        #8. Click on profile icon 
        result_flag = test_obj.profile()
        test_obj.log_result(result_flag,
                            positive="Successfully clicked on profile icon the form\n",
                            negative="Failed to click profile icon \nOn url: %s"%test_obj.get_current_url())
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))
 

        #9. Click on signout
        result_flag = test_obj.Logout()
        test_obj.log_result(result_flag,
                            positive="Successfully Logged out\n",
                            negative="Failed to Logout the form \nOn url: %s"%test_obj.get_current_url())
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))
       """

        #8. Print out the results
        test_obj.write_test_summary()

        #Teardown
        test_obj.wait(3)
        expected_pass = test_obj.result_counter
        actual_pass = test_obj.pass_counter
        test_obj.teardown()
        
    except Exception as e:
        print("Exception when trying to run test:%s"%__file__)
        print("Python says:%s"%str(e))

    assert expected_pass == actual_pass, "Test failed: %s"%__file__
       
    
#---START OF SCRIPT   
if __name__=='__main__':
    print("Start of %s"%__file__)
    #Creating an instance of the class
    options_obj = Option_Parser()
    options = options_obj.get_options()
                
    #Run the test only if the options provided are valid
    if options_obj.check_options(options): 
        test_werfolks_login(base_url=options.url,
                        browser=options.browser,
                        browser_version=options.browser_version,
                        os_version=options.os_version,
                        os_name=options.os_name,
                        remote_flag=options.remote_flag,
                        testrail_flag=options.testrail_flag,
                        tesults_flag=options.tesults_flag,
                        test_run_id=options.test_run_id,
                        remote_project_name=options.remote_project_name,
                        remote_build_name=options.remote_build_name) 
    else:
        print('ERROR: Received incorrect comand line input arguments')
        #print(option_obj.print_usage())
