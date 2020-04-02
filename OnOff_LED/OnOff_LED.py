#!OnOff_LED
import RPi.GPIO as GPIO         # todo: what is this library?
import string

def init():
    GPIO.setmode(GPIO.BCM)      # Set the GPIO modes to BCM Numbering                            
    setLED(0)

def setLED(x):
    LedPin = 17                 # Make sure the LED is on this pin on breadboard 
    if x == 0:
        GPIO.setup(LedPin, GPIO.OUT, initial=GPIO.LOW)     # Set pin 17 off (no voltage)
    else:
        GPIO.setup(LedPin, GPIO.OUT, initial=GPIO.HIGH)

def destroy():    
    setLED(0)  # Turn off LED
    GPIO.cleanup()  # Release resource         

def main():
    while True:  
        userInput = input('What? ').upper()
        if userInput == "ON":
            setLED(1)
        elif userInput == "OFF":
            setLED(0)
        else:
            print('WTF!')

if __name__ == '__main__':          # todo: is this the entry point to the program? thesis: yes it is 
    init()
    try:
        main()
    except KeyboardInterrupt:       # When 'Ctrl+C' is pressed, the program destroy() will be  executed.
        destroy()
        print('\nok. bye!\n')
        exit()