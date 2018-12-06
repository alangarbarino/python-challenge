import os
import csv

#set data file location
file_path = os.path.join("../../../NUCHI201811DATA2/Homework/03-Python/Instructions/PyPoll/Resources/","election_data.csv")

#open and read csv file
with open(file_path, "r") as pollfile:
    polline = csv.reader(pollfile, delimiter = ",")

    #initialize variables
    line_count = 0         #file line count
    vote_count = 0         #vote count
    candidates = []        #list of candidates with votes
    
    #build list of candidates with votes
    for vote in polline:   
        if vote[2] not in candidates:

            if line_count > 0:
                candidates.append(vote[2])

        line_count += 1

    #initialize dictionary to hold candidates and votes
    
    listcounter = 0

    for entry in candidates:

        if listcounter == 0:
            TallyDict = ({candidates[listcounter]: 0})
        else:
            TallyDict.update({candidates[listcounter]: 0})
    
        listcounter += 1

# iterate through file again counting votes

with open(file_path, "r") as pollfile2:
    polline2 = csv.reader(pollfile2, delimiter = ",")

    line_count = 0

    for vote2 in polline2: 
        if line_count > 0:
            Name = vote2[2]
            NewTotal = TallyDict[Name] + 1
            TallyDict[Name] = NewTotal
            vote_count += 1
        line_count += 1

    
    print(f"  Election Results")
    print(f"  ----------------------------")
    print(f"  Total Votes:  {vote_count}")
    print(f"  ----------------------------")
    
    maxvotes = 0
    finalvotes = 0
    winner = "START"
    
    for name in candidates:
        finalvotes = TallyDict[name]
        print(f"  {name}:   {format(float(((finalvotes/vote_count)*100)),'.3f')}%  ({TallyDict[name]})")
    
        if finalvotes > maxvotes:
            maxvotes = finalvotes
            winner = name
    
    print(f"  ----------------------------")
    print(f"  Winner:  {winner}")
    print(f"  ----------------------------")

with open("output.txt", "w") as outfile:
    outfile.write(f"  Election Results\n")
    outfile.write(f"  ----------------------------\n")
    outfile.write(f"  Total Votes:  {vote_count}\n")
    outfile.write(f"  ----------------------------\n")
    for name in candidates:
        finalvotes = TallyDict[name]
        outfile.write(f"  {name}:   {format(float(((finalvotes/vote_count)*100)),'.3f')}%  ({TallyDict[name]})\n")
    outfile.write(f"  ----------------------------\n")
    outfile.write(f"  Winner:  {winner}\n")
    outfile.write(f"  ----------------------------\n")