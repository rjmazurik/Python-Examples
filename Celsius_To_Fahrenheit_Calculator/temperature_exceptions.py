# Temperature Exceptions
import Temperature

class TemperatureTooLowError(Exception):
    def __init__(self, *args):
        if args:
            self.Message = args[0]
            self.TempLowBoundValue = args[1]
            
    def __str__(self):
        if True:
            return str(self.TempLowBoundValue)
    
        

        
        
        




    