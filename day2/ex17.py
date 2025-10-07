import pandas as pd

df = pd.read_excel("excel_with_multiple_sheets.xlsx", sheet_name=2)
print("The dataframe is:")
print(df)
# The dataframe is:
#     Name  Marks
# 0  Adiya    179
# 1  Samen    181
# 2  Darek    170
# 3   Jhon    167

df = pd.read_excel("excel_with_multiple_sheets.xlsx", sheet_name="marks")
print("The dataframe is:")
print(df)
# The dataframe is:
#     Name  Marks
# 0  Adiya    179
# 1  Samen    181
# 2  Darek    170
# 3   Jhon    167

dane = pd.ExcelFile("excel_with_multiple_sheets.xlsx")
print(dane.sheet_names)  # ['height', 'weight', 'marks']

# wczytanie konkretnej kolumny
df = pd.read_excel("excel_with_multiple_sheets.xlsx", sheet_name="marks", usecols=['Name'])
print("The dataframe is:")
print(df)
# The dataframe is:
#     Name
# 0  Adiya
# 1  Samen
# 2  Darek
# 3   Jhon