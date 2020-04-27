#census_tool
import csv
from census import Census

def main():
    census = Census() # instantiate object 
    while True:
        stateAcronym = input('State(default: OR) ? ').upper()
        if stateAcronym == "":
            stateAcronym = None
        while True:
            year = input('Year (2010-2019) ? ')
            if not census.ValidateYear(year):
                print("Invalid year")
                continue 
            else:
                break
        theSortedList = census.MetroByState( year, stateAcronym )
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
    


    