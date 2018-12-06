import os
import csv

#set data file location
file_path = os.path.join("../../../NUCHI201811DATA2/Homework/03-Python/Instructions/PyBank/Resources/","budget_data.csv")

#open and read csv file
with open(file_path, "r") as bankfile:
    bankline = csv.reader(bankfile, delimiter = ",")

    #initialize variables
    line_count = 0         #file line count
    month_count = 0        #month count
    plsum = 0              #profit loss sum      
    plchg = 0              #profit loss avg change
    plchgtot = 0           #profit loss total change
    plprior = 0            #profit loss prior value
    plgrinc = 0            #profit loss greatest increase
    plgrincmth = "Start"   #profit loss greatest increase month
    plgrdec = 0            #profit loss greatest decrease
    plgrdecmth = "Start"   #profit loss greatest decrease month

    #iterate through file to build metrics
    for row in bankline:         

        if line_count > 0 :

            month_count += 1
            plsum = plsum + float(row[1])

            if line_count > 1 :
                plchg = float(row[1])-plprior
                plchgtot = plchgtot + plchg

                if plchg > plgrinc:
                    plgrinc = plchg
                    plgrincmonth = row[0]
            
                if plchg < plgrdec:
                    plgrdec = plchg
                    plgrdecmonth = row[0]

            plprior = float(row[1])

        line_count += 1
    
    print(f"Financial Analysis")
    print(f"----------------------------")
    print(f"Total Months:  {month_count}")
    print(f"Total:  ${round(plsum)}")
    print(f"Average Change:  ${round(plchgtot /(month_count - 1),2)}")
    print(f"Greatest Increase in Profits: {plgrincmonth}  (${round(plgrinc)})")
    print(f"Greatest Decrease in Profits: {plgrdecmonth}  (${round(plgrdec)})")

    with open("output.txt", "w") as outfile:
        outfile.write(f"Financial Analysis\n")
        outfile.write(f"----------------------------\n")
        outfile.write(f"Total Months:  {month_count}\n")
        outfile.write(f"Total:  ${round(plsum)}\n")
        outfile.write(f"Average Change:  ${round(plchgtot /(month_count - 1),2)}\n")
        outfile.write(f"Greatest Increase in Profits: {plgrincmonth}  (${round(plgrinc)})\n")
        outfile.write(f"Greatest Decrease in Profits: {plgrdecmonth}  (${round(plgrdec)})\n")