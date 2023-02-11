import os
import csv # imports file-handling funcions

csvFilePath = os.path.join('Resources', 'budget_data.csv') # Specifies directory of .csv file

monthlyChange = [] # list to hold the difference between each pair of dates
date = [] # list to hold dates

totalMonths = 0
totalProfits = 0
profitsChange = 0
firstProfit = 0
count = 0

with open(csvFilePath, "r", encoding="utf-8") as csvFile: # opens the file and saves it as an object named csvFile
    csvReader = csv.reader(csvFile, delimiter=",") # specifies the object name and delimiter for the reader in the open() function
    header = next(csvReader) # reads the row of headers and skips over this row for our data

    for row in csvReader:
        count += 1
        date.append(row[0]) # the rows in the dates column is appended to date

        revenue = int(row[1])
        totalMonths += 1 # the total months is the total count of each row sans the header
        totalProfits = totalProfits + int(row[1]) # the total profit is the summation of all rows sans the header

        monthlyChangeProfits = revenue - firstProfit
        
        monthlyChange.append(monthlyChangeProfits) # stores monthly changes in a list

        profitsChange = profitsChange + monthlyChangeProfits
        firstProfit = revenue

        #change = (int(row[1], 2)) - (int(row[1], 1))
        #average = (change)-(totalMonths - 1)
        average = (profitsChange/totalMonths - 1)

        grIncrease = max(monthlyChange)
        grDecrease = min(monthlyChange)

        increaseDate = date[monthlyChange.index(grIncrease)]
        decreaseDate = date[monthlyChange.index(grDecrease)]

    print(" ")
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {totalMonths}")
    print(f"Total: ${totalProfits}")
    print(f"Average Change: $" + str(int(average)))
    print(f"Greatest Increase in Profits: " + str(increaseDate) + " ($" + str(grIncrease) + ")")
    print(f"Greatest Decrease in Profits: "+ str(decreaseDate) + " ($" + str(grDecrease)+ ")")

with open(os.path.join('analysis','financial_analysis.txt'), "w") as txt:
    txt.write("Financial Analysis"+ "\n")
    txt.write("----------------------------\n")
    txt.write(f"Total Months: {totalMonths}\n")
    txt.write("Total Profits: " + "$" + str(totalProfits) +"\n")
    txt.write("Average Change: $" + str(int(average)) + "\n")
    txt.write("Greatest Increase in Profits: " + str(increaseDate) + " ($" + str(grIncrease) + ")\n")
    txt.write("Greatest Decrease in Profits: " + str(decreaseDate) + " ($" + str(grDecrease) + ")")