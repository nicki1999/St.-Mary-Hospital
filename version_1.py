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
pdf_path_all = './2022-04-30_onwards_record.pdf'

pdf_path_2pages = './service_orthopedics_specialty_orthopedics-2.pdf'
# Create an empty list to store the data frames for each page
dfs = []


all_pages = tabula.read_pdf(pdf_path_all, pages='all')
# with open(pdf_path_all, 'rb') as pdf_file:
#     pdf_reader = PyPDF2.PdfReader(pdf_file)
#     num_pages = len(pdf_reader.pages)
#         # Get the text of the last page in the PDF file
#     last_page_text = pdf_reader.pages[num_pages-1].extract_text()

#     # Print the extracted text
#     print(last_page_text)



# Iterate over each page of the PDF and append the data frame to the list
delay_time = []
for page in range(1, len(all_pages)+1):
    tables = tabula.read_pdf(pdf_path_all, pages=page, multiple_tables=True)
    if page == 1:
        df = pd.concat(tables, ignore_index=True)
        #remove the first 12 rows
        df = df.iloc[12:]
        df.columns = df.iloc[0]
        df = df[1:]
        df = df.drop(['R D Record No.', 'Last name, First name','Planned', 'Time Speciality',], axis=1)
        dfs.append(df)

    if page != 1:
         if isinstance(tables[0], pd.DataFrame):
            # removes all the columns with no values in them
            tables[0] = tables[0].dropna(axis=1, how='all')
            #remove the first row
            tables[0] = tables[0].drop(index=range(1, 2))
            tables[0] = tables[0][1:]
            dfs.append(tables[0])



# Concatenate the data frames into a single data frame
df = pd.concat(dfs, ignore_index=True)
# Save the resulting data frame to a CSV file
#print(df.columns.values)
df.drop(["St. Mary's Hospital Center","Unnamed: 0","Unnamed: 3","Date:"], axis=1, inplace=True)


# remove rows with all null values
df = df.dropna(how='all')

# replace NaN values with empty strings
df = df.fillna('')
df['Procedure, localization, technique'] = df['Procedure, localization, technique'].astype(str) + df['Unnamed: 1'].astype(str)
df['Surgeon'] = df['Surgeon'].astype(str) + df['Unnamed: 2'].astype(str)

#Beware of this as the time changes
df['Entered'] = df['Entered'].astype(str) + df['2023-04-30'].astype(str)
df['Delay'] = df['Delay'].astype(str) + df['Unnamed: 5'].astype(str)


df = df.drop(['Unnamed: 1', 'Unnamed: 2','2023-04-30', 'Unnamed: 5',], axis=1)

df = df.drop(df.columns[1], axis=1)

df['Procedure, localization, technique'] = df['Procedure, localization, technique'].str.split(',').str[0]
df = df.rename(columns={'Procedure, localization, technique': 'Procedure'})


# convert the 'date' column to datetime format
df['Entered'] = pd.to_datetime(df['Entered'])

# this month and day last year
current_year = datetime.datetime.now().year - 1
current_month = datetime.datetime.now().month
current_day = datetime.datetime.now().day
current_time_str = datetime.datetime(current_year, current_month, current_day).strftime('%Y-%m-%d')

print('1 year ago is: ',current_time_str)

# filter the dataframe to only include dates after 1 year ago
filtered_df = df[df['Entered'] > current_time_str]

#print(df.columns.values)
df.to_csv('./output_5.csv', index=False)
#----------------------DONE formatting the data-----------------------------------------

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = UserInterface(filtered_df)
    win.show()
    sys.exit(app.exec_())



