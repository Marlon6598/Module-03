import os
import csv # imports file-handling funcions

csvFilePath = os.path.join('Resources','election_data.csv') # Specifies directory of .csv file

candidateList = []
candidate = []
voteCount = []
votePercent = []
count = 0

with open(csvFilePath, "r", encoding="utf-8") as csvFile: # opens the file and saves it as an object named csvFile
    csvReader = csv.reader(csvFile, delimiter=",") # specifies the object name and delimiter for the reader in the open() function
    header = next(csvReader) # reads the row of headers and skips over this row for our data

    for row in csvReader:
        count += 1 # Counts the total number of votes
        candidateList.append(row[2]) # appends the candidate names to candidateList
    
    for name in set(candidateList):
        candidate.append(name) # obtains unique candidate names from list candidateList

        voteTotal = candidateList.count(name) # voteTotal is the total number of votes per candidate
        voteCount.append(voteTotal)

        percentTotal = (voteTotal/count)*100 # finds the percent of total votes per candidate
        votePercent.append(percentTotal)
        
    winningCount = max(voteCount)
    winner = candidate[voteCount.index(winningCount)]
 
    print(" ")
    print("Election Results")
    print("-------------------------")
    print("Total Votes :" + str(count))
    print("-------------------------")
    for i in range(len(candidate)):
        print(candidate[i] + ": " + str(votePercent[i]) +"% (" + str(voteCount[i])+ ")")
    print("-------------------------")
    print("Winner: " + winner)
    print("-------------------------")

with open(os.path.join('analysis','election_analysis.txt'), "w") as txt:
    txt.write("Election Results\n")
    txt.write("-------------------------\n")
    txt.write("Total Vote: " + str(count) + "\n")
    txt.write("-------------------------\n")
    for i in range(len(set(candidate))):
        txt.write(candidate[i] + ": " + str(votePercent[i]) +"% (" + str(voteCount[i]) + ")\n")
    txt.write("-------------------------\n")
    txt.write("Winner: " + winner + "\n")
    txt.write("-------------------------")