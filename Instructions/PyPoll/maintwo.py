import os
import csv

#upload csv
file_to_load = os.path.join("Resources/election_data.csv")
output = ""

with open (file_to_load) as csvfile:
    csvreader = csv.reader(csvfile)

    headers = next(csvreader)
    first_row = next(csvreader)

total_votes = 0
candidates_list = 0
percentage_of_winner = 0
total_winner = int(first_row[1])
popular_vote = int(first_row[1])


for row in csvreader:
    total_votes += 1
    candidates_list += int(row[1])