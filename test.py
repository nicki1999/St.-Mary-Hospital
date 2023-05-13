import tabula
import os
import pandas as pd
import datetime
import sys
from PyQt5.QtWidgets import QApplication
from user_interface import UserInterface

# clear the terminal
os.system('cls' if os.name == 'nt' else 'clear')

#for the 1st page of the report
pdf_path = './service_orthopedics_specialty_orthopedics-1.pdf'

#for all pages of the report
pdf_path_all = './test.pdf'

pdf_path_2pages = './service_orthopedics_specialty_orthopedics-2.pdf'
# Create an empty list to store the data frames for each page
dfs = []

# Iterate over each page of the PDF and append the data frame to the list
delay_time = []
for page in range(1, len(tabula.read_pdf(pdf_path_all, pages='all'))+1):
    tables = tabula.read_pdf(pdf_path_all, pages=page, multiple_tables=True)
    print(tables[0])
    if isinstance(tables[0], pd.DataFrame):
        # removes all the columns with no values in them
        tables[0] = tables[0].dropna(axis=1, how='all')
        #remove the first row
        tables[0] = tables[0].drop(index=range(1, 2))
        tables[0] = tables[0][1:]
        dfs.append(tables[0])

# concatenate the data frames in dfs into a single data frame
print(dfs)
df = pd.concat(dfs, ignore_index=True)


# replace NaN values with empty strings

df.to_csv('./output_1.csv', index=False)
#----------------------DONE formatting the data-----------------------------------------
