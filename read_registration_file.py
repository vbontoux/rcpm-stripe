
import config
from openpyxl import load_workbook


def read_race_registration_excel_file(filepath):
  #Selecting specific sheet
  wb = load_workbook(filepath)
  sheet = wb.worksheets[3]
  return sheet

sheet = read_race_registration_excel_file(filepath=config.excel_file_path)

#reading multiple cell
emails_column = sheet['D']
amounts_column = sheet['K']
combined_columns = []
for i, e in emails_column:
  print(e.value)
for a in amounts_column:
  print(a.value)

