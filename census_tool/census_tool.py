#census_tool
import csv
from census import Census

def main():
    census = Census() # instantiate object 
    while True:
        stateInput = input('State(default: OR) ? ').upper()
        yearInput = input('Year (default: 2019) ? ')
        if stateInput == '' and yearInput == '':
            theSortedList = census.MetroByState()
        elif stateInput == '' and yearInput != '':
            theSortedList = census.MetroByState(year=yearInput) # named parameter passing 
        elif stateInput != '' and yearInput == "":
                theSortedList = census.MetroByState(state=stateInput)     
        else: # both state and year were entered 
            theSortedList = census.MetroByState(stateInput, yearInput) # positional passing
                   
        i = 0
        for metro, pop in dict(theSortedList).items(): # output the dict 
            i = i + 1
            print(f'{metro} {pop:,}')
        print('\nTotal State Counties:', i)
    
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\nok. bye!\n')
        exit()
    


    