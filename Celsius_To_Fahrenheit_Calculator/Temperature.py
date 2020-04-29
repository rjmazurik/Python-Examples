#!Temperature (Fahrenheit to celsius & celsius to fahrenheit)
import temperature_exceptions 

def FtoC(F : float):
    if F < -459.67:
        raise temperature_exceptions.TemperatureTooLowError
    else:
        celsius = (F - 32.0) * (5.0/9.0)
        return celsius
             
def CtoF(C : float):
    if C < -273.15:
        raise temperature_exceptions.TemperatureTooLowError
    else:
        fahrenheit = (C * (9.0/5.0)) + 32.0 
        return fahrenheit

def KtoF(K : float):
    if K < 0:
        raise temperature_exceptions.TemperatureTooLowError
    else:
        celsiusValue = K - 273.15
        return CtoF(celsiusValue)