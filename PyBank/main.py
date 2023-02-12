import os
import csv # imports file-handling funcions

csvFilePath = os.path.join('Resources', 'budget_data.csv') # Specifies directory of .csv file

monthlyChange = [] # list to hold the difference between each pair of dates
profits = [] # list to hold all the profits and losses in order to calculate the average change
date = [] # list to hold all the dates in the dataset
totalProfits = 0
profitsChange = 0
firstProfit = 0
count = 0

firstNumber = 0 # first variable to calculate average change
secondNumber = 1 # second variable to calculate average change
difference = 0 # variable to contain the difference between two months of profits / losses
averageChange = 0 # variable to contain the total of all differences between months divided by the length of the dataset minus one

with open(csvFilePath, "r", encoding="utf-8") as csvFile: # opens the file and saves it as an object named csvFile
    csvReader = csv.reader(csvFile, delimiter=",") # specifies the object name and delimiter for the reader in the open() function
    header = next(csvReader) # reads the row of headers and skips over this row for our data

    for row in csvReader:
        count += 1 # scans row-by-row through the dataset
        date.append(row[0]) # appends the rows in the dates column to date
        profits.append(float(row[1]))

        revenue = int(row[1]) # revenue is the integer in the profits/losses column
        totalProfits = totalProfits + int(row[1]) # the total profit is the summation of all rows sans the header

        monthlyChangeProfits = revenue - firstProfit
        monthlyChange.append(monthlyChangeProfits) # stores monthly changes in a list

        profitsChange = profitsChange + monthlyChangeProfits
        firstProfit = revenue

        grIncrease = max(monthlyChange)
        grDecrease = min(monthlyChange)

        increaseDate = date[monthlyChange.index(grIncrease)] 
        decreaseDate = date[monthlyChange.index(grDecrease)] # increaseDate & decreaseDate are the dates that share the same index as the max & min value of monthlyChange

    for i in profits: # for loop that will calculate the average change
        if secondNumber == len(profits):
            secondNumber = len(profits) - 1 # this if statement prevents "list index out of range" error from occurring

        difference = profits[secondNumber] - profits[firstNumber]
        averageChange = averageChange + difference
        firstNumber += 1
        secondNumber += 1

    averageChange = averageChange / (len(profits) - 1) # the average change is the total of the averages divided by the number of rows minus one

    print(" ")
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {count}")
    print(f"Total: ${totalProfits}")
    print("Average Change: $" + str(round(averageChange, 2)))
    print(f"Greatest Increase in Profits: " + str(increaseDate) + " ($" + str(grIncrease) + ")")
    print(f"Greatest Decrease in Profits: "+ str(decreaseDate) + " ($" + str(grDecrease)+ ")")

with open(os.path.join('analysis','financial_analysis.txt'), "w") as txt: # exports data into a text document in the "analysis" folder
    txt.write("Financial Analysis"+ "\n")
    txt.write("----------------------------\n")
    txt.write(f"Total Months: {count}\n")
    txt.write("Total Profits: " + "$" + str(totalProfits) +"\n")
    txt.write("Average Change: $" + str(round(averageChange, 2)) + "\n")
    txt.write("Greatest Increase in Profits: " + str(increaseDate) + " ($" + str(grIncrease) + ")\n")
    txt.write("Greatest Decrease in Profits: " + str(decreaseDate) + " ($" + str(grDecrease) + ")")