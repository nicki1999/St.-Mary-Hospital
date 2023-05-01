import os
import pandas as pd
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt

# clear the terminal
os.system('cls' if os.name == 'nt' else 'clear')
df = pd.read_csv('output_3.csv',nrows=1395,usecols=['Procedure, localization, technique', 'Surgeon', 'Delay'])
df['Procedure, localization, technique'] = df['Procedure, localization, technique'].str.split(',').str[0]
df = df.rename(columns={'Procedure, localization, technique': 'Procedure'})
# Create a new dataframe with only the rows that contain 'Jennifer'
df_jennifer = df[df['Surgeon'] == 'Dimentberg R']
print(df_jennifer)
df_jennifer_procedure_total_hip = df_jennifer[df_jennifer['Procedure'].str.contains('Total hip')]
df_jennifer_procedure_total_knee = df_jennifer[df_jennifer['Procedure'].str.contains('Total knee')]
df_jennifer_procedure_total_shoulder = df_jennifer[df_jennifer['Procedure'].str.contains('Total shoulder')]

# Output the new dataframe Jennifer Mutch
jennifer_total_shoulder_count = len(df_jennifer_procedure_total_shoulder)
jennifer_total_knee_count = len(df_jennifer_procedure_total_knee)
jennifer_total_hip_count = len(df_jennifer_procedure_total_hip)
count = 0
for delay in df_jennifer_procedure_total_shoulder['Delay'].values:
    if delay>=180:
        count+=1

jennifer_knee_count = 0
for delay in df_jennifer_procedure_total_knee['Delay'].values:
    #print(delay)
    if delay>=180.0:
        jennifer_knee_count = jennifer_knee_count + 1

jennifer_hip_count = 0
for delay in df_jennifer_procedure_total_hip['Delay'].values:
    #print(delay)
    if delay>=180.0:
        jennifer_hip_count = jennifer_hip_count + 1
        #print('for delay:' ,delay,'jennifer_hip_count:',jennifer_hip_count)


#print('total hip',jennifer_total_hip_count) 
#print('More_6 months_hip',jennifer_hip_count) 
#print(df_jennifer_procedure_total_hip['Delay'].values)

#UI

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Table Example')
        self.setGeometry(100, 100, 500, 300)

        # Create a table
        table = QTableWidget(self)
        table.setGeometry(50, 50, 1800, 900)
        table.setRowCount(3)
        table.setColumnCount(9)
        table.setHorizontalHeaderLabels(["Total", "More than 6 months", "Percentage"])


        if  jennifer_total_shoulder_count == 0:
                total_shoulder_percentage =0
        else:
            total_shoulder_percentage = count/jennifer_total_shoulder_count

        # Add some sample data to the table
        data = [["Alice", "25", "New York"],
                ["Bob", "30", "London"],
                [str(jennifer_total_shoulder_count), str(count), str("{:.2f}".format((total_shoulder_percentage)*100)),
                 str(jennifer_total_knee_count),str(jennifer_knee_count),str("{:.2f}".format((jennifer_knee_count/jennifer_total_knee_count)*100)),
                 str(jennifer_total_hip_count),str(jennifer_hip_count),str("{:.2f}".format((jennifer_hip_count/jennifer_total_hip_count)*100))]]
        for i, row in enumerate(data):
            for j, item in enumerate(row):
                table.setItem(i, j, QTableWidgetItem(item))
                # Add new cells on top
        header_cell1 = QTableWidgetItem("Dimentberg R")
        header_cell1.setTextAlignment(Qt.AlignCenter)
        table.setItem(0, 0, header_cell1)
        table.setSpan(0, 0, 1, table.columnCount())  # span the cell across all columns

        header_cell2 = QTableWidgetItem("Total Shoulder                                                           | Total Knee |                                                             Total Hip")
        header_cell2.setTextAlignment(Qt.AlignCenter)
        table.setItem(1, 0, header_cell2)
        table.setSpan(1, 0, 1, table.columnCount())  # span the cell across all columns

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

