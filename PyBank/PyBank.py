import os
import csv # imports file-handling funcions

csvFilePath = os.path.join('Resources', 'budget_data.csv') # Specifies directory of .csv file

profit = []
monthly_changes = []
date = []

totalProfits = 0
totalMonths = 0
currentChange = 0

with open(csvFilePath, "r", encoding="utf-8") as csvFile: # opens the file and saves it as an object named csvFile
    csvReader = csv.reader(csvFile, delimiter=",") # specifies the object name and delimiter for the reader in the open() function
    header = next(csvReader) # reads the row of headers and skips over this row for our data

    for i, row in enumerate(csvReader): # 
        revenue = int(row[1])
        totalMonths += 1 # the total months is the total count of each row sans the header
        totalProfits = totalProfits + revenue # the total profit is the summation of all rows sans the header




# average change = second row minus first row, repeat. Then divide by totalMonths -1 because we only did 85 calculations




print(" ")
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {totalMonths}")
print(f"Total: ${totalProfits}")
print(f"Average Change: ")
print(f"Greatest Increase in Profits: ")
print(f"Greatest Decrease in Profits: ")