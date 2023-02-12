import os
import csv # imports file-handling funcions

csvFilePath = os.path.join('Resources','election_data.csv') # Specifies directory of .csv file

candidateList = [] # list to hold all the instances of candidate names from the dataset
candidate = [] # list to hold the truncated list of candidate names
totalVote = [] # list to hold the total votes from each
votePercent = [] # list to hold the percent of total votes per candidate
count = 0 

with open(csvFilePath, "r", encoding="utf-8") as csvFile: # opens the file and saves it as an object named csvFile
    csvReader = csv.reader(csvFile, delimiter=",") # specifies the object name and delimiter for the reader in the open() function
    header = next(csvReader) # reads the row of headers and skips over this row for our data

    for row in csvReader:
        count += 1 # scans row-by-row through the dataset
        candidateList.append(row[2]) # appends the candidate names to candidateList
    
    for name in set(candidateList):
        candidate.append(name) # obtains unique candidate names from the candidateList list and populates the candidate list

        voteTotal = candidateList.count(name) # the total number of votes per candidate is the voteTotal
        totalVote.append(voteTotal)

        percentTotal = (voteTotal/count)*100 # finds the percent of total votes per candidate
        votePercent.append(percentTotal)
        votePercentRounded = [ round(i, 3) for i in votePercent]
        
    winningCount = max(totalVote) # the maximum totalVote value is the winningCount
    winner = candidate[totalVote.index(winningCount)] # the winner is the candidate associated with the winning totalVote
 
    print(" ")
    print("Election Results")
    print("-------------------------")
    print("Total Votes :" + str(count))
    print("-------------------------")
    for i in range(len(candidate)):
        print(candidate[i] + ": " + str(votePercentRounded[i]) +"% (" + str(totalVote[i])+ ")")
    print("-------------------------")
    print("Winner: " + winner)
    print("-------------------------")

with open(os.path.join('analysis','election_analysis.txt'), "w") as txt: # exports data into a text document in the "analysis" folder
    txt.write("Election Results\n")
    txt.write("-------------------------\n")
    txt.write("Total Vote: " + str(count) + "\n")
    txt.write("-------------------------\n")
    for i in range(len(set(candidate))):
        txt.write(candidate[i] + ": " + str(votePercentRounded[i]) +"% (" + str(totalVote[i]) + ")\n")
    txt.write("-------------------------\n")
    txt.write("Winner: " + winner + "\n")
    txt.write("-------------------------")