# ============================================================
# MODEL EVALUATION
# ============================================================

import os
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    f1_score,
    classification_report,
    confusion_matrix
)

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

DATA_PATH = os.path.join(
    BASE_DIR,
    "data",
    "data.csv"
)

MODEL_PATH = os.path.join(
    BASE_DIR,
    "models",
    "student_outcome_model.pkl"
)


def get_evaluation():

    # Load dataset
    df = pd.read_csv(DATA_PATH)

    # Load trained model
    model = joblib.load(MODEL_PATH)

    # --------------------------------------------------------
    # SAME FEATURE ENGINEERING USED DURING TRAINING
    # --------------------------------------------------------

    df["Sem1_Approval_Rate"] = (
        df["Curricular units 1st sem (approved)"] /
        df["Curricular units 1st sem (enrolled)"].replace(0, 1)
    )

    df["Sem2_Approval_Rate"] = (
        df["Curricular units 2nd sem (approved)"] /
        df["Curricular units 2nd sem (enrolled)"].replace(0, 1)
    )

    df["Average_Approval_Rate"] = (
        df["Sem1_Approval_Rate"] +
        df["Sem2_Approval_Rate"]
    ) / 2

    # --------------------------------------------------------
    # FEATURES AND TARGET
    # --------------------------------------------------------

    X = df.drop("target", axis=1)
    y = df["target"]

    # Use the same split as training
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    # --------------------------------------------------------
    # PREDICTION
    # --------------------------------------------------------

    y_pred = model.predict(X_test)

    # --------------------------------------------------------
    # METRICS
    # --------------------------------------------------------

    accuracy = accuracy_score(
        y_test,
        y_pred
    )

    macro_f1 = f1_score(
        y_test,
        y_pred,
        average="macro"
    )

    # Classification report
    report = classification_report(
        y_test,
        y_pred,
        output_dict=True,
        zero_division=0
    )

    report_df = pd.DataFrame(report).transpose()

    # Confusion matrix
    cm = confusion_matrix(
        y_test,
        y_pred,
        labels=model.classes_
    )

    confusion_matrix_df = pd.DataFrame(
        cm,
        index=[f"Actual: {c}" for c in model.classes_],
        columns=[f"Predicted: {c}" for c in model.classes_]
    )

    # Feature importance
    if hasattr(model, "feature_importances_"):
        feature_importance = pd.Series(
            model.feature_importances_,
            index=X.columns
        ).sort_values(ascending=False)
    else:
        feature_importance = pd.Series(dtype=float)

    return {
        "accuracy": accuracy,
        "macro_f1": macro_f1,
        "test_samples": len(y_test),
        "report_df": report_df,
        "confusion_matrix_df": confusion_matrix_df,
        "feature_importance": feature_importance
    }
