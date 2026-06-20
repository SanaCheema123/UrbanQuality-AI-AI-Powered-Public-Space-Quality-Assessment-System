from pathlib import Path
import json, pandas as pd

ROOT = Path(__file__).resolve().parents[2]
PROCESSED_PATH = ROOT / "data" / "processed" / "processed_urban_quality.csv"
RAW_PATH = ROOT / "data" / "raw" / "world_cities_quality_of_life.csv"
OUTPUTS = ROOT / "outputs"

def load_data():
    if PROCESSED_PATH.exists(): return pd.read_csv(PROCESSED_PATH)
    if RAW_PATH.exists(): return pd.read_csv(RAW_PATH)
    return pd.DataFrame()

def load_classification_comparison():
    p = OUTPUTS / "classification_model_comparison.csv"
    return pd.read_csv(p) if p.exists() else pd.DataFrame()

def load_regression_comparison():
    p = OUTPUTS / "regression_model_comparison.csv"
    return pd.read_csv(p) if p.exists() else pd.DataFrame()

def load_metadata():
    p = OUTPUTS / "training_metadata.json"
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else {}
