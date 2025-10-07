import openpyxl

from openpyxl.styles import Font, colors, PatternFill, Border, Side
from openpyxl.formatting.rule import CellIsRule

# wb = openpyxl.load_workbook('video2.xlsx')
wb = openpyxl.load_workbook('video3.xlsx')
ws = wb.active

print(ws.title)  # vgsales

ws = wb['Video Games Sales Data']