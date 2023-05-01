import tabula
import os
import pandas as pd
import numpy as np

# clear the terminal
os.system('cls' if os.name == 'nt' else 'clear')

#for the 1st page of the report
pdf_path = './service_orthopedics_specialty_orthopedics-1.pdf'

#for all pages of the report
pdf_path_all = './2022-04-30_onwards_record.pdf'

pdf_path_2pages = './service_orthopedics_specialty_orthopedics-2.pdf'
# Create an empty list to store the data frames for each page
dfs = []

# Iterate over each page of the PDF and append the data frame to the list
delay_time = []
for page in range(1, len(tabula.read_pdf(pdf_path_all, pages='all'))+1):
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

# filter the dataframe to only include dates after 2022-01-02
filtered_df = df[df['Entered'] > '2022-04-30']
print(len(filtered_df))


#print(df.columns.values)
#df.to_csv('./output_5.csv', index=False)





