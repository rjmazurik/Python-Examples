#census class
import csv

class Census():
    
    yearDict = {} # class data 
    
    def __init__(self): # ~ constructor 
        self.yearDict['2010'] = 8
        self.yearDict['2011'] = 9
        self.yearDict['2012'] = 10
        self.yearDict['2013'] = 11
        self.yearDict['2014'] = 12
        self.yearDict['2015'] = 13
        self.yearDict['2016'] = 14
        self.yearDict['2017'] = 15
        self.yearDict['2018'] = 16
        self.yearDict['2019'] = 17
        
    def MetroByState(self, state="OR", year="2019") -> dict: 
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
                    popIndex = self.yearDict[year]
                    population = (row[popIndex]) 
                    statesPopulationList[metro]=int(population) # add dict item by key (metro)
                
            return self._sortOutput(statesPopulationList) # sort the dict
    
    def ValidateYear(self, year="2019") -> bool: # see if year is in dict 
        if year in self.yearDict.keys():
            return True 
        else:
            return False 
        
    def _sortOutput(self, popList) -> dict: # internal sort dict 
        sortedList = sorted(dict(popList).items(), key=lambda x: x[1], reverse=True)
        return sortedList