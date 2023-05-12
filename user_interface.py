from PyQt5.QtWidgets import  QMainWindow, QTableWidget, QTableWidgetItem, QComboBox, QLabel
from PyQt5.QtCore import Qt
import os

#user_input = input("Enter your name: ")

surgeon_value = ''

class UserInterface(QMainWindow):

    def __init__(self,filtered_df):
        self.filtered_df = filtered_df
        super().__init__()
        self.setWindowTitle('Table Example')
        self.setGeometry(100, 100, 500, 300)
    
        # Create a table
        table = QTableWidget(self)
        table.setGeometry(50, 50, 1800, 900)
        table.setRowCount(3)
        table.setColumnCount(9)
        table.setHorizontalHeaderLabels(["Total", "More than 6 months", "Percentage"])

        # Add some sample data to the table
        data = [["Alice", "25", "New York"],
                ["Bob", "30", "London"],
                ['0', "0", "0",
                "Alice", "25", "New York",
                "Alice", "25", "New York"]]
        for i, row in enumerate(data):
            for j, item in enumerate(row):
                table.setItem(i, j, QTableWidgetItem(item))
        

        

        # Add a dropdown to the window
        dropdown = QComboBox(self)
        dropdown.addItem("Choose a surgeon")
        dropdown.addItem("Albers, Anthony")
        dropdown.addItem("Dimentberg R")
        dropdown.addItem("Stephenson P")
        dropdown.addItem("Mutch, Jennifer")
        dropdown.addItem("Haydon, C")
        dropdown.addItem("Martinez, Adriana")
        dropdown.move(300, 20)
        dropdown.view().setMinimumWidth(200)
        dropdown.setFixedWidth(200)


        # Function to be called when the user selects an option from the dropdown
        def on_select(index):
            global surgeon_value
            
            selected_option = dropdown.itemText(index)
            print("Selected option:", selected_option)
            surgeon_value = selected_option
            #update the value of the surgeon text
            header_cell1.setText(surgeon_value)
            surgeon_df = filtered_df[filtered_df['Surgeon'] == surgeon_value]
            if not os.path.isfile(f'./individual_surgeons/{surgeon_value}.csv'):
                surgeon_df.to_csv(f'./individual_surgeons/{surgeon_value}.csv', index=False)


            #This is shoulder procedure
            procedure(surgeon_df,'Total shoulder')
            #Shoulder procedure ends here

            #This is knee procedure
            procedure(surgeon_df,'Total knee')
            #knee procedure ends here

            #This is hip procedure
            procedure(surgeon_df,'Total hip')
            #hip procedure ends here

        # Connect the dropdown to the on_select function
        dropdown.activated.connect(on_select)

        # Add new cells on top
        header_cell1 = QTableWidgetItem(surgeon_value)
        header_cell1.setTextAlignment(Qt.AlignCenter)
        table.setItem(0, 0, header_cell1)
        table.setSpan(0, 0, 1, table.columnCount())  # span the cell across all columns

        header_cell2 = QTableWidgetItem("Total Shoulder                                                           | Total Knee |                                                             Total Hip")
        header_cell2.setTextAlignment(Qt.AlignCenter)
        table.setItem(1, 0, header_cell2)
        table.setSpan(1, 0, 1, table.columnCount())  # span the cell across all columns


        def procedure(surgeon_df,procedure_type):
            #Total shoulder procedure
            procedure_delay_count = 0
            if procedure_type == 'Total shoulder':
                table_index = 0
            if procedure_type == 'Total knee':
                table_index = 3
            if procedure_type == 'Total hip':
                table_index = 6
            procedure_total = surgeon_df[surgeon_df['Procedure'].str.contains(procedure_type)]
            procedure_total_count = len(procedure_total)
            table.setItem(2, table_index, QTableWidgetItem(str(procedure_total_count)))
            for delay in procedure_total['Delay'].values:
                if float(delay) >= 180:
                    print('this is delay: ',filtered_df['Delay'])
                    procedure_delay_count+=1
            table.setItem(2, table_index+1, QTableWidgetItem(str(procedure_delay_count)))
            if  procedure_total_count == 0:
                total_percentage =0
            else:
                total_percentage = procedure_delay_count/procedure_total_count
            table.setItem(2, table_index+2, QTableWidgetItem(str("{:.2f}".format(total_percentage))))
