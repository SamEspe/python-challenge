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

#Set up CSV
output_csv_path = os.path.join("analysis", "Election_Results.csv")

with open(output_csv_path, 'w') as output_file:
    csvwriter = csv.writer(output_file, delimiter=",")
    #Find percentage, winner, print to terminal, print to csv
    print("")
    print("Election Results")
    csvwriter.writerow(["Election Results"])
    print("--------------------------")
    csvwriter.writerow(["--------------------------"])
    print(f"Total votes: {number_of_votes}")
    csvwriter.writerow([f"Total votes: {number_of_votes}"])
    print("--------------------------")
    csvwriter.writerow(["--------------------------"])
    print("")

    for candidate_name in candidate_dict:
        percent_of_votes = (candidate_dict[candidate_name]/number_of_votes)*100
        print(f"{candidate_name}: {percent_of_votes:.3f}% ({candidate_dict[candidate_name]})")
        csvwriter.writerow([f"{candidate_name}: {percent_of_votes:.3f}% ({candidate_dict[candidate_name]})"])

        if winner not in candidate_dict.keys():
            winner = candidate_name
        if candidate_dict[candidate_name] > candidate_dict[winner]:
            winner = candidate_name
    print("")
    print("--------------------------")
    csvwriter.writerow(["--------------------------"])
    print(f"Winner is: {winner}")
    csvwriter.writerow({f"Winner is: {winner}"})
    print("--------------------------")
    csvwriter.writerow(["--------------------------"])