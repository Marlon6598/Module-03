import os
import csv # imports file-handling funcions

csvFilePath = os.path.join('Resources', 'budget_data.csv') # Specifies directory of .csv file

with open(csvFilePath, "r", encoding="utf-8") as csvFile: # opens the file and saves it as an object named csvFile
    csvReader = csv.reader(csvFile, delimiter=",") #specifies the object name and delimiter for the reader in the open() function
    header = next(csvReader) # reads the row of headers and skips over this row for our data
    
    totalMonths = len(list(csvReader)) # the total months is the length of the dataset minus the header

profits = [] # creates an empty variable to contain the data from the profits & losses column in the csv file
for row in csvReader:
        profits.append(row[1])




print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {totalMonths}")
print(f"Total: ${[]}")
print(f"Average Change: ")
print(f"Greatest increase in Profits: ")
print(f"Greatest Decrease in Profits: ")