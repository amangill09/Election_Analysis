# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candiated who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winnder of election based on popular vote


# assign a variable for the file to load and the path
# file_to_load = 'Resources\election_results.csv'
# election_data = open(file_to_load,'r')
from asyncore import write
import csv
from functools import total_ordering
import os
from textwrap import wrap

file_to_load = os.path.join("resources","election_results.csv")
file_to_save = os.path.join("analysis","election_results.csv")

#initialize total vote count
total_votes = 0
#initialize list of candidate names
candidate_options = []
# initialize dictionary for candidate votes
candidate_votes = {}
# winning_count and winning percentage
winner_name = ""
winning_count = 0
winning_percentage = 0.00

# perform analysis
with open(file_to_load,"r") as election_data:
# read
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    #print(headers)
    
    # print each row
    for row in file_reader:
        total_votes += 1
        candidate_name = row[2]
        # if candidat name does not exist
        if candidate_name not in candidate_options:
            # add to list (if it doesnt exist)
            candidate_options.append(candidate_name) 
            # add name to 
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1

with open(file_to_save, "w") as txt_file:
    election_results = (
        f"\nElection Resuls\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"    
        f"-------------------------\n\n"
                        )
    print(election_results, end="")
    #save to text file
    txt_file.write(election_results)    
    
    
#print(total_votes)
#print(candidate_options)    
#print(candidate_votes)   

    for i in candidate_votes:
        # 2. Retrieve vote count of a candidate.
        votes = candidate_votes[i]
        # 3. Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        # 4. Print the candidate name and percentage of votes.
        #print(f"{i} received {vote_percentage:.1f}% of the vote with a total of {votes:,} votes")
        candidate_results = (f"{i}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)
        # 5. Loop to check current candidate's vote and percentage against highest winning number (initially set to 0). 
        if votes > winning_count and vote_percentage > winning_percentage:
            winning_count = votes
            winning_percentage = vote_percentage
            winner_name = i
    # after for loop to print summary (and write to file)
    winning_candidate_summary = f"\n---------------------\nWinner: {winner_name}\nWinning Vote Count: {winning_count:,}\nWinning percentage: {winning_percentage:,.1f}%\n-------------------"
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)

#print(f'---------------------\nWinner: {winner_name}\nWinning Vote Count: {winning_count:,}\nWinning percentage: {winning_percentage:,.1f}%')

#candidate_results = (f'---------------------\nWinner: {winner_name}\nWinning Vote Count: {winning_count:,}\nWinning percentage: {winning_percentage:,.1f}%')

# close the file
election_data.close()