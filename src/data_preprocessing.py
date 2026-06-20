from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RAW_PATH = ROOT / "data" / "raw" / "world_cities_quality_of_life.csv"
PROCESSED_PATH = ROOT / "data" / "processed" / "processed_urban_quality.csv"

def load_dataset(path=RAW_PATH):
    path = Path(path)
    if not path.exists():
        from generate_sample_data import main
        main()
    return pd.read_csv(path)

def clean_dataset(df):
    df = df.copy()
    df.columns = [c.strip().lower().replace(" ","_") for c in df.columns]
    df = df.drop_duplicates()
    for col in df.columns:
        converted = pd.to_numeric(df[col], errors="coerce")
        if converted.notna().sum() > len(df)*0.70:
            df[col] = converted.fillna(converted.median())
        else:
            df[col] = df[col].astype(str)
            mode = df[col].mode()
            df[col] = df[col].replace("nan", mode.iloc[0] if not mode.empty else "Unknown")
    return df

def ensure_targets(df):
    df = df.copy()
    if "quality_of_life_index" not in df.columns:
        numeric = df.select_dtypes(include="number")
        if numeric.empty:
            raise ValueError("Dataset needs numeric columns or quality_of_life_index.")
        score = numeric.apply(lambda s:(s-s.min())/(s.max()-s.min()+1e-9)).mean(axis=1)*100
        df["quality_of_life_index"] = score.round(2)
    if "public_space_quality" not in df.columns:
        df["public_space_quality"] = pd.cut(df["quality_of_life_index"], bins=[-1,40,60,80,101], labels=["Poor","Moderate","Good","Excellent"]).astype(str)
    return df

def preprocess(path=RAW_PATH):
    df = ensure_targets(clean_dataset(load_dataset(path)))
    PROCESSED_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(PROCESSED_PATH, index=False)
    return df

if __name__ == "__main__":
    preprocess()
    print(f"Processed data saved: {PROCESSED_PATH}")
