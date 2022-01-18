a = list()
type(a)

counties = ['Arapahoe', 'Denver', 'Jefferson']
type(counties)

counties.insert(1,"El Paso")

counties[1], counties[2] = counties[2], counties[1]

counties.append("Araphoe")

counties.remove("Araphoe")
counties.pop(3)

counties[1]

counties_tuple = ("Araphahoe","Denver","Jefferson")

type(counties_tuple)

len(counties_tuple)

counties_tuple[:2]

# Dictionaries

my_dictionary = dict()

type(my_dictionary)

counties_dict = {}

counties_dict["Arapahoe"] = 422829
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438

len(counties_dict)

print(counties_dict)

counties_dict.items() # returns a view object
counties_dict.keys() # returns a view object
counties_dict.values() # returns a view object

counties_dict.get("Arapahoe")

counties_dict['Arapahoe']

voting_data = []
voting_data.append({"county":"Arapahoe", "registered_voters":"422829"})
voting_data.append({"county":"Denver", "registered_voters":"463353"})
voting_data.append({"county":"Jefferson", "registered_voters":"432438"})

len(voting_data[2])

voting_data.insert(1,{"county":"Jefferson", "registered_voters":"432438"})

voting_data[1] = {"county":"El Paso", "registered_voters":"461149"}

voting_data.pop(0)

voting_data[1], voting_data[2] = voting_data[2], voting_data[1]

#3.2.8

#how many votes
my_votes = int(input("How many votes did you get?"))
# total votes
total_votes = int(input("Total votes?"))
#percent
percentage_votes = (my_votes / total_votes)*100
print("I received " + str(percentage_votes) + "% of total votes")

counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == "Denver":
    print(counties[1])


temp = int(input("what is the temp"))

if temp > 80:
    print("above 80")    
else:
    print("below 80")

temp2 = int(input("what is the temp"))

if temp2 > 90:
    print("above 90")    
elif temp2 > 80:
    print("above 80")
elif temp2 > 70:
    print("above 70")
else: 
    print("below 70")

#membership operators



counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")

x = 5
y = 5
if x == 5 or not(y == 5):
    print("true")
else:
    print("false")

counties = ["Arapahoe","Denver","Jefferson"]
if "Arapahoe" in counties and "aa" in counties:
    print("true")
else:
    print("false")


x = 0
while x < 5:
    print(x)
    x = x+1

t = "true"    
f = "false"
for county in counties:
    print(county)
for num in range(5):
    print(num)


for i in range(len(counties)):
    print(counties[i])


for i in counties_dict.values():
    print(i)

for i in counties_dict:
    print(i, counties_dict[i])
# same as 
for i in counties_dict.keys():
    print(i, counties_dict[i])
# same as
for i in counties_dict:
    print(i, counties_dict.get(i))
# same as
for i,j in counties_dict.items():
    print(i, j)

for i,j in counties_dict.items():
    print(i + " county has " + str(j) + " registered voters.")


voting_data = []
voting_data.append({"county":"Arapahoe", "registered_voters":"422829"})
voting_data.append({"county":"Denver", "registered_voters":"463353"})
voting_data.append({"county":"Jefferson", "registered_voters":"432438"})

# a list of dictionaries
for i in range(len(voting_data)):
    print(voting_data[i])

# print value of a specifiv key
for i in range(len(voting_data)):
    print(voting_data[i]['county'])

for i in voting_data:
    print(i,i['county'])
    for j in i.values():
        print (j)

for county_dict in voting_data:
    print(county_dict['county'])


x = 5
print(f'I got {x} votes')

for county, voters in counties_dict.items():
    print(f'{county} has {voters} voters')


    candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100}% of the total votes.")

print(message_to_candidate)

for name, values in counties_dict.items():
    print(
    f'{name} has {values:,} votes'

)

voting_data = [{"county":"Arapahoe", "registered_voters": "422829"}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]

for dict in voting_data:
    print(dict)
    for i,j in dict.keys():
        print(
            f"{dict[i]} has {dict[j]} votes"
            )


# inporting file
import datetime
now = datetime.datetime.now()
print(now)

import csv
dir(csv)

dir(counties_dict)
dir(now)

import random
dir(random)
print(random)

# file_to_load = 'Resources\election_results.csv'
# election_data = open(file_to_load,'r')
import csv
import os

with open(os.path.join("resources","election_results.csv"),"r") as election_data:
    print(election_data)


# perform analysis

# close the file
election_data.close()


import csv
import os
file_to_save = os.path.join("analysis","test.csv")
#test = open(file_to_save,"w") 
#test.write("Hello World")
with open(file_to_save,"w") as txt_file:
    txt_file.write("Arapahoe, ")
    txt_file.write("Denver, Jefferson\n\nnew_line")

txt_file.close()


import csv
import os
file_to_save = os.path.join("analysis","test.csv")
#test = open(file_to_save,"w") 
#test.write("Hello World")
with open(file_to_save,"w") as txt_file:
    txt_file.write("Arapahoe, ")
    txt_file.write("Denver, Jefferson\n\nnew_line")

txt_file.close()


import csv
import os
file_to_save = os.path.join("analysis","test.csv")
#test = open(file_to_save,"w") 
#test.write("Hello World")
with open(file_to_save,"w") as txt_file:
    txt_file.write("Countines in Election\n----------------\nArapahoe\nDenver\nJefferson")
txt_file.close()