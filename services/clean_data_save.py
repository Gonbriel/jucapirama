import pandas as pd
from io import StringIO

def csv_to_xlsx(table_string: str, output_file: str):
    """
    Converts a table in string format (CSV) back to a DataFrame and saves it as an Excel file (.xlsx).
    
    Args:
        table_string (str): The table in string format (CSV).
        output_file (str): Path to save the Excel file.
    """
    print("Converting string to xlsx...\n")
    df = pd.read_csv(StringIO(table_string))
    data_csv = df.to_csv(index=False)
    
    df.to_excel(output_file, index=False)
    print(f"Table saved as {output_file}")
    return df, data_csv

def csv_to_csv(table_string: str, output_file: str):
    """
    Converts a table in string format (CSV) back to a DataFrame and saves it as a CSV file.
    
    Args:
        table_string (str): The table in string format (CSV).
        output_file (str): Path to save the CSV file.
    """
    print("Converting string to csv...\n")
    df = pd.read_csv(StringIO(table_string))
    data_csv = df.to_csv(index=False)

    df.to_csv(output_file, index=False)
    print(f"Table saved as {output_file}")
    return df, data_csv

