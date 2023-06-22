import openpyxl
from openpyxl import workbook
from openpyxl import worksheet
wb = openpyxl.load_workbook("example1.xlsx")
sheet = wb.active
sheet.insert_cols(2)
#sheet.move_range("B1:B1",rows=0,cols=2)
wb.save("example1.xlsx")