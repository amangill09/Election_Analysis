# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candiated who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winnder of election based on popular vote


# assign a variable for the file to load and the path
# file_to_load = 'Resources\election_results.csv'
# election_data = open(file_to_load,'r')
import csv
import os

file_to_load = os.path.join("resources","election_results.csv")
file_to_save = os.path.join("analysis","election_results.csv")

# perform analysis
with open(file_to_load,"r") as election_data:
# read
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    print(headers)
    #for row in file_reader:
    #    print(row[0])



# close the file
election_data.close()

