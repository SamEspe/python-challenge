#Import necessary modules
import os
import csv

#Create path for csv file
csv_path = os.path.join("Resources", "budget_data.csv")

#Read csv file
with open(csv_path) as csv_file:
    csvreader = csv.reader(csv_file, delimiter=",")
    
    csv_header = next(csvreader)
    #print(f"File header is: {csv_header}")

#Initialize variables
    month_count = 0
    total_profit_loss = 0
    change = 0
    list_of_changes = []
    average_change = 0.0
    max_positive_change = 0
    max_negative_change = 0
    greatest_gain = []
    greatest_loss = []
    values = []
    i=1
    for row in csvreader:

        #Find number of months
        month_count = month_count + 1
        
        #Calculate total Profit/Loss
        total_profit_loss = total_profit_loss + int(row[1])
        #print(row)

        #Calculate average of changes in Profit/Losses
        #Start by making a list of values
        values.append(int(row[1]))
    
    # print(values)
        
    for i in range(1,len(values)):
        change = values[i]-values[i-1]
        list_of_changes.append(change)
        # print(change)
    
    #Find average of changes
    #print(list_of_changes)
    average_change = sum(list_of_changes)/len(list_of_changes)   
   # print(average_change)

    #Find largest increase in profits
    # max_positive_change = max(list_of_changes)
    # print(max_positive_change)

    # for row in csvreader:
    #     if row[1] == max_positive_change:
    #         greatest_gain.append(row)
    # print(greatest_gain)

    #Find largest decrease in profits
    
    
    #Print Financial Analysis to Terminal
    print(" ")
    print("Financial Analysis")
    print("---------------------------")
    print(f"Total months: {month_count}")
    print(f"Total: ${total_profit_loss}")
    print(f"Average change: ${average_change}")
    #print(f"Greatest Increase of Profits: {greatest_gain[0]} ${greatest_gain[1]}")
    #print(f"Greatest Loss: {greatest_loss[0]} ${greatest_loss[1]}")

#Create CSV file of Financial Analysis