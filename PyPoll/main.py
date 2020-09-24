# Import Modules
# Way to create file paths across operating systems
import os
# Module to READ csv files
import csv

# Create a file path to election_data.csv
csvpath = os.path.join('resources', 'election_data.csv')

# Declare variables:
# Lists to capture the names of candidates, vote numbers, % of total votes per candidate, and sum of votes
candidates = []

number_votes = []

percent_votes = []

sum_votes = 0

# Open the CSV file to start finding the data
with open(csvpath, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter =',')
    csv_header = next(csvreader)

    #For Loop to start total all the votes
    for row in csvreader:
        sum_votes += 1

        #Another For loop to determine if candidate is on list, if not, will add name to the list we are making 
        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            number_votes.append(1)
        else:
            index = candidates.index(row[2])
            number_votes[index] += 1

    #Another For Loop to add the percentage of votes list
    for votes in number_votes:
        percentage = (votes/sum_votes) * 100
        percentage = round(percentage)
        #Use the "%.3f%%" code for the code to print correctly...check stackoverflow
        percentage = "%.3f%%" % percentage
        percent_votes.append(percentage)
    
    # Formulas to find the sinning candidate
    winner = max(number_votes)
    index = number_votes.index(winner)
    winning_candidate = candidates[index]



# Displaying results
print("Election Results")
print("--------------------------")
print(f"Total Votes: {str(sum_votes)}")
print("--------------------------")
for i in range(len(candidates)):
    print(f"{candidates[i]}: {str(percent_votes[i])} ({str(number_votes[i])})")
print("--------------------------")
print(f"Winner: {winning_candidate}")
print("--------------------------")


# Exporting to .txt file
output = open("output.txt", "w")
line1 = "Election Results"
line2 = "--------------------------"
line3 = str(f"Total Votes: {str(sum_votes)}")
line4 = str("--------------------------")
output.write('{}\n{}\n{}\n{}\n'.format(line1, line2, line3, line4))
for i in range(len(candidates)):
    line = str(f"{candidates[i]}: {str(percent_votes[i])} ({str(number_votes[i])})")
    output.write('{}\n'.format(line))
line5 = "--------------------------"
line6 = str(f"Winner: {winning_candidate}")
line7 = "--------------------------"
output.write('{}\n{}\n{}\n'.format(line5, line6, line7))