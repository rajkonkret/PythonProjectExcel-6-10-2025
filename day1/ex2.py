import openpyxl

wb = openpyxl.load_workbook("../data/videogamesales.xlsx")
ws = wb.active

print(wb)  # <openpyxl.workbook.workbook.Workbook object at 0x0000017BB778D550>
print(ws)  # <Worksheet "vgsales">

ws = wb['vgsales']

print("Total number of rows:", ws.max_row)  # Total numbers of rows: 16328
print("Total number of columns:", ws.max_column)  # Total number of columns: 10
