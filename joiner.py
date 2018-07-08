import csv

# Simple method to grab data from file for given player
def grabData(name, file):
    with open(file) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for i, row in enumerate(readCSV):
            ''' Row is a python list, where each time in loop it gets a full row of data
             then we access column by ith element, so 0 is the first element in the sheet
             so access with [0]. If we wanted, say, Losses, we could use print(row[4])
             to access that column '''
            if(row[0] == name):
                return row
    csvfile.close()


# Aaron Nola
fileOneData = grabData("Aaron Nola", "source1.csv")
fileTwoData = grabData("Aaron Nola", "source2.csv")

print(fileOneData)
print(fileTwoData)

# Example of doing our 'join' -  data for player from sheet one and two
print("Joined data for Aaron Nola: " + "wins - " + fileOneData[2] + " ERA - " + fileTwoData[4])
