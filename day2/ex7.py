import openpyxl
from openpyxl.chart import Reference, BarChart
from openpyxl.chart.axis import ChartLines

wb = openpyxl.load_workbook('video2.xlsx')
ws = wb['Total Sales by Genre']


