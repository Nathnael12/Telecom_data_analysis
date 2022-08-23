import pandas as pd
import numpy as np


class Utils:

    def load_data(self, data_path: str,dtype:dict=None) -> pd.DataFrame:
        """
        Load data from a csv file.
        """
        try:
            df = pd.read_csv(data_path,dtype=dtype)
        except FileNotFoundError:
            print("File not found.")
        return df

    def save_data(self, df: pd.DataFrame, data_path:str) -> None:
        """
        Save data to a csv file.
        """
        try:
            df.to_csv(data_path,index=False)
            print("Data saved successfully!")
        except Exception as e:
            print(f"Saving failed {e}")