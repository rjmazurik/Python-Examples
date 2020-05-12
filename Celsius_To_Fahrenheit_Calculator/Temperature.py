#!Temperature (Fahrenheit to celsius & celsius to fahrenheit)
import temperature_exceptions 

LOWER_FAHRENHEIT_BOUND = -459.67
LOWER_CELSIUS_BOUND = -273.15
LOWER_KELVIN_BOUND = 0

def FtoC(F : float):
        if F < LOWER_FAHRENHEIT_BOUND:
                raise temperature_exceptions.TemperatureTooLowError('Fahrenheit temp too low', LOWER_FAHRENHEIT_BOUND)
        celsius = (F - 32.0) * (5.0/9.0)
        return celsius
             
def CtoF(C : float):
        if C < LOWER_CELSIUS_BOUND:
                raise temperature_exceptions.TemperatureTooLowError('Celsius temp too low', LOWER_CELSIUS_BOUND)
        fahrenheit = (C * (9.0/5.0)) + 32.0 
        return fahrenheit

def KtoF(K : float):
        if K < LOWER_KELVIN_BOUND:
                raise temperature_exceptions.TemperatureTooLowError('Kelvin temp too low', LOWER_KELVIN_BOUND)
        celsiusValue = K - 273.15
        return CtoF(celsiusValue)