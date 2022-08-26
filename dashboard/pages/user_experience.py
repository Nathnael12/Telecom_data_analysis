from msilib.schema import Icon
import os
import pandas as pd
import streamlit as st
import pickle
import matplotlib.pyplot as plt

cwd = os.getcwd()

# @st.cache
def load_data(DATA_URL):
    
    data = pickle.load(open(DATA_URL, "rb"))
    return data

st.set_page_config(page_title="User Engagement Analysis", page_icon="👤", layout="wide")

# st.sidebar.header("Please select the desired page")
data = load_data(f"{cwd}/data/experience_data.pkl")

