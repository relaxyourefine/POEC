import pandas as pd
from langdetect import detect
import xlrd


df = pd.read_excel("/home/relaxyourefine/Documents/PythonProjects/POEC/2023_working_manual_8-28-2023 (2.1).xlsm")


def highlight_cells():
    abstracts = df["abstract"]
    for abstract in abstracts:
        if detect(abstract) == 'en':
            return['background-color yellow']
        else:
            return

df.style.apply(highlight_cells)
