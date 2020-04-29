#!Celsius_To_Fahrenheit_Calculator 

from Temperature import CtoF, FtoC, KtoF
import temperature_exceptions 

def main(): 
    while True:
        try:
            userInput = input('Convert (C)elsius, (F)ahrenheit, or (K)elvin? ')
            userInput = userInput.upper()
            convertType = userInput[0]
        except IndexError:
            pass
        try:
            if convertType == ('C'):
                while True:
                    try:
                        inputVal = float(input('(Celsius)value? '))
                    except ValueError:
                        pass
                    try:
                        if inputVal < -273.15:
                            raise temperature_exceptions.TemperatureTooLowError
                        fahrenheitOutput = CtoF(inputVal)
                        print(str(round(fahrenheitOutput, 1)) + ' F')
                        break 
                    except temperature_exceptions.TemperatureTooLowError:
                        print('Temperature cannot exceed absolute zero')
                        pass
                    except: 
                        print('Please input a temperature')
                        pass  
            elif convertType == ('F'):
                while True:
                    try:
                        inputVal = float(input('(Fahrenheit)value? '))
                    except ValueError:
                        pass
                    try:
                        if inputVal < -459.67:
                            raise temperature_exceptions.TemperatureTooLowError
                        celsiusOutput = FtoC(inputVal)
                        print(str(round(celsiusOutput, 1)) + ' C')
                        break 
                    except temperature_exceptions.TemperatureTooLowError:
                        print('Temperature cannot exceed absolute zero')
                        pass  
                    except: 
                        print('Please input a temperature')
                        pass
            elif convertType == ('K'):
                while True:
                    try:
                        inputVal = float(input('(Kelvin)value? '))
                    except ValueError:
                        pass
                    try:
                        if inputVal < 0:
                            raise temperature_exceptions.TemperatureTooLowError
                        kelvinOutput = KtoF(inputVal)
                        print(str(round(kelvinOutput, 1)) + 'F')
                        break 
                    except temperature_exceptions.TemperatureTooLowError:
                        print('Temperature cannot exceed absolute zero')
                        pass    
                    except: 
                        print('Please input a temperature')
                        pass
            else:
                print('Please choose either (C)elsius, (F)ahrenheit, or (K)elvin')
        except:
            pass
        
if __name__ == '__main__': 
    try:
        main()
    except KeyboardInterrupt:
        print('\nok. bye!\n')
        exit()
        





