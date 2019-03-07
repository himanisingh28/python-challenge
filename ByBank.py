import os
import csv

# Path to collect data from the CSV file in the folder
budgetDataCSV = os.path.join('..', 'python-challenge', 'budget_data.csv')


# Read in the CSV file
# Define the function and have it accept the 'budgetDataCSV' as its sole parameter
    
with open(budgetDataCSV, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    #initializing the variables and lists
    totalProfitLoss = 0
    totalMonths = 0
    avgChange = 0
    totalChange = 0
    greatestIncrease = 0
    greatestDecrease = 0
    monthly_change = 0

    monthlyChangeList = []
    monthList = []
    profitLossValue = []
    
    
    # Loop through the data
    for row in csvreader:

        #Iterate through the month column and append the values to an empty list
        monthList.append(row[0])
        
    
        # Find the total profit/loss
        totalProfitLoss = totalProfitLoss + int(row[1])

        # Iterate through the profit/loss column and append the values to a 2nd emply list
        profitLossValue.append(row[1])
        
        #Calculting total number of months frm the length of the monthlist
        totalMonths = (len(monthList)) 
       
    #For loop to iterate through the rows to calculate average change in profit loss
    #Initializing the loop from 1. If we initialize from 0 then there is no value for -1 index
    for i in range(1,totalMonths):
        monthly_change = int(profitLossValue[i]) - int(profitLossValue[i-1])
       
        #Calculating the total profit loss change for every month
        totalChange = totalChange + monthly_change

        #Calculating the greatest increase and decrease in profit
        if monthly_change > greatestIncrease:
            greatestIncrease = monthly_change
            greatestMonth = monthList[i]
        
        if monthly_change < greatestDecrease:
            greatestDecrease = monthly_change
            smallestMonth = monthList[i]

    #Calculating the average change in profit/loss over a period of time
    #Calculating it for total rows -1 as we initiated the for loop from 1
    avgChange = round(totalChange/(int(totalMonths)-1),2)



    print (f"Financial Analysis")
    print (f"-----------------------------------------------")
    
    print (f"Total Months: {totalMonths}")
    print (f"Total: {totalProfitLoss}")
    print (f"Average Change: {avgChange}")
    print (f"Greatest Increase in Profits: {greatestMonth} ($ {greatestIncrease})")
    print (f"Greatest Decrease in Profits: {smallestMonth} ($ {greatestDecrease})")
    
    output_path = os.path.join("..", "python-challenge", "writeBudgetData.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(['Total Months', 'Total', 'Average Change', 'Greatest Increase in Profits', 'Greatest Decrease in Profits'])

    # Write the second row
    csvwriter.writerow([totalMonths, totalProfitLoss, avgChange, str(greatestMonth) + " (" + "$ " +str(greatestIncrease) + ")", str(smallestMonth) +  " (" + "$ " +str(greatestDecrease) + ")"])

    
