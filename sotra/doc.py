'''doc.py

Methods for updating and maintaining the document delivery list
'''

import pandas as pd
from pathlib import Path
import json
from datetime import datetime, date

from sotra import constants as c
from sotra import helpers



def _get_data() -> pd.DataFrame:
    """This function returns all rows where the column "Kontrollobjekt" is equal to obs.

    Parameters:
    df (pd.DataFrame): The DataFrame to filter.
    obs (str): The value to match in the "Kontrollobjekt" column.

    Returns:
    pd.DataFrame: A DataFrame containing only the rows where "Kontrollobjekt" is equal to obs.
    """
    excel = c.DOKUMENTLEVERANSELISTE
    sheet = c.MODELL
    df = helpers.open_excel_to_dataframe(excel, sheet)
    return df

def _get_json() -> dict:
    with open(c.LOG, 'r', encoding='utf-8') as f:
        return json.load(f)


def _latest_revision(revisions: list) -> str:
    revs = []
    if len(revisions) == 0:
        return ""
    for rev in revisions:
        if rev not in ['Missing', 'NA', 'None']:
            revs.append(rev)
    return str(max(revs))

def _latest_revision_date(revisions: list) -> str:
    dates = []
    if len(revisions) == 0:
        return ""
    for rev_date in revisions:
        if rev_date in ['Missing', 'NA', 'None', '-']:
            continue
        try:
            date = datetime.strptime(rev_date, '%Y.%m.%d')
        except:
            pass
        try: 
            date = datetime.strptime(rev_date, '%Y-%m-%d')
        except:
            pass
            
        dates.append(date)
    return max(dates).strftime('%Y-%m-%d')


def get_log_value(log: dict, prop: str) -> str: 
    value = ""
    if 'KeyProperties' in log:
        log_item_keys = log['KeyProperties']
        if prop in log_item_keys:
            value = log_item_keys[prop]
    return value


def get_log_rev(log: dict) -> str: 
    prop = 'GEN-B07_Revisjonsindeks_Element-revision'
    values = []
    if 'KeyProperties' in log:
        log_item_keys = log['KeyProperties']
        if prop in log_item_keys:
            values.extend(list(log_item_keys[prop].keys()))
    value = _latest_revision(values)
    return value


def get_log_rev_date(log: dict) -> str: 
    prop = 'GEN-B08_Revisjonsdato_Revision-date'
    values = []
    if 'KeyProperties' in log:
        log_item_keys = log['KeyProperties']
        if prop in log_item_keys:
            values.extend(list(log_item_keys[prop].keys()))
    value = _latest_revision_date(values)
    return value


def format_data(df: pd.DataFrame, d: dict) -> pd.DataFrame:
    """

    Parameters:

    Returns:
    """
    columns = [c.MODEL_DOCUMENT_CODE, c.MODEL_REVISION, c.MODEL_REVISION_DATE]
    new_df = df[columns].copy()

    new_revs = []
    new_dates = []

    fagmodeller = d['02 Fagmodeller']

    for _, row in new_df.iterrows():
        name = row[c.MODEL_DOCUMENT_CODE]
        log_name = f'{name}.ifc'
        old_rev = row[c.MODEL_REVISION]

        try:
            old_date = datetime.strptime(row[c.MODEL_REVISION_DATE], '%Y-%m-%d')
            old_date = date.strftime(old_date, '%Y-%m-%d')
        except:
            old_date = row[c.MODEL_REVISION_DATE]

        new_rev = ""
        new_date = ""

        if log_name in fagmodeller:
            log_item = fagmodeller[log_name]
            new_rev = get_log_rev(log_item)
            if new_rev == "":
                new_rev = old_rev
            
            new_date = get_log_rev_date(log_item)
            if new_date == "":
                new_date = old_date

        new_revs.append(new_rev)
        new_dates.append(new_date)
    
    new_df[c.MODEL_NEW_REV] = new_revs
    new_df[c.MODEL_NEW_REV_DATE] = new_dates
    return new_df


def update_revisions():
    df = _get_data()
    jf = _get_json()
    new_df = format_data(df, jf)
    new_df.to_excel('sotra-build_output.xlsx', index=False)


if __name__ == "__main__":
    pass


