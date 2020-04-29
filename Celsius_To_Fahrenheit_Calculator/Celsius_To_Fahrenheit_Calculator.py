#!Celsius_To_Fahrenheit_Calculator 

from Temperature import CtoF, FtoC, KtoF
import temperature_exceptions 

def getNumericTemperature(promptString):
    while True:
        try:
            inputVal = input('(' + promptString + ')value? ')
            return float(inputVal)
        except KeyboardInterrupt:
            raise
        except:
            print("Input must be a float")
def main(): 
    while True:  
        userInput = input('Convert (C)elsius, (F)ahrenheit, or (K)elvin? ')
        userInput = userInput.upper()
        convertType = userInput[0]
        try:
            if convertType == ('C'):
                celsius = getNumericTemperature('celsius')
                fahrenheitOutput = CtoF(celsius)
                print(str(round(fahrenheitOutput, 1)) + ' F')
            elif convertType == ('F'):
                fahrenheit = getNumericTemperature('fahrenheit')
                celsiusOutput = FtoC(fahrenheit)
                print(str(round(celsiusOutput, 1)) + ' C')   
            elif convertType == ('K'):
                kelvin = getNumericTemperature('kelvin')
                kelvinOutput = KtoF(kelvin)
                print(str(round(kelvinOutput, 1)) + 'F')         
            else:
                print('Please choose either (C)elsius or (F)ahrenheit')
        except temperature_exceptions.TemperatureTooLowError:
            print('Temperature cannot exceed absolute zero')
        
if __name__ == '__main__': 
    try:
        main()
    except KeyboardInterrupt:
        print('\nok. bye!\n')
        exit()
    except: 
        print('Exception occured please restart program')
        





