#Import necessary modules
import os
import csv

#Create path for csv file
csv_path = os.path.join("Resources", "budget_data.csv")

#Read csv file
with open(csv_path) as csv_file:
    csvreader = csv.reader(csv_file, delimiter=",")
    
    csv_header = next(csvreader)

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
    months = []
    
    for row in csvreader:

        #Find number of months
        month_count = month_count + 1
        
        #Calculate total Profit/Loss
        total_profit_loss = total_profit_loss + int(row[1])

        #Calculate average of changes in Profit/Losses
        #Start by making a list of values and list of months
        values.append(int(row[1]))
        months.append(row[0])
            
    for i in range(1,len(values)):
        change = values[i]-values[i-1]
        list_of_changes.append(change)
            
    #Find average of changes)
    average_change = sum(list_of_changes)/len(list_of_changes)   

    #Find largest increase in profits
    max_positive_change = max(list_of_changes)
    positive_change_index = list_of_changes.index(max_positive_change)
    month_max_positive_change = months[positive_change_index+1]

    #Find largest decrease in profits
    max_negative_change = min(list_of_changes)
    negative_change_index = list_of_changes.index(max_negative_change)
    month_max_negative_change = months[negative_change_index+1]
    
    #Print Financial Analysis to Terminal
    print(" ")
    print("Financial Analysis")
    print("---------------------------")
    print(f"Total months: {month_count}")
    print(f"Total: ${total_profit_loss}")
    print(f"Average change: ${average_change}")
    print(f"Greatest Increase of Profits: {month_max_positive_change} (${max_positive_change})")
    print(f"Greatest Loss: {month_max_negative_change} (${max_negative_change})")

#Create CSV file of Financial Analysis
output_csv_path = os.path.join("analysis", "analysis.csv")

with open(output_csv_path, 'w') as output_file:
    csvwriter = csv.writer(output_file, delimiter=",")

    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["---------------------------"])
    csvwriter.writerow([f"Total months: {month_count}"])
    csvwriter.writerow([f"Total: ${total_profit_loss}"])
    csvwriter.writerow([f"Average change: ${average_change}"])
    csvwriter.writerow([f"Greatest Increase of Profits: {month_max_positive_change} (${max_positive_change})"])
    csvwriter.writerow([f"Greatest Loss: {month_max_negative_change} (${max_negative_change})"])