#census_tool
import csv

# sort by population numeric value 
def sortOutput(popList):
    sortedList = sorted(dict(popList).items(), key=lambda x: x[1], reverse=True)
    return sortedList

def ReadInMetroPopulationByState(state):
    with open('US-Census-Metro-Data.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, dialect='excel', delimiter=',')
        next(reader, None)                      # skip the header line 
        statesPopulationList = {}               # dict init 
        for row in reader: 
            metroAreas = (row[4])
            splitMetro = metroAreas.split(',')
            metro = splitMetro[0]
            stateAbbreviation = splitMetro[1].strip() # remove leading and trailing spaces
            if state == stateAbbreviation:
                population = (row[17]) 
                statesPopulationList[metro]=int(population) # add dict item by key (metro)
                
        return sortOutput(statesPopulationList) # sort the dict
        
def main():
    while True:
        stateAcronym = input('State(ex. AZ) ? ').upper()
        theSortedList = ReadInMetroPopulationByState( stateAcronym )
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
    


    