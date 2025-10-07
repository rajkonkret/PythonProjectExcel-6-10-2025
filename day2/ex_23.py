# konwersja plików przy pomocy pyexcel
# pip install pyexcel-csv - w nowszych wersjach niepotrzebne
import pyexcel as pe

pe.save_book_as(file_name='wyniki.xlsx',
                dest_file_name='wyniki.csv')
