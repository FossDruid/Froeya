import pandas as pd
import numpy as np
from pandas import DataFrame, read_csv
import csv

csvFilePath = ""
rows = []

def dataReadFile(rows, csvFile):
    with open(csvFile, 'r') as file:
        csvreader = csv.reader(file)
        header = next(csvreader)
        for row in csvreader:
            rows.append(row)
    data = pd.read_csv(csvFile)
    print(header)
    print(rows)

#dataReadFile(rows, csvFilePath)
#data = pd.read_csv("testData/peopleJobPay.csv")