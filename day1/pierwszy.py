# https://peps.python.org/pep-0008/
# ctrl alt l - formatowanie kodu
# snake_case
import sys

print()  # wypisz/wydrukuj
print("Radek")  # Radek
print('Radek')

# ctrl / - komentarz kodu
# print('Radek")
#   File "C:\Users\Szkolenie\PycharmProjects\PythonProjectExcel-6-10-2025\day1\pierwszy.py", line 8
#     print('Radek")
#           ^
# SyntaxError: unterminated string literal (detected at line 8)
#
# Process finished with exit code 1

print("Dalsza część programu")

print(type("Radek"))  # <class 'str'>, tekstowy

print(45)
print(type(45))  # <class 'int'>, liczby całkowite

print(sys.int_info)
# sys.int_info(bits_per_digit=30,
#              sizeof_digit=4, default_max_str_digits=4300,
#              str_digits_check_threshold=640)

print("34" + "19")  # 3419, konkatenacja, łączenie stringow
print(34 + 19)  # 53
# print("34" + 19) # TypeError: can only concatenate str (not "int") to str

print(34 * "168")
# 168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168
print(10 * "_")  # __________

# liczby zmiennoprzecinkowe
print(4.56)  # float
print(type(4.56))  # <class 'float'>
print(sys.float_info)  # informacja o zakresie liczb
# sys.float_info(max=1.7976931348623157e+308, max_exp=1024,
#                max_10_exp=308, min=2.2250738585072014e-308, min_exp=-1021,
#                min_10_exp=-307, dig=15, mant_dig=53, epsilon=2.220446049250313e-16,
#                radix=2, rounds=1)

# błąd zaokrąglenia
print(0.1 + 0.2)  # 0.30000000000000004
print(0.1 + 0.9)  # 1.0
# decimal - pozwala ominąć problem zaokrąglenia

# zmienna - pudełko na dane
# typowanie dynmiczne
name = "Radek"
print(name)  # Radek
name = 90
print(name)  # 90

# rzutowanie (zamiana) typów
a = "1"
b = 0
# print(a + b) # TypeError: can only concatenate str (not "int") to str
# int() - rzutowanie na całkowite
print(int(a) + b)  # 1
print(int(a) + int(b))  # 1

tekst = "Witaj Świecie"
print(type(tekst))  # <class 'str'>

#  teksty są niemutowalne
tekst.upper()
print(tekst)  # Witaj Świecie
""" Return a copy of the string converted to uppercase. """
print(tekst.upper())  # WITAJ ŚWIECIE
nowy_tekst = tekst.upper()
print(nowy_tekst) # WITAJ ŚWIECIE


