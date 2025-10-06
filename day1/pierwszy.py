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
print(nowy_tekst)  # WITAJ ŚWIECIE

zmienna1 = "GROSS"
zmienna2 = "groẞ"

print(zmienna1.lower() == zmienna2.lower())  # , == porównanie, False - fałsz
print(zmienna1.casefold() == zmienna2.casefold())  # True

# typ logiczny, True, False
print(1 != 0)  # różne, True

name = "Radek"
# f - f-string, string sformatowany
print(f"Nazywam się: {name}")  # Nazywam się: Radek

a = 4.567
print(f"Liczba {a}")  # Liczba 4.567
# ctrl d - powielanie linii
print(f"Liczba {a:.2f}")  # Liczba 4.57

print("Liczba:", a)  # Liczba: 4.567

# f - float
print("Liczba: %f" % a)  # Liczba: 4.567000
print("Liczba: %.2f" % a)  # Liczba: 4.57
# print("Liczba: %f" % "Radek")  # TypeError: must be real number, not str

print("""
Tekst
    wielolinijkowe""")

# "Tekst
#     wielolinijkowe"

"""Komentarz
wielolinijkowy - dokumentacja"""

print(100 / 3)  # 33.333333333333336
print(100 // 3)  # 33, cześć całkowita z dzielenia
print(100 % 3)  # 1, modulo, reszta z dzielenia
print(10 % 3)  # reszta 1

zysk = 890123456987
print(f"Nasza duża liczba: {zysk:,}")  # Nasza duża liczba: 890,123,456,987
print(f"Nasza duża liczba: {zysk:_}")  # Nasza duża liczba: 890_123_456_987
print(f"Nasza duża liczba: {zysk:_}".replace("_", "."))  # Nasza duża liczba: 890.123.456.987

liczba = 150_000_000_000
print(liczba)  # 150000000000
print(type(liczba))  # <class 'int'>

# kolekcje
# lista - przechowuje elementy z zachowaniem kolejności
lista = [1, 2, 3, 5, 6, "Radek"]
print(type(lista))  # <class 'list'>
print(lista)  # [1, 2, 3, 5, 6, 'Radek']

lista = []  # pusta lista
lista.append("Radek")  # dodanie elementów do listy
lista.append("Tomek")
lista.append("Zenek")
lista.append("Klaudia")
lista.append("Maciej")
print(lista)  # ['Radek', 'Tomek', 'Zenek', 'Klaudia', 'Maciej']

# usunięcie
lista.remove("Radek")
print(lista)  # ['Tomek', 'Zenek', 'Klaudia', 'Maciej']

lista_copy = lista.copy()
lista_k = lista  # kopia adresu, referencji
print(lista_k)  # ['Tomek', 'Zenek', 'Klaudia', 'Maciej']
print(lista)  # ['Tomek', 'Zenek', 'Klaudia', 'Maciej']
lista.clear()  # usunięcie wszystkich elementów z listy
print(lista_k)  # []
print(lista)  # []
print(lista_copy)  # ['Tomek', 'Zenek', 'Klaudia', 'Maciej']

# krotka (tupla) - kolekcja niemutowalna, do odczytu
# pozwala lepiej zarządzać pamiecią
krotka = tuple(lista_copy)
print(type(krotka))  # <class 'tuple'>
print(krotka)  # ('Tomek', 'Zenek', 'Klaudia', 'Maciej')
tupla1 = "Radek", "Tomek"
print(type(tupla1))  # <class 'tuple'>

# zbiór - set
# przechowuje unikalne elementy, nie zachowuje kolejności
lista = [2, 5, 6, 8, 6, 7, 8, 5, 9]
zbior = set(lista)
print(zbior)  # {2, 5, 6, 7, 8, 9}
print(type(zbior))  # <class 'set'>
pusty_zbior = set()
pusty_zbior.add(15)
print(pusty_zbior)  # {15}

# słownik - klucz - wartość
slownik = {'name': "Radek", 'ag': 56}
print(slownik)  # {'name': 'Radek', 'ag': 56}
print(type(slownik))  # <class 'dict'>

print(slownik.keys())
print(slownik.values())
print(slownik.items())
# dict_keys(['name', 'ag'])
# dict_values(['Radek', 56])
# dict_items([('name', 'Radek'), ('ag', 56)])
