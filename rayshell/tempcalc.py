#!Celsius_To_Fahrenheit_Calculator 
import sys
from Temperature import CtoF, FtoC, KtoF
            
def main(): 
    convertType = sys.argv[1]
    valueString = sys.argv[2]
    value = float(valueString)
    if convertType == ('c'):
        fahrenheitOutput = CtoF(value)
        print(str(round(fahrenheitOutput, 1)) + ' F')
    elif convertType == ('f'):
        celsiusOutput = FtoC(value)
        print(str(round(celsiusOutput, 1)) + ' C')   
    elif convertType == ('k'):
        kelvinOutput = KtoF(value)
        print(str(round(kelvinOutput, 1)) + 'F')         
    else:
        print('Please choose either (C)elsius or (F)ahrenheit')
                          
if __name__ == '__main__': 
    try:
        main()
    except KeyboardInterrupt:
        print('\nok. bye!\n')
        exit()
    except:
        print('Exception encountered. Restart program and try again.')
        exit()





