Note: I worked with Puneeth Nimmagadda for this challenge. We followed pair-programming methodology and the code and readme were co-created.

# **Election_Analysis**

## Project Overview

We are performing election audit for a Colorado Board of Elections employee. The following tasks need to be performed:

1. Calculate the total number of votes cast
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

## Resources 
- Data Source: election_results.csv 
- Software: Python 3.9.7, Visual Studio Code, 1.63.2

## Results 
The analysis of the election show that: 
- There were 369,711 votes cast in the election.
- The candidates were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
-The candidate results were:
    - Charles Casper Stockham received 23.0% of vote and 85,213 number of votes.
    - Diana DeGette received 73.8% of vote and 272,892 number of votes.
    - Raymon Anthony Doane received 3.1% of vote and 11,606 number of votes.
- The winner of election was:
    - Diana DeGette, who received 73.8% of vote and 272,892 number of votes.

## Challenge Overview

The Colorado Board of Elections employee now wants us to perform an audit based on county. The following tasks need to be performed:

1. Get a complete list of counties who received votes.
2. Calculate the total number of votes each county received.
3. Calculate the percentage of votes by each county.
4. Determine the largest outcome of the election based on popular vote by county.

## Challenge Results

The analysis of election by county show us that:
- There were three counties:
    - Jefferson
    - Denver
    - Arapahoe
- The results for each county are:
    - Jefferson received 10.5% of votes and a total of 38,855 votes.
    - Denver received 82.8% of votes and a total of 306,055 votes.
    - Arapahoe received 6.7% of votes and a total of 24,801 votes.
- The largest outcome of election was in:
    - Denver county, that received 82.8% of votes and a total of 306,055 votes.

## Election Audit Summary
This python code showed us how to get results for small data set which includes ballot number, candidate name and location. We were able to find who won, by what percentage and which county got most votes. This code can be modified and used for any election and here here two examples:
- There dataset can include more voter information like gender and we can analyze what the vote distribution looks like. In the for loop we will add another counter to determine if the vote if male, female or other. Then we can use those counts to determine vote percent by gender. 
- For the same data set we can determine votes for each candidate by county. We can add another dictionary in the candidate_votes which captures each county as key and total votes as a value. We will use an if loop to capture the county names just like we did for candidates.

## GitHUB Links
- [Python Challenge Code](PyPoll_Challenge.py)    
- [Election Results Folder](analysis)    
- [Election Resources Folder](resources)    
- [Election Analysis Text File](analysis/election_analysis.txt)    