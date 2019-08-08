"""
This is Automation test written for client prospecting actiivity done on werfolks.com
Our automated test will do the following:
    # open werolks.com's login page
    # Using existing credentials login to the app 
    # Click on profile icon then click on Add icon
    # Select the Post option 
    # Add a post details by passing values from conf
    # Logout from app
"""
import os,sys,time
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from page_objects.PageFactory import PageFactory
from utils.Option_Parser import Option_Parser
import conf.werfolks_conf as conf
import conf.testrail_caseid_conf as testrail_file


def test_werfolks_login_add_delete_post(base_url,browser,browser_version,os_version,os_name,remote_flag,testrail_flag,tesults_flag,test_run_id,remote_project_name,remote_build_name):

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
        
        #3. Get the test details from the conf file
        username  = conf.username
        password  = conf.password

        name = conf.post_name
        desc = conf.post_desc
        loc = conf.post_location
        option_text = conf.option_text
        visibility_text = conf.visibility_text

        #4. Set username in form
        result_flag = test_obj.set_username(username) 
        test_obj.log_result(result_flag,
                            positive="Name was successfully set to: %s\n"%username,
                            negative="Failed to set name: %s \nOn url: %s\n"%(username,test_obj.get_current_url()))
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))

        #5. Set password in form
        result_flag = test_obj.set_password(password) 
        test_obj.log_result(result_flag,
                            positive="password was successfully set to: %s\n"%password,
                            negative="Failed to set password: %s \nOn url: %s\n"%(password,test_obj.get_current_url()))
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))
        
        #6. Click on Login button
        result_flag = test_obj.click_Login()
        test_obj.log_result(result_flag,
                            positive="Successfully submitted the form\n",
                            negative="Failed to submit the form \nOn url: %s"%test_obj.get_current_url())
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))
        time.sleep(15)

        #7. Click on profile icon 
        result_flag = test_obj.click_profile_icon()
        test_obj.log_result(result_flag,
                            positive="Successfully clicked on profile icon the form\n",
                            negative="Failed to click profile icon \nOn url: %s"%test_obj.get_current_url())
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))  
        time.sleep(15)

        #8. Click on Add icon 
        result_flag = test_obj.click_add_icon()
        test_obj.log_result(result_flag,
                            positive="Successfully clicked on Add icon the form\n",
                            negative="Failed to click Add icon \nOn url: %s"%test_obj.get_current_url())
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))
        time.sleep(15)

        #9.click on Post icon
        result_flag = test_obj.click_add_post()
        test_obj.log_result(result_flag,
                            positive="Successfully clicked on Add post icon the form\n",
                            negative="Failed to click Add post icon \nOn url: %s"%test_obj.get_current_url())
        time.sleep(15)

        #10. checking New Post page heading
        if result_flag is True:
                result_flag = test_obj.check_heading()
                test_obj.log_result(result_flag,
                                positive="Heading on the redirect page checks out!\n",
                                negative="Fail: Heading on the redirect page is incorrect!")
        time.sleep(15)
        
        #11.Set post name 
        result_flag = test_obj.set_post_name(name) 
        test_obj.log_result(result_flag,
                            positive="post name was successfully set to: %s\n"%name,
                            negative="Failed to set post namec: %s \nOn url: %s\n"%(name,test_obj.get_current_url()))
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))
        time.sleep(15)

        #11.Select post category
        result_flag = test_obj.select_post_category(option_text) 
        test_obj.log_result(result_flag,
                            positive="post category was successfully selected to: %s\n"%option_text,
                            negative="Failed to set post category: %s \nOn url: %s\n"%(option_text,test_obj.get_current_url()))
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))
        time.sleep(15)
        
        #11.Set post desc
        result_flag = test_obj.set_post_desc(desc) 
        test_obj.log_result(result_flag,
                            positive="post desc was successfully set to: %s\n"%desc,
                            negative="Failed to set post desc: %s \nOn url: %s\n"%(desc,test_obj.get_current_url()))
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))
        time.sleep(15)

        #11. Select post visibility option
        result_flag = test_obj.select_post_visibility(visibility_text) 
        test_obj.log_result(result_flag,
                            positive="post category was successfully selected to: %s\n"%option_text,
                            negative="Failed to set post category: %s \nOn url: %s\n"%(option_text,test_obj.get_current_url()))
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))
        time.sleep(15)

        #9.click on submit
        result_flag = test_obj.click_submit_post()
        test_obj.log_result(result_flag,
                            positive="Successfully clicked on Add post icon the form\n",
                            negative="Failed to click Add post icon \nOn url: %s"%test_obj.get_current_url())
        time.sleep(15)

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
        test_werfolks_login_add_delete_post(base_url=options.url,
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
