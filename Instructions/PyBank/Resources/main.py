import os
import csv

#load to output

file_to_load = os.path.join("budget_data.csv")
output = ""
with open (file_to_load) as csvfile:
    csvreader = csv.reader(csvfile)

    headers = next(csvreader)
    first_row = next(csvreader)

    net_change = 0
    total_months = 1
    prev_rev = int(first_row[1])
    total_profit = int(first_row[1])
    greatest_increase_value = 0
    greatest_decrease_value = 100000000
    greatest_increase_month = ""
    greatest_decrease_month = ""
    
    #profits = []

    for row in csvreader:
        total_months += 1
        total_profit += int(row[1])
        net_change += int(row[1]) - prev_rev
        current_change = int(row[1]) - prev_rev
        
        #profits.append(current_change)
        #print(net_change)

        if current_change > greatest_increase_value:
            greatest_increase_value = current_change
            greatest_increase_month = row[0]

        if current_change < greatest_decrease_value:
            greatest_decrease_value = current_change
            greatest_decrease_month = row[0]   

        prev_rev = int(row[1])

    # greatest_increase_value = max(profits)
    # print("Max: ", max(profits))
    # print("Min: ", min(profits))
    # print("Average change :", sum(profits)/len(profits))

        
    print('\n\nFinancial Analysis')
    print('----------------------------')
    print('Total Months: ' + str(total_months))
    print('Total: $' + str(total_profit))
    print('Average Change: $' + str(net_change/(total_months-1)))
    print('Greatest Increase in Profits:' + (greatest_increase_month) +  ' $' + str(greatest_increase_value))
    print('Greatest Decrease in Profits:' + (greatest_decrease_month) +  ' $' + str(greatest_decrease_value))
    output += '\n\nFinancial Analysis\n'
    output += '----------------------------\n'
    output += 'Total Months: ' + str(total_months) + '\n'
    output += 'Total: $' + str(total_profit) + '\n'
    output += 'Average Change: $' + str(net_change/(total_months-1)) + '\n'
    output += 'Greatest Increase in Profits:' + (greatest_increase_month) +  ' $' + str(greatest_increase_value) + '\n'
    output += 'Greatest Decrease in Profits:' + (greatest_decrease_month) +  ' $' + str(greatest_decrease_value) + '\n'
    print(output)

file_to_output = os.path.join("budget_data.txt")



with open (file_to_output, "w") as txt_file:
    txt_file.write(output)

#day 2 act 10-cvs python    
   



