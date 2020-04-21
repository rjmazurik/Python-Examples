#!Temperature (Fahrenheit to celsius & celsius to fahrenheit)

def FtoC(F : float):
    celsius = (F - 32.0) * (5.0/9.0)
    return celsius

def CtoF(C : float):
    fahrenheit = (C * (9.0/5.0)) + 32.0 
    return fahrenheit

def KtoF(kelvinValue):
    celsiusValue = kelvinValue - 273.15
    return CtoF(celsiusValue)