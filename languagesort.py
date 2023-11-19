import pandas as pd
from langdetect import detect_langs
import xlrd

df = pd.read_excel("/home/relaxyourefine/Documents/PythonProjects/POEC/2023_working_manual_8-28-2023 (2.1).xlsm")

def highlight_cells():

    return['background-color: yellow']

df.style.apply(highlight_cells)
print(df.head())
