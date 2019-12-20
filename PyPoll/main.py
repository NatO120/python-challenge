import os
import csv

election_data_csv = os.path.join("C:\\Users\\norti\\Desktop\\PythonStuff\\UofA-PHX-DATA-PT-11-2019-U-C\\03-Python\\Homework\\Instructions\\PyPoll\\Resources\\election_data.csv")

python_poll = os.path.join("Resources", "Election_Data")
votes = []
county = []
total_candidates = []

with open (election_data_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    print(csvreader)
    header = next(csvreader)

    
    correy = []
    khan = []
    li = []
    otooley = []

    for row in csv.reader(csvfile):
        votes.append(int(row[0]))
        county.append(row[1])
        total_candidates.append(row[2])
        
        total_votes = len(votes)
        
    for candidate in total_candidates:
        if candidate == "Correy":
            correy.append(total_candidates)
            correy_votes = len(correy)
        
        elif candidate == "Khan":
            khan.append(total_candidates)
            khan_votes = len(khan)

        elif candidate == "Li":
            li.append(total_candidates)
            li_votes = len(li)

        else:
            otooley.append(total_candidates)
            otooley_votes = len(otooley)

    khan_percent_won = round(((khan_votes / total_votes) * 100), 2)
   
    correy_percent_won = round(((correy_votes / total_votes) * 100), 2)
   
    li_percent_won = round(((li_votes / total_votes) * 100), 2)
   
    otooley_percent_won = round(((otooley_votes / total_votes) * 100), 2)


    if correy_percent_won > max(khan_percent_won, li_percent_won, otooley_percent_won):
        winner_is = "Correy"
     
    elif khan_percent_won > max(correy_percent_won, li_percent_won, otooley_percent_won):
        winner_is = "Khan" 
    
    elif li_percent_won > max(correy_percent_won, khan_percent_won, otooley_percent_won):
        winner_is = "Li"
    
    else:
        winner_is = "O'Tooley"

winner = max(votes)
winner = total_candidates[votes.index(max(votes))]

print("Election Results")
print("----------------------------------------") 
print("Total Votes: " + (str(total_votes)))
print("----------------------------------------")
print("Khan: " + str(khan_percent_won) + "%" + " " + "(" + (str(total_votes)) + ")")
print("Correy: " + str(correy_percent_won) + "%" + " " + "(" + (str(total_votes)) + ")")
print("Li: " + str(li_percent_won) + "%" + " " + "(" + (str(total_votes)) + ")")
print("O'Tooley: " + str(otooley_percent_won) + "%" + " " + "(" + (str(total_votes)) + ")")
print("----------------------------------------")
print("Winner: " + (str(winner)))
print("----------------------------------------")

