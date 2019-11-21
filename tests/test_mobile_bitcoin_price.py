"""
Automated test will do the following:
    # Open Bitcoin Info application in emulator.
    # Click on the bitcoin real time price page button.
    # Compare expected bitcoin real time price page heading with current page heading.
    # Verify that the bitcoin real time price is displayed on the page.
    # Display the results.
"""
import os, sys, time
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from page_objects.PageFactory import PageFactory
from utils.Option_Parser import Option_Parser
import conf.mobile_bitcoin_conf as conf
import conf.testrail_caseid_conf as testrail_file


def test_mobile_bitcoin_price(test_obj_mobile):
    "Run the test."
    try:
        # Initalize flags for tests summary.
        expected_pass = 0
        actual_pass = -1

        #1. Create a test object.
        test_obj_mobile = PageFactory.get_page_object("bitcoin main page")      
        
        #2. Setup and register a driver
        start_time = int(time.time())

        #3. Get expected bitcoin price page header name
        expected_bitcoin_price_page_heading = conf.expected_bitcoin_price_page_heading
        
        #4. Click on real time price page button and verify the price page header name.
        result_flag = test_obj_mobile.click_on_real_time_price_button(expected_bitcoin_price_page_heading)
        test_obj_mobile.log_result(result_flag,
                    positive="Successfully visited the bitcoin real time price page.",
                    negative="Failed to visit the bitcoin real time price page.")
        #Update TestRail
        case_id = testrail_file.test_bitcoin_price_page_header
        test_obj_mobile.report_to_testrail(case_id,test_obj_mobile.test_run_id,result_flag)
        test_obj_mobile.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))
        
        #5. Verify bitcoin real time price is displayed.
        if result_flag is True:
            result_flag = test_obj_mobile.get_bitcoin_real_time_price()
        test_obj_mobile.log_result(result_flag,
                            positive="Successfully got the bitcoin real time price in usd.",
                            negative="Failed to get the bitcoin real time price in usd.")
        #Update TestRail
        case_id = testrail_file.test_bitcoin_real_time_price
        test_obj_mobile.report_to_testrail(case_id,test_obj_mobile.test_run_id,result_flag)
        test_obj_mobile.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))
        
        #6. Print out the results.
        test_obj_mobile.write_test_summary()

        #7. Teardown and Assertion.
        test_obj_mobile.wait(3)
        expected_pass = test_obj_mobile.result_counter
        actual_pass = test_obj_mobile.pass_counter

    except Exception as e:
        print("Exception when trying to run test:%s" % __file__)
        print("Python says:%s" % str(e))

    assert expected_pass == actual_pass,"Test failed: %s"%__file__


# ---START OF SCRIPT

if __name__ == '__main__':
    print("Start of %s" % __file__)
    # Creating an instance of the class.
    options_obj = Option_Parser()
    options = options_obj.get_options()
    
    # Run  the test only if the options provided are valid.
    if options_obj.check_options(options):
        test_obj_mobile = PageFactory.get_page_object("Zero Mobile")

        #Setup and register a driver
        test_obj_mobile.register_driver(options.mobile_os_name,options.mobile_os_version,options.device_name,options.app_package,options.app_activity,options.remote_flag,options.device_flag,options.app_name,options.app_path)
        
        #Setup TestRail reporting
        if options.testrail_flag.lower()=='y':
            if options.test_run_id is None:
                test_obj_mobile.write('\033[91m'+"\n\nTestRail Integration Exception: It looks like you are trying to use TestRail Integration without providing test run id. \nPlease provide a valid test run id along with test run command using -R flag and try again. for eg: pytest -X Y -R 100\n"+'\033[0m')
                testrail_flag = 'N'   
            if options.test_run_id is not None:
                test_obj_mobile.register_testrail()
                test_obj_mobile.set_test_run_id(options.test_run_id)

        if options.tesults_flag.lower()=='y':
            test_obj_mobile.register_tesults()
        
        test_mobile_bitcoin_price(test_obj_mobile)
        
        #Teardown
        test_obj_mobile.wait(3)
        test_obj_mobile.teardown() 

    else:
        print('ERROR: Received incorrect comand line input arguments')
        print(options_obj.print_usage())
