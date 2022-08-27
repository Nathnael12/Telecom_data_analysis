import sys
import unittest
import pandas as pd
import json
import os
cwd = os.getcwd()
sys.path.append(f"{cwd}/scripts")
from clean_data import DataCleaner
sample_df = pd.DataFrame(data=[[1,'3','4'],[1,None,'4'],[1,'3',None],[None,'3','4']],columns=['a b','b','c'])
sample_df_filled_ff = pd.DataFrame(data=[[1,'3','4'],[1,'3','4'],[1,'3','4'],[None,'3','4']],columns=['a b','b','c'])
sample_df_no_space = pd.DataFrame(data=[[1,'3','4'],[1,None,'4'],[1,'3',None],[None,'3','4']],columns=['a_b','b','c'])
cleaner = DataCleaner()

class TestCleanDf(unittest.TestCase):
    
    def setUp(self) -> pd.DataFrame:
        self.df=sample_df.copy()
    def test_remove_whitespace_column(self):
        self.assertTrue(sample_df.equals(cleaner.remove_whitespace_column(sample_df)))
    
    def test_percent_missing(self):
        self.assertEqual(
            cleaner.percent_missing(self.df), 25.00)
    
    def test_get_numerical_col(self):
        self.assertListEqual(
            cleaner.get_numerical_columns(self.df), ['a b'])
    
    def test_percent_missing_column(self):
        self.assertEqual(
            cleaner.percent_missing_column(self.df,'c'), 25.00)
    
    def test_fill_missing_values_categorical(self):
        self.assertTrue(sample_df_filled_ff.equals(cleaner.fill_missing_values_categorical(self.df,'ffill')))

if __name__ == "__main__":
    unittest.main()