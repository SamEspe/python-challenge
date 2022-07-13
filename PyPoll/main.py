#Import necessary modules
import os
import csv

from sympy import per

#Create path for csv file
csv_path = os.path.join("Resources", "election_data.csv")

#Initialize variables
number_of_votes = 0
candidate_dict = {}
candidate_name = ""
percent_of_votes = 0.0
percent_list = []
winner = ""

#Read csv file
with open(csv_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    
    csv_header = next(csv_reader)

    #Find number of votes cast
    for row in csv_reader:
        number_of_votes = number_of_votes + 1
        
        candidate_name = row[2]
    #Find candidates who received votes and how many votes they got in total
        if candidate_name in candidate_dict.keys():
            candidate_dict[candidate_name] = candidate_dict[candidate_name] + 1

        else:
            candidate_dict[candidate_name] = 1

#Set up output file
output_path = os.path.join("analysis", "Election_Results.txt")

with open(output_path, 'w') as output_file:
    #Find percentage, winner, print to terminal, print to csv
    print("")
    print("Election Results")
    output_file.write("Election Results\n") 
    print("--------------------------")
    output_file.write("--------------------------\n")
    print(f"Total votes: {number_of_votes}")
    output_file.write(f"Total votes: {number_of_votes}\n")
    print("--------------------------")
    output_file.write("--------------------------\n")
    print("")

    for candidate_name in candidate_dict:
        percent_of_votes = (candidate_dict[candidate_name]/number_of_votes)*100
        print(f"{candidate_name}: {percent_of_votes:.3f}% ({candidate_dict[candidate_name]})")
        output_file.write(f"{candidate_name}: {percent_of_votes:.3f}% ({candidate_dict[candidate_name]})\n")

        if winner not in candidate_dict.keys():
            winner = candidate_name
        if candidate_dict[candidate_name] > candidate_dict[winner]:
            winner = candidate_name
    print("")
    print("--------------------------")
    output_file.write("--------------------------\n")
    print(f"Winner is: {winner}")
    output_file.write(f"Winner is: {winner}\n")
    print("--------------------------")
    output_file.write("--------------------------")