import os
import csv
import numpy as np

# Set path for file
csvpath = "Solution/Resources/election_data.csv"

votes = 0
poll_dict = {"Charles Casper Stockham" : 0, 
            "Diana DeGette" : 0, 
            "Raymon Anthony Doane" : 0}

# Open the CSV
with open(csvpath, encoding='utf') as csvfile:
   
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    
    # Loop through csv to get vote total and votes per candidate
    for row in csvreader: 
        votes += 1
        candidate = row[2]
        poll_dict[candidate] += 1

# print out election results
print()
print("Election Results")
print("----------------------------------------")
print(f"Total Votes: {votes}")
print("----------------------------------------")
for x in poll_dict : 
    percent = 100 * poll_dict[x] / votes
    percent = round (percent, 3)
    print(f"{x}: {percent}% ({poll_dict[x]})")

winner = max(poll_dict, key=poll_dict.get)
print("----------------------------------------")
print(f"Winner: {winner}")

# print out election results to txt file
with open ("poll_results.text", "w") as f:
    f.write("\n")
    f.write("Election Results\n")
    f.write("----------------------------------------\n")
    f.write(f"Total Votes: {votes}\n")
    f.write("----------------------------------------\n")
    for x in poll_dict : 
        percent = 100 * poll_dict[x] / votes
        percent = round (percent, 3)
        f.write(f"{x}: {percent}% ({poll_dict[x]})\n")

    winner = max(poll_dict, key=poll_dict.get)
    f.write("----------------------------------------\n")
    f.write(f"Winner: {winner}\n")
    f.write("\n")
    