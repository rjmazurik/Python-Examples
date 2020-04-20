import subprocess

def main():
    while True:
        userInput = input('rsh> ')
        if userInput == 'exit':
            break
        try:
            x = eval(userInput)
            if x: print(x)
        except:
            try:
                exec(userInput)
            except Exception as error:
                print('error:', error)
        

        










if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()