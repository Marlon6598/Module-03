import os
import csv # imports file-handling funcions

csvFilePath = os.path.join('Resources', 'budget_data.csv') # Specifies directory of .csv file

with open(csvFilePath, "r", encoding="utf-8") as csvFile: # opens the file and saves it as an object named csvFile
    csvReader = csv.reader(csvFile, delimiter=",") #specifies the object name and delimiter for the reader in the open() function
    header = next(csvReader) # reads the row of headers and skips over this row for our data
    firstRow = next(csvReader)
    totalMonths = len(list(csvReader)) # the total months is the length of the dataset minus the header
    prevChange = int(firstRow[1])

    # dates = [] # creates an empty variable to contain the data from the date column in the csv file
    profits = [1] # creates an empty variable to contain the data from the profits/losses column in the csv file
    rowCount = 0

    for row in csvReader:
        change = int(row[1]) - prevChange
        profits.append(change)
        prevChange = int(row[1])
        rowCount = rowCount + 1

average = sum(profits)/(len(profits))




print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {totalMonths}")
print(f"Total: ${[]}")
print(f"Average Change: {average}")
print(f"Greatest increase in Profits: ")
print(f"Greatest Decrease in Profits: ")