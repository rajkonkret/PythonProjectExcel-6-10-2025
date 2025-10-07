import xlwings as xw
import pandas as pd
import numpy as np

df = pd.DataFrame(data=np.random.randn(100, 5),
                  columns=[f"Próba {i}" for i in range(1, 6)])

print(df)
print(df.head())  # 5 pierwszych
print(df.tail())  # 5 ostatnich
#      Próba 1   Próba 2   Próba 3   Próba 4   Próba 5
# 95  0.311306 -0.993508  1.065142  0.694060  2.202290
# 96 -0.398089  0.743708  0.066352  0.904160  1.002245
# 97  0.549451 -0.139569  0.494283 -0.518541  0.286365
# 98 -0.070626 -1.355883 -0.837919  0.363560  0.325967
# 99 -2.518122  2.419594  3.554019  1.607917  0.845520

# xw.view(df)

book = xw.Book()
print(book.name)
print(book.sheets)
# Zeszyt2
# Sheets([<Sheet [Zeszyt2]Arkusz1>])

sheet1 = book.sheets[0]
print(sheet1.range('A1'))
# <Range [Zeszyt1]Arkusz1!$A$1>

sheet1.range('A1').value = [[1, 2],
                            [3, 4]]

sheet1.range('A4').value = "Witaj!"

print(sheet1['A1'].value)  # 1.0

print(sheet1["A1:B2"].value)  # [[1.0, 2.0], [3.0, 4.0]]
