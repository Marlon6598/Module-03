import os
import csv # imports file-handling funcions

csvFilePath = os.path.join('Resources', 'budget_data.csv') # Specifies directory of .csv file

with open(csvFilePath, "r", encoding="utf-8") as csvFile: # opens the file and saves it as an object named csvFile
    csvReader = csv.reader(csvFile, delimiter=",") # specifies the object name and delimiter for the reader in the open() function
    header = next(csvReader) # reads the row of headers and skips over this row for our data

    total = 0
    totalMonths = 0

    for row in csvReader:
        revenue = int(row[1])
        totalMonths += 1 # the total months is the total count of each row sans the header
        total = total + revenue # the total profit is the summation of all rows sans the header




print(" ")
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {totalMonths}")
print(f"Total: ${total}")
print(f"Average Change: ")
print(f"Greatest increase in Profits: ")
print(f"Greatest Decrease in Profits: ")