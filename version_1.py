import tabula
import os
import pandas as pd

# clear the terminal
os.system('cls' if os.name == 'nt' else 'clear')

pdf_path = './service_orthopedics_specialty_orthopedics-1.pdf'

#tabula.convert_into(pdf_path,'output_2', output_format='csv', pages='all')

tables = tabula.read_pdf(pdf_path, pages=1, multiple_tables=True)

name_col = tables[0]
print(name_col)





