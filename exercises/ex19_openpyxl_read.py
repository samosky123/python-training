from openpyxl import *
wb = load_workbook('arp_table.xlsx')
ws = wb.active
rows_gen = ws.rows
rows = list(rows_gen)

for row in rows:
    print("MAC:", row[0].value)
    print("IP:", row[1].value)
    print("AGE:", row[2].value)
    print("\n")

