# Import Modules
# Way to create file paths across operating systems
import os
# Module to READ csv files
import csv

# Declare Variables
greatest_increase = 0
greatest_decrease = 0
greatest_increase_month = 0
greatest_decrease_month = 0
total_months = 0
net_total = 0
monthly_change = []
month_count = []

# Create a file path to budget_data.csv
csvpath = os.path.join('Resources', 'budget_data.csv')


# Open the CSV File
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    row = next(csvreader)

    # Calculate total number of months with the Net Profits and Losses with Row Variables
    previous_row = int(row[1])
    total_months += 1
    net_total += int(row[1])
    greatest_increase = int(row[1])
    greatest_increase_month = row[0]

    # For Loop that loops through each row after the header
    for row in csvreader:

        # Find Month Total
        total_months += 1
        # Calculate Net Profits and Losses
        net_total += int(row[1])

         #Calculate Change between the months 
        revenue_change = int(row[1]) - previous_row
        monthly_change.append(revenue_change)
        previous_row = int(row[1])
        month_count.append(row[0])
    
        # Find the greatest Increase in own For Loop
        if int(row[1]) > greatest_increase:
            greatest_increase = int(row[1])
            greatest_increase_month = row[0]
        
        # Calculate Greatest Decrease in own For Loop
        if int(row[1]) < greatest_decrease:
            greatest_decrease = int(row[1])
            greatest_decrease_month = row[0]

    #Calculate the change in Mean and Dates
        mean_change = sum(monthly_change) / len(monthly_change)
        highest = max(monthly_change)
        lowest = min(monthly_change)

#Display Analysis
print("Financial Analysis")
print("-------------------")
print(f"Total Months: {str(total_months)}")
print(f"Total: ${str(net_total)}")
print(f"Average Change in Profits/Losses: ${str(round(mean_change,2))}")
print(f"Greatest Increase in Profits:, {greatest_increase_month}, (${highest})")
print(f"Greatest Decrease in Profits:, {greatest_decrease_month}, (${lowest})")


#Send to a text file
output = open("output.txt", "w")

line1 = "Financial Analysis"
line2 = "---------------------"
line3 = str(f"Total Months: {str(total_months)}")
line4 = str(f"Total: ${str(net_total)}")
line5 = str(f"Average Change in Profits/Losses: ${str(round(mean_change,2))}")
line6 = str(f"Greatest Increase in Profits: {greatest_increase_month} (${str(highest)})")
line7 = str(f"Greatest Decrease in Profits: {greatest_decrease_month} (${str(lowest)})")
output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7))