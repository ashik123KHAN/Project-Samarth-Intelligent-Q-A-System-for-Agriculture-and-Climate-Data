# src/etl/cleaners.py
import pandas as pd
from fuzzywuzzy import process

def normalize_state_name(name):
    if pd.isna(name):
        return None
    return name.strip().title()

def clean_crop_df(df):
    df = df.rename(columns=lambda c: c.strip())
    df['state'] = df['state'].apply(normalize_state_name)
    df['crop'] = df['crop'].str.strip().str.title()
    df['production_tonnes'] = pd.to_numeric(df['production_tonnes'], errors='coerce')
    df['area_hectares'] = pd.to_numeric(df['area_hectares'], errors='coerce')
    return df

def clean_rainfall_df(df):
    df = df.rename(columns=lambda c: c.strip())
    df['state'] = df['state'].apply(normalize_state_name)
    df['total_mm'] = pd.to_numeric(df['total_mm'], errors='coerce')
    return df
