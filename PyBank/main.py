#Import necessary modules
import os
import csv

#Create path for csv file
csv_path = os.path.join("Resources", "budget_data.csv")

#Read csv file
with open(csv_path) as csv_file:
    csvreader = csv.reader(csv_file, delimiter=",")
    
    csv_header = next(csvreader)
    print(f"File header is: {csv_header}")

#Find number of months
    row_count = 0
    for row in csvreader:
        row_count = row_count + 1
        print(row)
    print(row_count)

#Calculate total amount of "Profit/Losses"

#Calculate average of changes in "Profit/Losses"

#Find largest increase in profits

#Find largest decrease in profits

#Print Financial Analysis to Terminal

#Create CSV file of Financial Analysis