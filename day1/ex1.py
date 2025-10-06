from openpyxl import Workbook, load_workbook

# pip install openpyxl

wb = Workbook()  # tworzy szablon pliku excel
ws = wb.active  # ustawia aktywny arkusz

# komórka A1 w arkuszu
ws['A1'] = 42
ws['A1'] = 43
ws.append([1, 2, 3])  # lista int
ws.append([4, 5, 6])  # lista int

# zapisanie danych do pliku excel
wb.save('sample.xlsx')
wb.close()
