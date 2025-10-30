# src/etl/downloaders.py
from pathlib import Path
import pandas as pd

DATA_DIR = Path(__file__).resolve().parents[2] / "data" / "snapshots"

def load_crop_snapshot():
    path = DATA_DIR / "crop_sample.csv"
    return pd.read_csv(path)

def load_rainfall_snapshot():
    path = DATA_DIR / "rainfall_sample.csv"
    return pd.read_csv(path)
