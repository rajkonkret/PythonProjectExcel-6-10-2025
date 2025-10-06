import openpyxl

wb = openpyxl.load_workbook("../data/videogamesales.xlsx")
ws = wb.active

print(wb)  # <openpyxl.workbook.workbook.Workbook object at 0x0000017BB778D550>
print(ws)  # <Worksheet "vgsales">

ws = wb['vgsales']

print("Total number of rows:", ws.max_row)  # Total numbers of rows: 16328
print("Total number of columns:", ws.max_column)  # Total number of columns: 10

print("Value un cell A1 is:", ws['A1'].value)  # Value un cell A1 is: Rank

# wczytanie wszystkich kolumn z wiersza 1
# +1 - excel numeruje od 1, python od 0
# list comprehensions
value = [ws.cell(row=1, column=i).value for i in range(1, ws.max_column + 1)]
print(value)

# ['Rank', 'Name', 'Platform', 'Year', 'Genre', 'Publisher', 'NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']

# dane z kolumny 2
data = [ws.cell(row=i, column=2).value for i in range(2, 12)]  # od 2 do 11
print(data)
# ['Wii Sports',
#  'Super Mario Bros.',
#  'Mario Kart Wii',
#  'Wii Sports Resort',
#  'Pokemon Red/Pokemon Blue',
#  'Tetris',
#  'New Super Mario Bros.',
#  'Wii Play',
#  'New Super Mario Bros. Wii',
#  'Duck Hunt']
