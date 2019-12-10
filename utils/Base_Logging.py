"""
Qxf2 Services: A plug-n-play class for logging.
This class wraps around Python's loguru module.
"""
import os, inspect
import datetime
import sys
from loguru import logger

class Base_Logging():
    "A plug-n-play class for logging"
    def __init__(self,log_file_name=None,level="DEBUG",format="{time} - {level} - {message}"):
        "Constructor for the logging class"
        self.log_file_name=log_file_name
        self.log_file_dir = os.path.abspath(os.path.join(os.path.dirname(__file__),'..','log'))
        self.level=level
        self.format=format
        self.log = self.set_log(self.log_file_name,self.level,self.format) 
        
        
    def set_log(self,log_file_name,level,format,test_module_name=None):
        "Add an handler sending log messages to a sink"
        if test_module_name is None:
            test_module_name = self.get_calling_module()              
        if not os.path.exists(self.log_file_dir):
            os.makedirs(self.log_file_dir)
        if log_file_name is None:
            log_file_name = self.log_file_dir + os.sep + test_module_name + '.log'
        else:
            log_file_name = self.log_file_dir + os.sep + log_file_name
        
        logger.add(log_file_name,level=level,format=format, 
        rotation="30 days", filter=None, colorize=None, serialize=False, backtrace=True, enqueue=False, catch=True)


    def get_calling_module(self):
        "Get the name of the calling module"        
        calling_file = inspect.stack()[-1][1]                  
        if 'runpy' in calling_file:
            calling_file = inspect.stack()[4][1]
            all_stack_frames = inspect.stack()
            caller_stack_frame = all_stack_frames[1]
            caller_name = caller_stack_frame[3]
            print("This is from Base_Loggin and my caller method name is", caller_name)
        calling_filename = calling_file.split(os.sep)

        #This logic bought to you by windows + cygwin + git bash 
        if len(calling_filename) == 1: #Needed for 
            calling_filename = calling_file.split('/')
        
        self.calling_module = calling_filename[-1].split('.')[0]

        return self.calling_module
    
    
    def write(self,msg,level='info'):
        "Write out a message"
        fname = inspect.stack()[2][3] #May be use a entry-exit decorator instead    
        f1name = inspect.stack()[3][1] 
        all_stack_frames = inspect.stack()
        caller_stack_frame = all_stack_frames[3]
        caller_name = caller_stack_frame[3]   
        d = {'caller_func': fname}      
        df =  {'caller_func': caller_name}                 
        if level.lower()== 'debug': 
            logger.debug("{module}|{name} | {msg} ",module=d['caller_func'],msg=msg, name=df['caller_func'])                      
        elif level.lower()== 'info':
            logger.info("{module} |{name} | {msg}",module=d['caller_func'],msg=msg, name=df['caller_func'])             
        elif level.lower()== 'warn' or level.lower()=='warning':           
            logger.warning("{module} |{name} | {msg}",module=d['caller_func'],msg=msg, name=df['caller_func'])    
        elif level.lower()== 'error':
            logger.error("{module} |{name} | {msg}",module=d['caller_func'],msg=msg, name=df['caller_func'])              
        elif level.lower()== 'critical':   
            logger.critical("{module} |{name} | {msg}",module=d['caller_func'],msg=msg, name=df['caller_func'])                
        else:
            logger.critical("Unknown level passed for the msg: {}", msg)