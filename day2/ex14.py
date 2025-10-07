import pandas as pd

df = pd.DataFrame({
    "Imie": ['Jan', "Anna", "Tomek"],
    "Wiek": [29, 24, 35],
    "Miasto": ['Warszawa', "Wrocław", "Legnica"]
})

# kontekst menadżer
with pd.ExcelWriter("Tabela.xlsx", engine='xlsxwriter') as writer:
    df.to_excel(writer, sheet_name="Osoby", startrow=1, header=False, index=False)

    workbook = writer.book
    worksheet = writer.sheets['Osoby']

    header_format = workbook.add_format({
        'bold': True,
        'text_wrap': True,
        'valign': 'vcenter',
        'bg_color': '#D7E4BC',
        'border': 1
    })
