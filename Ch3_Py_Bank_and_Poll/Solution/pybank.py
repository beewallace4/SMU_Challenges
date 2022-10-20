import os
import csv
import numpy as np

# Set path for file
csvpath = "Solution/Resources/budget_data.csv"

months = 0
total = 0
change = 0
tot_change = 0
bank_list = []
index = 0
max_inc = -np.inf
date_inc = ""
date_dec = ""
max_dec = np.inf


# Open the CSV
with open(csvpath, encoding='utf') as csvfile:
   
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    
    # Loop through csv and create list of lists
    for row in csvreader: 
        bank_list.append(row)
        
    #print(bank_list)

for lists in bank_list :
    
    #total months
    months += 1

    #find overall total
    total += int(bank_list[index][1])
    
    #find total change
    if (index > 0) :
        change = int(bank_list[index][1]) - int(bank_list[index - 1][1])
        tot_change += change

    #find greatest increase
    if (change > max_inc) :
        max_inc = change
        date_inc = bank_list[index][0]

    #find greatest decrease
    elif (change < max_dec) :
        max_dec = change
        date_dec = bank_list[index][0]

    #set values for next iteration
    index += 1
    change = 0
    
avg_change = tot_change / (months - 1)
avg_change = round (avg_change, 2)

#print out terminal results
print()
print("Financial Analysis")
print("-------------------")
print(f"Total Months: {months}")
print(f"Total: ${total}")
print(f"Average Change: ${avg_change}")
print(f"Greatest Increase in Profits: {date_inc} (${max_inc})")
print(f"Greatest Increase in Profits: {date_dec} (${max_dec})")

#print out txt file results
with open ("financial_analysis.text", "w") as f:
    
    f.write("\n")
    f.write("Financial Analysis\n")
    f.write("-------------------\n")
    f.write(f"Total Months: {months}\n")
    f.write(f"Total: ${total}\n")
    f.write(f"Average Change: ${avg_change}\n")
    f.write(f"Greatest Increase in Profits: {date_inc} (${max_inc})\n")
    f.write(f"Greatest Increase in Profits: {date_dec} (${max_dec})\n")
    f.write("\n")

