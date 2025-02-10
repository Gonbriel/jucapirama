import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from io import StringIO
import os

def scatter(table_string: str, column_x: str, column_y: str, title: str, dpi: int, figsize: tuple, alpha: float, filename: str):
    """
    Creates a scatter plot with the given cleared DataFrame and columns, then saves it as an image.
    
    Args:
        table_string (str): The cleared table in string format (CSV).
        column_x (str): The name of the column to use for the x-axis.
        column_y (str): The name of the column to use for the y-axis.
        title (str): The title of the plot.
        dpi (int): The resolution of the image that you think it's good.
        figsize (tuple): The size of the plot that you think it's good.
        alpha (float): The transparency of the points in the plot that you think it's good.
        filename (str): The name of the file with .png for output.
    """

    print('Creating scatter plot...\n')
    
    try:
        df = pd.read_csv(StringIO(table_string), sep=",")  

        if column_x not in df.columns or column_y not in df.columns:
            raise ValueError(f"Columns '{column_x}' and/or '{column_y}' not found in the DataFrame.")

        plt.figure(figsize=figsize)
        plt.scatter(df[column_x], df[column_y], alpha=alpha, edgecolors='k')
        plt.xlabel(column_x)
        plt.ylabel(column_y)
        plt.title(title)
        plt.grid(True)

        filename = filename
        file_path = os.path.join(os.getcwd(), filename)

        plt.savefig(file_path, dpi=dpi, bbox_inches="tight")
        plt.close()

        text = f"Scatter plot saved as '{file_path}'"
        return text

    except Exception as e:
        return e
