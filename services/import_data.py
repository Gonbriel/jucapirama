import pandas as pd
from pathlib import Path

def get_datas_dir() -> Path:
    current_path = Path(__file__).resolve().parent

    while current_path != current_path.root:
        datas_path = current_path / "datas"
        if datas_path.exists() and datas_path.is_dir():
            return datas_path
        current_path = current_path.parent

    raise FileNotFoundError('Dir "datas" not found.')

def import_csv(file: str):
    """
    Reads a CSV file and returns a DataFrame and its string version (CSV format).
    
    Args:
        file (str): CSV file name.
    
    Returns:
        tuple[pd.DataFrame, str]: DataFrame and CSV string version.
    """
    datas_dir = get_datas_dir()
    files_way = datas_dir / file

    if not files_way.exists():
        Warning = 'File not found. Examine the file name and try again. Check if the file is in the "datas" folder.'
        return Warning

    df = pd.read_csv(files_way)
    
    data_csv = df.to_csv(index=False)
    
    return df, data_csv


def import_xlsx(file: str):
    """
    Reads an XLSX file and returns a DataFrame and its string version (CSV format).
    
    Args:
        file (str): Name of the XLSX file.
    
    Returns:
        tuple[pd.DataFrame, str]: DataFrame and CSV string version.
    """

    print('Importing xlsx data...')
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)

    datas_dir = get_datas_dir()
    files_way = datas_dir / file

    if not files_way.exists():
        warning = 'File not found. Examine the file name and try again. Check if the file is in the "datas" folder.'
        return warning

    df = pd.read_excel(files_way)
    
    data_csv = df.to_csv(index=False)
    
    return df, data_csv