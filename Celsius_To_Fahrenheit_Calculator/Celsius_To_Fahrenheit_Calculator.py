#!Celsius_To_Fahrenheit_Calculator 

from Temperature import CtoF, FtoC, KtoF
import temperature_exceptions 

def main(): 
    while True:
        try:
            userInput = input('Convert (C)elsius, (F)ahrenheit, or (K)elvin? ')
            userInput = userInput.upper()
            convertType = userInput[0]
            if convertType == ('C'):
                while True:
                    try:
                        inputVal = float(input('(Celsius)value? '))
                        fahrenheitOutput = CtoF(inputVal)
                        print(str(round(fahrenheitOutput, 1)) + ' F')
                        break 
                    except temperature_exceptions.TemperatureTooLowError:
                        print('Temperature cannot be below absolute zero')
                    except ValueError:
                        print("Please enter a value for the temperature")
                        
            elif convertType == ('F'):
                while True:
                    try:
                        inputVal = float(input('(Fahrenheit)value? '))
                        celsiusOutput = FtoC(inputVal)
                        print(str(round(celsiusOutput, 1)) + ' C')
                        break 
                    except temperature_exceptions.TemperatureTooLowError:
                        print('Temperature cannot exceed absolute zero')
                    except ValueError: 
                       print("Please enter a value for the temperature")
                        
            elif convertType == ('K'):
                while True:
                    try:
                        inputVal = float(input('(Kelvin)value? '))
                        kelvinOutput = KtoF(inputVal)
                        print(str(round(kelvinOutput, 1)) + 'F')
                        break 
                    except temperature_exceptions.TemperatureTooLowError:
                        print('Temperature cannot exceed absolute zero')   
                    except ValueError: 
                        print("Please enter a value for the temperature")
        except IndexError:
            print('invalid input')
        except KeyboardInterrupt:
            raise
if __name__ == '__main__': 
    try:
        main()
    except KeyboardInterrupt:
        print('\nok. bye!\n')
        exit()
        





