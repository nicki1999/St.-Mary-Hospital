import tabula
import os
import pandas as pd

# clear the terminal
os.system('cls' if os.name == 'nt' else 'clear')

pdf_path = './service_orthopedics_specialty_orthopedics-1.pdf'

#tabula.convert_into(pdf_path,'output_2', output_format='csv', pages='all')

tables = tabula.read_pdf(pdf_path, pages=1, multiple_tables=True,)

name_col = tables[0]

df = name_col.iloc[12:]
df.columns = df.iloc[0]
df = df[1:]

# Reset the index
#df = df.reset_index(drop=True)

print('this is name_col',name_col,'ends here.')
print(df['Delay'])
#print(name_col.keys())
#print(name_col.iloc[1, 1])





