import pandas as pd
from pathlib import Path, os

def get_datas_dir() -> Path:
    current_path = Path(__file__).resolve().parent

    while current_path != current_path.root:
        datas_path = current_path / "datas"
        if datas_path.exists() and datas_path.is_dir():
            return datas_path
        current_path = current_path.parent

    raise FileNotFoundError('Dir "datas" not found.')

def import_csv(file: str) -> pd.DataFrame:
    """
    Read the data.csv file and return a pandas DataFrame with the data.
    
    Returns:
        pd.DataFrame: The data in the data.csv file.
    """
    datas_dir = get_datas_dir()
    files_way = datas_dir / file

    data = pd.read_csv(files_way)
    return data

def import_xlsx(file: str) -> pd.DataFrame:
    """
    Read the file.xlsx file and return a pandas DataFrame with the data.
    
    Returns:
        pd.DataFrame: The data in the file.xlsx file.
    """
    datas_dir = get_datas_dir()
    files_way = datas_dir / file

    data = pd.read_excel(files_way)
    return data