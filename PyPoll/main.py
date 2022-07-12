#Import necessary modules
import os
import csv

#Create path for csv file
csv_path = os.path.join("Resources", "election_data.csv")

#Initialize variables
number_of_votes = 0
candidate_dict = {}
candidate_name = ""

#Read csv file
with open(csv_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    
    csv_header = next(csv_reader)
    print(f"File header is: {csv_header}")

    #Find number of votes cast
    for row in csv_file:
        number_of_votes = number_of_votes + 1
print(number_of_votes)

    #Find candidates who received votes

    #Calculate percentage of votes per candidate

    #Find total number of votes per candidate

    #Find winner of election

    #Print Election Results to terminal

    #Create csv file of Election Results
