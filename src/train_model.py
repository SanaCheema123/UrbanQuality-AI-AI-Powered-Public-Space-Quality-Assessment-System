from pathlib import Path
import json
import joblib
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, r2_score, mean_absolute_error, mean_squared_error
)

from data_preprocessing import preprocess

ROOT = Path(__file__).resolve().parents[1]
MODELS = ROOT / "models"
OUTPUTS = ROOT / "outputs"

CLASS_TARGET = "public_space_quality"
REG_TARGET = "quality_of_life_index"


def build_preprocessor(X):
    num_cols = X.select_dtypes(include="number").columns.tolist()
    cat_cols = X.select_dtypes(exclude="number").columns.tolist()

    return ColumnTransformer([
        ("num", StandardScaler(), num_cols),
        ("cat", OneHotEncoder(handle_unknown="ignore"), cat_cols)
    ])


def train():
    df = preprocess()

    X = df.drop(columns=[CLASS_TARGET, REG_TARGET])
    y_class = df[CLASS_TARGET]
    y_reg = df[REG_TARGET]

    class_counts = y_class.value_counts()

    if class_counts.min() < 2:
        X_train, X_test, yc_train, yc_test, yr_train, yr_test = train_test_split(
            X,
            y_class,
            y_reg,
            test_size=0.2,
            random_state=42
        )
    else:
        X_train, X_test, yc_train, yc_test, yr_train, yr_test = train_test_split(
            X,
            y_class,
            y_reg,
            test_size=0.2,
            random_state=42,
            stratify=y_class
        )

    preprocessor = build_preprocessor(X)

    class_models = {
        "Random Forest Classifier": RandomForestClassifier(
            n_estimators=180,
            random_state=42
        ),
        "Decision Tree Classifier": DecisionTreeClassifier(
            random_state=42
        )
    }

    class_results = []
    best_acc = -1
    best_pipe = None
    best_name = ""
    best_cm = None
    best_labels = sorted(y_class.unique())

    for name, model in class_models.items():
        pipe = Pipeline([
            ("preprocessor", preprocessor),
            ("model", model)
        ])

        pipe.fit(X_train, yc_train)
        pred = pipe.predict(X_test)

        acc = accuracy_score(yc_test, pred)

        class_results.append({
            "Model": name,
            "Accuracy": acc,
            "Precision": precision_score(
                yc_test,
                pred,
                average="weighted",
                zero_division=0
            ),
            "Recall": recall_score(
                yc_test,
                pred,
                average="weighted",
                zero_division=0
            ),
            "F1 Score": f1_score(
                yc_test,
                pred,
                average="weighted",
                zero_division=0
            )
        })

        if acc > best_acc:
            best_acc = acc
            best_pipe = pipe
            best_name = name
            best_cm = confusion_matrix(
                yc_test,
                pred,
                labels=best_labels
            )

    reg_models = {
        "Random Forest Regressor": RandomForestRegressor(
            n_estimators=180,
            random_state=42
        ),
        "Decision Tree Regressor": DecisionTreeRegressor(
            random_state=42
        )
    }

    reg_results = []
    best_r2 = -999
    best_reg = None
    best_reg_name = ""

    for name, model in reg_models.items():
        pipe = Pipeline([
            ("preprocessor", preprocessor),
            ("model", model)
        ])

        pipe.fit(X_train, yr_train)
        pred = pipe.predict(X_test)

        r2 = r2_score(yr_test, pred)

        reg_results.append({
            "Model": name,
            "R2 Score": r2,
            "MAE": mean_absolute_error(yr_test, pred),
            "RMSE": mean_squared_error(yr_test, pred) ** 0.5
        })

        if r2 > best_r2:
            best_r2 = r2
            best_reg = pipe
            best_reg_name = name

    MODELS.mkdir(exist_ok=True)
    OUTPUTS.mkdir(exist_ok=True)

    joblib.dump(
        best_pipe,
        MODELS / "best_public_space_classifier.pkl"
    )

    joblib.dump(
        best_reg,
        MODELS / "best_quality_score_regressor.pkl"
    )

    pd.DataFrame(class_results).to_csv(
        OUTPUTS / "classification_model_comparison.csv",
        index=False
    )

    pd.DataFrame(reg_results).to_csv(
        OUTPUTS / "regression_model_comparison.csv",
        index=False
    )

    pd.DataFrame(
        best_cm,
        index=best_labels,
        columns=best_labels
    ).to_csv(
        OUTPUTS / "confusion_matrix.csv"
    )

    metadata = {
        "best_classifier": best_name,
        "classification_accuracy": round(float(best_acc), 4),
        "best_regressor": best_reg_name,
        "regression_r2": round(float(best_r2), 4),
        "feature_columns": X.columns.tolist()
    }

    (OUTPUTS / "training_metadata.json").write_text(
        json.dumps(metadata, indent=4),
        encoding="utf-8"
    )

    print(f"Best classifier: {best_name} | Accuracy: {best_acc:.4f}")
    print(f"Best regressor: {best_reg_name} | R2: {best_r2:.4f}")
    print(f"Models saved: {MODELS}")


if __name__ == "__main__":
    train()