import logging
import sys
from src.logger import logging

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        self.error_message = error_message

        _, _, exc_tb = error_detail.exc_info()

        self.file_name = exc_tb.tb_frame.f_code.co_filename
        self.line_number = exc_tb.tb_lineno

    def __str__(self):
        return "Error occurred in python script [{0}] line number [{1}] error message [{2}]".format(
            self.file_name, self.line_number, str(self.error_message)
        )



# import sys
# def error_message_detail(error,error_detail:sys):
#     _,_,exc_tb=error_detail.exc_info()
#     file_name=exc_tb.tb_frame.f_code.co_filename
#     error_message="Error occured in Python script name [{0}] line number [{1}] and error message [{2}]".format(
#         file_name,exc_tb.tb_lineno,str(error)
#     )
#     return error_message


# class CustomExecption(Exception):
#     def __init__(self, error_message,error_detail:sys):
#         super().__init__(error_message)
#         self.error_message=error_message_detail(error_message,error_detail=error_detail)

#     def __str__(self):
#         return self.error_message




if __name__=="__main__":
    try:
        a=10/0
    except Exception as e:
        logging.info("Divide by 0 error")
        raise CustomException(e,sys)