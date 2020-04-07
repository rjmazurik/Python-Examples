#!rgb_led

import RPi.GPIO as GPIO

pins = {'red': 17, 'green': 18, 'blue': 27}

color_dict = {}


def setColor(hexString):
    hexColor = int(hexString, 16)
    R_val = (hexColor & 0xFF0000) >> 16
    G_val = (hexColor & 0x00FF00) >> 8
    B_val = (hexColor & 0x0000FF) >> 0
 # these three lines are used for analyzing the col variables 
 # assign the first two values of the hexadecimal to R, the middle two assigned to G
 # assign the last two values to B, please refer to the shift operation of the hexadecimal for details.

    # Map color value from 0~255 to 0~100
    R_val = MAP(R_val, 0, 255, 0, 100)
    G_val = MAP(G_val, 0, 255, 0, 100)
    B_val = MAP(B_val, 0, 255, 0, 100)
    
    # Change the colors
    p_R.ChangeDutyCycle(R_val)
    # Assign the mapped duty cycle value to the corresponding PWM channel to change the luminance. 
    p_G.ChangeDutyCycle(G_val)
    p_B.ChangeDutyCycle(B_val)
    
def setup():
    global p_R, p_G, p_B
    # Set the GPIO modes to BCM Numbering
    GPIO.setmode(GPIO.BCM)
    # Set all LedPin's mode to output and initial level to High(3.3v)
    for i in pins:
        GPIO.setup(pins[i], GPIO.OUT, initial=GPIO.HIGH)

    # Set all led as pwm channel and frequece to 2KHz
    p_R = GPIO.PWM(pins['red'], 2000)
    p_G = GPIO.PWM(pins['green'], 2000)
    p_B = GPIO.PWM(pins['blue'], 2000)

    # Set all begin with value 0
    p_R.start(0)
    p_G.start(0)
    p_B.start(0)

    color_dict["BLACK"]="0x000000"
    color_dict["WHITE"]="0xFFFFFF"
    color_dict["RED"]="0xFF0000"
    color_dict["LIME"]="0x00FF00"
    color_dict["BLUE"]="0x0000FF"
    color_dict["YELLOW"]="0xFFFF00"
    color_dict["CYAN"]="0x00FFFF"
    color_dict["MAGENTA"]="0xFF00FF"
    color_dict["SILVER"]="0xC0C0C0"
    color_dict["GRAY"]="0x808080"
    color_dict["MAROON"]="0x800000"
    color_dict["OLIVE"]="0x808000"
    color_dict["GREEN"]="0x008000"
    color_dict["PURPLE"]="0x800080"
    color_dict["TEAL"]="0x008080"
    color_dict["NAVY"]="0x000080"


# Define a MAP function for mapping values.  Like from 0~255 to 0~100
def MAP(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


def destroy():
    # Stop all pwm channel
    p_R.stop()
    p_G.stop()
    p_B.stop()
    # Release resource
    GPIO.cleanup()

def main(): 
    while True:  
        userInput = raw_input('What color? ')
        userInput = userInput.upper()
        hexValue = color_dict.get(userInput, "notfound" )
        if hexValue == "notfound": 
            print('\nbad color')
        else:
            setColor(hexValue)
                 
if __name__ == '__main__':          # todo: is this the entry point to the program? thesis: yes it is 
    setup()
    try:
        main()
    except KeyboardInterrupt:		# When 'Ctrl+C' is pressed, the program destroy() will be  executed.
        destroy()
        print('\nok. bye!\n')
        exit()