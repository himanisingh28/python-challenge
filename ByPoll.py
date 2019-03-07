import os
import csv

# Path to collect data from the CSV file in the folder
electionDataCSV = os.path.join('..', 'python-challenge', 'election_data.csv')


# Read in the CSV file
# Define the function and have it accept the 'electionDataCSV' as its sole parameter
    
with open(electionDataCSV, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    #Initializing variables, lists, dictionary
    totalVotes = 0
    voteList = []
    candDict = {}
    maxVotes = 0

#Loop through the data
    for row in csvreader:
        voteList.append(row[0])
        totalVotes = len(voteList)

        #Returns the corresponding value for the provided dictionary key  and increments counter by 1
        candDict[row[2]] = candDict.get(row[2],0) + 1

# Iterating through the dictionary to calculate vote percentage for each candidate
    for k,v in candDict.items():
        candDict[k]= round((v/totalVotes) * 100 , 2) 

    
    maxVotes = max(candDict, key=candDict.get)

    print ("Election Result")
    print ("---------------------------------")
    print (f"Total Votes: {totalVotes}")
    print ("----------------------------------")
    print ("{" + '\n'.join('{}:{}'.format(k, v) for k, v in candDict.items()) + "}")
    print ("----------------------------------")
    print(f"Winner: {maxVotes}: {candDict[maxVotes]}")


