#!Celsius_To_Fahrenheit_Calculator 

from Temperature import CtoF, FtoC, KtoF
import temperature_exceptions 

def convertTemperature(prompt:str, convertFunction, outputTempLabelChar  ):
    while True:
        try:
            inputVal = float(input(prompt + ' '))
            tempOutput = convertFunction(inputVal)
            print(str(round(tempOutput, 1)) + ' ' + outputTempLabelChar  )
            break 
        except temperature_exceptions.TemperatureTooLowError as exc:
            print(f'{exc.Message}, limit: {exc.TempLowBoundValue}')
        except ValueError:
            print("Please enter a numeric value for the temperature")

def main(): 
    INVALID_INPUT_MSG = 'Invalid conversion type. Try F, C or K'
    while True:
        try:
            userInput = input('Convert (C)elsius, (F)ahrenheit, or (K)elvin? ')
            userInput = userInput.upper()
            convertType = userInput[0]
            if convertType == ('C'):
                convertTemperature('(Celsius)value?', CtoF, 'F'  )    
            elif convertType == ('F'):
                convertTemperature('(Fahrenheit)value?', FtoC, 'C'  )   
            elif convertType == ('K'):
                convertTemperature('(Kelvin)value?', KtoF, 'K'  ) 
            else:
                print(INVALID_INPUT_MSG)
        except IndexError:
            print(INVALID_INPUT_MSG)
        
        
if __name__ == '__main__': 
    try:
        main()
    except KeyboardInterrupt:
        print('\nok. bye!\n')
        exit()
        





