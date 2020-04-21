import subprocess

def parseInput(inputString:str):
    inputString = inputString.lower()       #lower case it all
    inputArray = inputString.split()        # break line by white space into inputs[] array

    cmdstring = inputArray[0]               # grab the first chars:   (t)empcalc command
    cmd = cmdstring[0]                      # pluck of the first char

    conversionType = None
    temperatureValue = None
    if len(inputArray) > 1 :
        conversionTypeString = inputArray[1]   # grab the 2nd string
        conversionType = conversionTypeString[0] # and the 1st char
    if len(inputArray) > 2 :
        temperatureValue = inputArray[2]       # grab the 3rd string 
    return cmd, conversionType, temperatureValue  # return 3 values from a function

def main():
    print('type exit to leave')
    while True:
        userInput = input('rsh> ')
        if userInput == '' : continue                    # handle no input  case
        cmd, convType, tempValue = parseInput(userInput) # separate the command line
        if cmd == 'e':
            break
        elif cmd == 't': #tempcalc command 
            commandline = f'python ./tempcalc.py {convType} {tempValue}'
            output = subprocess.getoutput(commandline) # getoutput() does the shell out
            print(output)
        elif cmd == 'f': # files command 
            commandline = f'ls -al'
            output = subprocess.getoutput(commandline) # getoutput() does the shell out
            print(output)
            
        
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()