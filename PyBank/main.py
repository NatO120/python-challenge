import os
import csv 

budget_data_csv = os.path.join("C:\\Users\\norti\\Desktop\\PythonStuff\\UofA-PHX-DATA-PT-11-2019-U-C\\03-Python\Homework\\Instructions\\PyBank\\Resources\\budget_data.csv")

with open (budget_data_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    print(csvreader)
    header = next(csvreader)

    months = []
    profit = []

    total_months = 0
    total_profit = 0
    change = 0
    prev = 0
    month_change = []
    greatest_increase = ["", 0]
    greatest_decrease = ["", 999999999999]

    for row in csv.reader(csvfile):
        months.append(row[0])
        profit.append(row[1])
    
        total_months = str(len(months))
        total_profit = map(int, profit)
        total_profit = sum(total_profit)

        change = int(row[1]) - prev
        prev = int(row[1])
        month_change = month_change + [row[0]]

        #average = sum(month_change) / len(month_change)
        

        if change > (greatest_increase[1]):
            greatest_increase[0] = row[0]
            greatest_increase[1] = change
            

        if change < (greatest_decrease[1]): 
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = change
    



print("Financial Analysis")
print("----------------------------------------") 
print("Total Months: " + (str(total_months)))
print("Total: " + "$" + (str(total_profit)))
#print("Average Change: " + str(int(average)))
print("Greatest Increase in Profits: " + str(greatest_increase[0]) + " $" + str(greatest_increase[1]))
print("Greatest Decrease in Profits: " + str(greatest_decrease[0]) + " $" + str(greatest_decrease[1]))
       
     






