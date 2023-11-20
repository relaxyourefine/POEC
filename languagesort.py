import pandas as pd
from langdetect import detect
import xlrd
import xlsxwriter


df = pd.read_excel("/home/relaxyourefine/Documents/PythonProjects/POEC/2023_working_manual_8-28-2023 (2.1).xlsm")

def highlight_cells(value):
    if detect(str(value)) != 'en':
        print("yes")
        return 'background-color: yellow'
    else:
        return 'background-color: white'

styled_df = df.style.applymap(highlight_cells, subset=['abstract'])

writer = pd.ExcelWriter('Ver2.xlsx')
styled_df.to_excel(writer)
writer.save()
