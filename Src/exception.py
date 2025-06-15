import sys 
from logger import logging # Importing the logging module from logger.py
#custom exception handle 
def error_message_details(error, error_detail:sys):
    _,_,exc_tb=error_detail.exc_info() #exc_tb is the traceback object which tells us at what time and where the error occurred
    filename=exc_tb.tb_frame.f_code.co_filename #filename is the name of the file where the error occurre
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
         filename,exc_tb.tb_lineno, str(error)    
    )
    return error_message
    
class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message) #call the parent class constructor
        self.error_message= error_message_details(error_message, error_detail=error_detail)
    def __str__(self):
        return self.error_message
    
 