'''constants.py'''

from pathlib import Path
from enum import Enum


# Resultat dokumenter
RESULTAT_DOKUMENTER = Path(r'\\norconsultad.com\dfs\nor\oppdrag\Sandvika\521\07\52107174\4 Resultatdokumenter\45 Kontrollobjekt')

# Dokumentleveranseliste
DOKUMENTLEVERANSELISTE = Path(r'C:\Users\thooes\Norconsult Group\52107174 - Rv 555 Sotrasambandet - Documents\145 Dokumentleveranseplan\RA-ADM-003 Document Deliverable list Execution Phase.xlsx')
LEVERANSE_SHEET = 'Leveransepakker'
COLUMN_DOK_KODE = 'Dokumentkode'
COLUMN_DOK_TYPE = 'Dokumenttype'
COLUMN_OBS = 'Kontrollobjekt'


# Tillate dokumenttypes for leveransepakker
class DocumentTypes(Enum):
    RAPPORT = '.txt'
    TEGNING = '.txt'
    MODELL = '.modell'
    STIKNING = '.stikning'
    ZIP = '.ZIPmodell'

