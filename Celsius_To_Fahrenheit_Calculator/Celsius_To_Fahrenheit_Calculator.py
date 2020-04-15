#!Celsius_To_Fahrenheit_Calculator 

def FtoC(F : float):
    celsius = (F - 32.0) * (5.0/9.0)
    return celsius

def CtoF(C : float):
    fahrenheit = (C * (9.0/5.0)) + 32.0 
    return fahrenheit
    
def main(): 
    while True:  
        userInput = input('Convert (C)elsius or (F)ahrenheit? ')
        userInput = userInput.upper()
        convertType = userInput[0]
        if convertType == ('C'):
            try:
                celsiusInput = input('(celsius)value? ')
                fahrenheitOutput = CtoF(float(celsiusInput))
                print(str(round(fahrenheitOutput, 1)) + ' F')
            except KeyboardInterrupt:
                raise
            except:
                print("Input must be a number")
            
        elif convertType == ('F'):
            try:
                fahrenheitInput = input('(fahrenheit)value? ')
                celsiusOutput = FtoC(float(fahrenheitInput))
                print(str(round(celsiusOutput, 1)) + ' C')
            except KeyboardInterrupt:
                raise
            except:
                print("Input must be a number")
                
        elif convertType != ('C') or ('F'):
            print('Please choose either (C)elsius or (F)ahrenheit')
                          
if __name__ == '__main__': 
    try:
        main()
    except KeyboardInterrupt:
        print('\nok. bye!\n')
        exit()





