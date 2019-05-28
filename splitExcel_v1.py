import pandas
import xlrd
from openpyxl import load_workbook


filenameInput = input("Enter Excel File name with path :")
sheetName = input("Enter the sheet name :")


account = pandas.read_excel(filenameInput, sheet_name=sheetName)

contractNumberUnique = account['Contract Number'].unique().tolist()

for i in contractNumberUnique:
    accountSubset = account[account['Contract Number'] == i]
    filename = filenameInput[0:filenameInput.rfind('\\')+1] + "Activity_" + str(i) + ".xlsx"
    writer = pandas.ExcelWriter(filename,engine='openpyxl')
    accountSubset.to_excel(writer,sheetName,startrow=0,startcol=0,index=False)
    writer.save()
