import os
import csv
budget_csv = os.path.join('Resources', 'budget_data.csv') # Specifies directory of .csv file

def finAnalysis(profit_data):
    date = str(profit_data[0])
    final_amount = int(profit_data[1])

    print(profit_data)
    