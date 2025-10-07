import pandas as pd

height_data = [
    {"Name": "Adiya", "Height": 179},
    {"Name": "Samen", "Height": 181},
    {"Name": "Darek", "Height": 170},
    {"Name": "Jhon", "Height": 167},
]

weight_data = [
    {"Name": "Adiya", "Weight": 79},
    {"Name": "Samen", "Weight": 81},
    {"Name": "Darek", "Weight": 70},
    {"Name": "Jhon", "Weight": 67},
]

marks_data = [
    {"Name": "Adiya", "Marks": 179},
    {"Name": "Samen", "Marks": 181},
    {"Name": "Darek", "Marks": 170},
    {"Name": "Jhon", "Marks": 167},
]

height_data_df = pd.DataFrame(height_data)
weight_data_df = pd.DataFrame(weight_data)
marks_data_df = pd.DataFrame(marks_data)

writer = pd.ExcelWriter("excel_with_multiple_sheets.xlsx", engine='xlsxwriter')

height_data_df.to_excel(writer, sheet_name="height", index=False)
weight_data_df.to_excel(writer, sheet_name="weight", index=False)
marks_data_df.to_excel(writer, sheet_name="marks", index=False)

writer.close()
