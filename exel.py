import sqlite3
from xlsxwriter.workbook import Workbook

def all_B(bot,message):
    conn = sqlite3.connect('database.sqlite')
    cur = conn.cursor()

    cur.execute('SELECT  *  FROM users')
    results = cur.fetchall()
    workbook = Workbook('Output.xlsx')
    worksheet = workbook.add_worksheet()
    conn = sqlite3.connect('database.sqlite')
    c = conn.cursor()
    mysel = c.execute(f"select * from users")
    worksheet.set_column('A:A', 3)
    worksheet.set_column('B:C', 25)
    worksheet.set_column('D:D', 9)
    worksheet.set_column('E:F', 40)
    format1 = workbook.add_format({'border': 1})
    worksheet.write(0, 0, "№", format1)
    worksheet.write(0, 1, "ФИО", format1)
    worksheet.write(0, 2, "Задача", format1)
    worksheet.write(0, 3, "Срок исполнения", format1)
    worksheet.write(0, 4, "Описание", format1)
    for i, row in enumerate(mysel):
        worksheet.write(i + 1, 0, row[0], format1)
        worksheet.write(i + 1, 1, row[1], format1)
        worksheet.write(i + 1, 2, row[2], format1)
        worksheet.write(i + 1, 3, row[3], format1)
        worksheet.write(i + 1, 4, row[4], format1)
    workbook.close()
    file_path = 'Output.xlsx'
    with open(file_path, 'rb') as file:
        bot.send_document(message, file)
    cur.close()
    conn.close()