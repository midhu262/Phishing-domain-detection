from os import path
from application_logging import logger
from Training_Raw_Data_Validation.rawValidation import raw_data_validation



class train_validation:
   
    """
    
    This class does all the raw data validation of training data.
    
    """    
    
    def __init__(self):
        self.raw_data = raw_data_validation()
        self.log_writer = logger.App_Logger()
        self.file_object = open("Training_Logs/TrainingFile_Validation.txt", 'a+')
           
    def training_validation(self):
        # The start of file validation
        self.log_writer.log(self.file_object, 'Start of File Validation')
        try:
           pass
        
        except Exception:
            # logging the unsuccessful Training
            self.log_writer.log(self.file_object, 'Unsuccessful End of Training')
            self.file_object.close()
            raise Exception      
        
        
obj = train_validation()
obj.training_validation()