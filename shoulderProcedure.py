class ShoulderProcedure:
    def __init__(self,filtered_df):
        self.filtered_df = filtered_df
        super().__init__()
    procedure_total_shoulder = surgeon_df[surgeon_df['Procedure'].str.contains('Total shoulder')]
    procedure_total_shoulder_count = len(procedure_total_shoulder)
    table.setItem(2, 0, QTableWidgetItem(str(procedure_total_shoulder_count)))
    for delay in procedure_total_shoulder['Delay'].values:
    if float(delay) >= 180:
    print('this is delay: ',filtered_df['Delay'])
    procedure_delay_shoulder_count+=1
    table.setItem(2, 1, QTableWidgetItem(str(procedure_delay_shoulder_count)))
    table.setItem(2, 2, QTableWidgetItem(str("{:.2f}".format((procedure_delay_shoulder_count/procedure_total_shoulder_count)))))