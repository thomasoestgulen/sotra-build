'''helpers.py'''

import pandas as pd
from pandas import read_excel
from pathlib import Path
from rich.console import Console

console = Console()


def open_excel_to_dataframe(filepath: str, sheetName: str) -> pd.DataFrame:
    '''Opens excel file returns Pandas.DataFrame'''
    df = read_excel(filepath, sheet_name=sheetName)  # , skiprows=3)
    return df


def make_txt_file(name: str, path: str, ext: str = '.txt') -> None:
    '''Creates a blank file with given path, name and extention'''
    fpath = Path(path)
    file = fpath / f'{name}{ext}'
    file.touch()