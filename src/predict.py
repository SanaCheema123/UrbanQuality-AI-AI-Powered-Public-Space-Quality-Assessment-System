from pathlib import Path
import joblib, pandas as pd

ROOT = Path(__file__).resolve().parents[1]
CLASS_MODEL = ROOT / "models" / "best_public_space_classifier.pkl"
REG_MODEL = ROOT / "models" / "best_quality_score_regressor.pkl"

def predict_public_space(input_data):
    if not CLASS_MODEL.exists() or not REG_MODEL.exists():
        raise FileNotFoundError("Models not found. Run: py src/train_model.py")
    clf = joblib.load(CLASS_MODEL); reg = joblib.load(REG_MODEL)
    df = pd.DataFrame([input_data])
    quality_class = str(clf.predict(df)[0])
    score = float(reg.predict(df)[0])
    result = {"quality_class": quality_class, "quality_score": round(max(0,min(100,score)),2)}
    result["confidence"] = round(float(clf.predict_proba(df)[0].max())*100,2) if hasattr(clf,"predict_proba") else None
    return result
