import openpyxl

filename = 'video2.xlsx'

wb = openpyxl.load_workbook(filename)
ws = wb['vgsales']

ws['P1'] = 'Averages Sales'
ws['P2'] = '=AVERAGE(K2:K16328)'

wb.save('video2.xlsx')
wb.close()

ws['Q1'] = "Number of populated cells"
ws['Q2'] = "=COUNTA(E2:E16328)"

wb.save('video2.xlsx')
wb.close()

ws['S1'] = "Total Sports Sales"
ws['S2'] = '=COUNTIF(E2:E16328, "sports")'

wb.save('video2.xlsx')
wb.close()

print(ws['S2'].value)  # wypisze formułe

ws['T1'] = "Total sum of sports sales"
ws['T2'] = '=SUMIF(E2:E16328, "Sports", K2:K16328)'

wb.save('video2.xlsx')
wb.close()

ws['U1'] = "Rounded sum of Sports Sales"
ws['U2'] = '=CEILING(T2, 25)'

wb.save('video2.xlsx')
wb.close()
