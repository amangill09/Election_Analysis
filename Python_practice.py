#hello world

from operator import index


print("hello world")

# lists

# Declare empty list
my_list = []

# add values to list
my_list.append("zero") ## append only adds to the end of list. No way to give an index value here 
my_list.append("one") 
my_list+="two" # same as append but breaksdown the string
my_list+=["two"] # same as append
my_list[2]+="two" # this will append to value at index 2


my_list.insert(2,"two")## insert will add whereever the index points to
my_list.insert(-1,"three") # -1 will insert before index -1 i.e. second last position

# remove from list
my_list.pop() # uses index. blank removes last
my_list.pop(0) # removes first position
my_list.remove("one") # uses value. cannot be blank

#diff data type lists
diff = ["cake",2,["paper","write","2022/01/01"]]

#2D lists - list os lists
list_of_lists = [[1,'a'],['b',2]]

#retreiving data from list
my_list[0] #using index
my_list[-1]
my_list[1:3]
list_of_lists[1][0] #2d list have two indexes

first, *middle, last = my_list
print(first,middle,last)

my_list.index("one") # retrieve index for an element

# performing operations on lists
my_list[-1] = "new value" # updates last index value
sorted(my_list) # sorted just outputs the sorted list. does not modify original list
my_list.sort() # sort func takes no arguments. modifies original list
my_list.reverse() #reverses list
my_list = my_list + ["two","one"] # add lists

a = [0]
a = a*100 # hundred zeroes in a list

a = [*range(5)] # creates list with output of range(5)

# loops
for val in my_list: # value will get each value assigned to it. no need of indexes
    print(val)
for indx in range(len(my_list)): # get list using an index
    print(indx,my_list[indx])
for i,x in enumerate(my_list,0): # enumerate gives index and value in a tuple
    print(i,x)

[print(x) for x in my_list] # list comprehension to iterate through a list

#other
my_list.count("one") # count takes values
len(my_list)  #len function returns # of elements in a list





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
my_d = {}

# Create and add elements
my_d = {1:'Navin',2:'Kiran',4:"Harsh"}

keys = ['Navin','Kiran',"Harsh"]
values = ['Python','Java',"JS"]
DictFromLists = dict(zip(keys,values)) # create a dict from lists 
DictFromLists['Monika'] = 'CS' # add a new key and value by directly assigning value to a key
DictFromLists.update({'Kiran':'C#'}) # use update func with argument = dictionary with updates 
Code_editor_dict = {'JS':'Atom','CS':'VS','Python':['Pychar','Sublime'],'Java':{'JSE':'Netbeans','JEE':'Eclipse'}}
Code_editor_dict['Python'].append("appended1") # appends to the list in dictionary - after last position
Code_editor_dict['Python'].append(5) # appends integer 5 to the list in dictionary - after last position
Code_editor_dict['Python']+=("_appendedagain") # appends to the list in dictionary - after last position but breaks down the string
Code_editor_dict['Python']+=(["_appendedagain"]) # appends this list to the exisitng list in dictionary - after last position 
Code_editor_dict['Python'][3]+=("_appendedagain") # appends to the index postion - adds strings to existing string

# remove elements
del DictFromLists['Harsh'] # del based on key. Original Dict gets updated.
DictFromLists.pop('Monika') # pop based on key. Original Dict gets updated.
Pop_value = DictFromLists.pop('Monika') # We can also assign popped value to a variable

# 2D Dictionary
Code_editor_dict = {'JS':'Atom','CS':'VS','Python':['Pychar','Sublime'],'Java':{'JSE':'Netbeans','JEE':'Eclipse'}}
Code_editor_dict['JS'] # acceess element with value type = STR
Code_editor_dict['Python'][0] # acceess element with value type = List
Code_editor_dict['Java']['JSE'] # acceess element with value type = Dict. THe second argument should be equal to a key

# access elements
my_d[1] # use the Rectangular (list) bracket to retrieve value based on Key. Notice no "" since key is an integer (1)
DictFromLists["Harsh"]
my_d[3] # error since 3 is not a key
my_d.get(4) # use brackets not rect brackets
my_d.get(3) # no error but blank
my_d.get(3,'Not Found') # display message if blank

my_d.items() # same as my_d i.e. name of dict
my_d.keys() # gives the keys , takes no arguments
my_d.values() # gives values, takes no arguments

len(my_d) # number of keys

# looping
for i in Code_editor_dict: # assigns keys to i
    print(i)
for i in Code_editor_dict.keys(): # assigns keys to i, same without .keys(). takes no argument
    print(i)
for i in Code_editor_dict.values(): # assigns values to i, takes no argument
    print(i)
for i,j in Code_editor_dict.items(): # assigns keys and values to i. This is only way to get both. takes no argument
    print(i,j)
for i in Code_editor_dict['Python']: # assigns values from list assigned to key python to i, takes no argument
    print(i)



a = "Hello World"

list(a)
set(a)

# perform operations on dictionaries
test_dict = {'gfg' : 6, 'is' : 4, 'best' : 7}
for key in test_dict:    # arithmetic operation on a value
    test_dict[key] *= 3

Code_editor_dict["Python"] += ['VS'] # add to a 'list' value in dictionary

# other




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