from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RAW_PATH = ROOT / "data" / "raw" / "world_cities_quality_of_life.csv"

def main(n=900, seed=42):
    np.random.seed(seed)
    cities = ["Vienna","Zurich","Copenhagen","Amsterdam","Berlin","Paris","London","Barcelona","Toronto","Vancouver","New York","Chicago","Singapore","Tokyo","Seoul","Dubai","Sydney","Melbourne","Istanbul","Doha","Kuala Lumpur","Bangkok","Lahore","Karachi"]
    countries = ["Austria","Switzerland","Denmark","Netherlands","Germany","France","UK","Spain","Canada","Canada","USA","USA","Singapore","Japan","South Korea","UAE","Australia","Australia","Turkey","Qatar","Malaysia","Thailand","Pakistan","Pakistan"]
    idx = np.random.randint(0, len(cities), n)
    safety = np.random.uniform(35,95,n); healthcare = np.random.uniform(40,95,n)
    climate = np.random.uniform(35,95,n); purchasing = np.random.uniform(25,120,n)
    cost = np.random.uniform(30,120,n); traffic = np.random.uniform(15,75,n)
    pollution = np.random.uniform(10,90,n); green = np.random.uniform(20,95,n)
    walk = np.random.uniform(25,95,n); access = np.random.uniform(30,95,n)
    comfort = np.random.uniform(30,95,n)
    quality = safety*.18 + healthcare*.12 + climate*.10 + purchasing*.08 + green*.16 + walk*.14 + access*.12 + comfort*.10 - pollution*.10 - traffic*.07 - cost*.04 + np.random.normal(0,4,n)
    quality = np.clip(quality,0,100)
    df = pd.DataFrame({
        "city":[cities[i] for i in idx], "country":[countries[i] for i in idx],
        "quality_of_life_index":np.round(quality,2), "safety_index":np.round(safety,2),
        "healthcare_index":np.round(healthcare,2), "climate_index":np.round(climate,2),
        "purchasing_power_index":np.round(purchasing,2), "cost_of_living_index":np.round(cost,2),
        "traffic_commute_index":np.round(traffic,2), "pollution_index":np.round(pollution,2),
        "green_space_index":np.round(green,2), "walkability_index":np.round(walk,2),
        "accessibility_index":np.round(access,2), "comfort_index":np.round(comfort,2),
        "latitude":np.round(np.random.uniform(24,60,n),5), "longitude":np.round(np.random.uniform(-125,140,n),5)
    })
    df["public_space_quality"] = pd.cut(df["quality_of_life_index"], bins=[-1,40,60,80,101], labels=["Poor","Moderate","Good","Excellent"]).astype(str)
    RAW_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(RAW_PATH, index=False)
    print(f"Sample dataset saved: {RAW_PATH}")

if __name__ == "__main__":
    main()
