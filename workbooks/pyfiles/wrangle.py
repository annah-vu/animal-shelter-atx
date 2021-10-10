import pandas as pd
import numpy as np

def get_shelter_data():
    df = pd.read_csv('shelter_data/atxshelter2021.csv')
    return df 
