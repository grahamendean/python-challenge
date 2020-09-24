import os
import csv

#upload csv
file_to_load = os.path.join("Resources/election_data.csv")
output = ""
voting_output = ""

#open csv file
with open (file_to_load) as csvfile:
    csvreader = csv.reader(csvfile)

    headers = next(csvreader)
    first_row = next(csvreader)

    total_votes = 0
    candidates_names = []
    candidate_votes = {}
    
#begin to loop for total votes and candidates
    for row in csvreader:
        total_votes += 1
        candidate_name = row[2]
        

        if candidate_name not in candidates_names:
            candidates_names.append(candidate_name)
            candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1    
        
#print statements

print('\n\nElection Results')
print('----------------------------')
print('Total Votes: ' + str(total_votes))
print('----------------------------')

winning_votes = 0
#determine the winning candidate along with the votes for each
for candidate_name in candidate_votes:
    votes = candidate_votes.get(candidate_name)
    vote_percentage = float(votes) / float(total_votes) * 100
    if votes > winning_votes:
        winning = candidate_name
        winning_votes = votes
    voter_output = f'{candidate_name}: {round(vote_percentage, 3)}% ({votes})\n'
    voting_output += voter_output
    print(voter_output, end="")    
print('----------------------------')    
print('Winner: ' + winning)
print('----------------------------')


#send to txt file
file_to_output = os.path.join("Resources/election_data.txt")

with open (file_to_output, "w") as txt_file:
    #txt_file.write(output)
    election_results = (
   f"\n\nResults\n"
   f'--------------\n'
   f'Total Votes: {total_votes}\n'
   f'--------------\n'
   f'Candidates: {voting_output}\n' #
   f'--------------\n'
   f'Winner: {winning}\n')
    print(election_results, end="")
    txt_file.write(election_results)

  

    

