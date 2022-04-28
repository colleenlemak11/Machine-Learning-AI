import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# bank customers data set: ID and ZIP Code are ignored as inputs of the model

# ID                 Customer ID
# Age                Age
# Experience         Professional experience (years)
# Income             Annual income (thousands of dollars)
# Family             Total family members
# CC Average         Avg. spending on credit cards (thousands of dollars)
# Education          Education level: 1:undergraduate, 2:graduate, 3:postgraduate
# Mortgage           House mortgage value (thousands of dollars)
# Securities Account Has a security account: 1:yes, 0:no
# CD Account         Has a CD account: 1:yes, 0:no
# Online             Has online banking facility:  1:yes, 0:no
# Credit Card        Has a credit card issued by the bank: 1:yes. 0:no
# ZIP Code           Home address ZIP code
# Personal Loan      Target variable

# read input file
bank_data = pd.read_csv("bank.csv")

# data set columns, null values and data types
print("\n Data set columns, null vaues and data types \n")
print(bank_data.info())

# total missing values by column
print("\n Missing values \n")
print(bank_data.isnull().sum())

# data description: min, 25%, 50%, 75%, max
transpose = bank_data.describe().T

print("\n Data description: min, 25%, 50%, 75%, max \n")
print(transpose[["min","25%","50%","75%","max"]])

# target column distribution
total_loans = pd.DataFrame(bank_data["Personal Loan"].value_counts()).reset_index()
total_loans.columns = ["Labels","Personal Loan"]

print("\n Personal loans distribution \n")
print(total_loans)

# data analysis: which customers are more likely to take out a loan
