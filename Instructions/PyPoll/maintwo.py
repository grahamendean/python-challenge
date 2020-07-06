import os
import csv

#upload csv
file_to_load = os.path.join("Resources/election_data.csv")
output = ""

with open (file_to_load) as csvfile:
    csvreader = csv.reader(csvfile)

    headers = next(csvreader)
    first_row = next(csvreader)

    total_votes = 1
    candidates_names = []
    candidate_votes = {}
    

    for row in csvreader:
        total_votes += 1
        candidates_list = row[2]
        

        if candidates_list in candidates_names:
            candidates_number = candidates_names.index(candidates_list)
            candidate_votes[candidates_names] = candidate_votes[candidates_names] + 1
        else:
            candidates_names.append(candidates_list)
            
            

        


#print statements

print('\n\nElection Results')
print('----------------------------')
print('Total Votes: ' + str(total_votes))
print('----------------------------')
print(candidates_names)
for candidates_names in candidate_votes:
    print(candidates_names)



        
