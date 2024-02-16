'''obs.py'''

import pandas as pd
import shutil
from pathlib import Path


from sotra import constants as c
from sotra import helpers


def obs_to_txt(obs: str, dest: str) -> None:
    '''Creates files for every document or model connected to the OBS
    
    Args:
        obs: Control object number (Example: 08.02.10.02)
        dest: Destination folder where the files are created

    Returns:
        None
    '''
    dataframe = get_data(obs)
    make_files(dataframe, dest)
    print("Done")


def archive(src_dir: str, date: str, obs: str) -> None:
    '''Archive the OBS control object to RESULTAT_DOKUMENT with date folder
    
    Args:
        src_dir: Source directory (Example: C:/foo/bar)
        date: Date for archive folder (Format: yyyy-mm-dd)
        obs: Control object number (Example: 08.02.10.02)
    
    Returns:
        None
    '''
    res_docs = c.RESULTAT_DOKUMENTER
    src = Path(src_dir)
    dst_dir = res_docs / obs / date
    dst_dir.mkdir(parents=True, exist_ok=True)
    for src_file in src.iterdir():
        if src_file.is_file():
            shutil.copy(src_file, dst_dir)



def get_data(obs: str) -> pd.DataFrame:
    """This function returns all rows where the column "Kontrollobjekt" is equal to obs.

    Parameters:
    df (pd.DataFrame): The DataFrame to filter.
    obs (str): The value to match in the "Kontrollobjekt" column.

    Returns:
    pd.DataFrame: A DataFrame containing only the rows where "Kontrollobjekt" is equal to obs.
    """
    excel = c.DOKUMENTLEVERANSELISTE
    sheet = c.LEVERANSE_SHEET
    df = helpers.open_excel_to_dataframe(excel, sheet)
    return df.loc[df[c.COLUMN_OBS].isin(obs)]


def check_files(existing_files: list, src_dir: str) -> list:
    '''Returns list of files in src_dir not in existing_files list
    
    Args:
        existging_files: files already in documentdeliverylist
        src_dir: Directory for delivery

    Returns:
        list: List of files in src_dir not in existing_files
    '''
    src = Path(src_dir)
    res = []
    for file in src.iterdir():
        if file not in existing_files:
            res.append(file)
    return res


def make_files(documents: pd.DataFrame, dir: str) -> None:
    '''Create new empty placeholder files

    Creates empty placeholder files for model document, models, stake-out
    data and zip files. 
    
    Args:
        documents: Table of documents, required columns
            c.COLUMN_DOK_KODE,
            c.COLUMN_DOK_TYPE
        dir: Directory where new files will be added

    Returns:
        None
    '''
    docs = documents[c.COLUMN_DOK_KODE].to_list()
    r = check_files(docs, dir)
    if len(r) > 0:
        print("\n\n!!! NY fil oppdaget. Kontroller og evt legg inn i dokumentleveranselisten:")
        for f in r:
            print('_'*(len(f.name)+8))
            print(f'Ny fil: {f.name}')
            print('-'*(len(f.name)+8))
        print()

    for _, document in documents.iterrows():
        file = document[c.COLUMN_DOK_KODE]
        file_type = str(document[c.COLUMN_DOK_TYPE]).upper()
        match file_type:
            case c.DocumentTypes.RAPPORT.name:
                helpers.make_txt_file(file, dir, c.DocumentTypes.RAPPORT.value)
            case c.DocumentTypes.TEGNING.name:
                helpers.make_txt_file(file, dir, c.DocumentTypes.TEGNING.value)
            case c.DocumentTypes.MODELL.name:
                helpers.make_txt_file(file, dir, c.DocumentTypes.MODELL.value)
            case c.DocumentTypes.STIKNING.name:
                helpers.make_txt_file(file, dir, c.DocumentTypes.STIKNING.value)
            case c.DocumentTypes.ZIP.name:
                helpers.make_txt_file(file, dir, c.DocumentTypes.ZIP.value)
            case _:
                helpers.make_txt_file(file, dir)





if __name__ == "__main__":
    pass
