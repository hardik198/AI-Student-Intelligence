import pandas as pd
import joblib
import os

from model_features import MODEL_FEATURES


# ============================================================
# LOAD MODEL
# ============================================================

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

MODEL_PATH = os.path.join(
    BASE_DIR,
    "models",
    "student_outcome_model.pkl"
)

model = joblib.load(MODEL_PATH)


# ============================================================
# PREDICTION FUNCTION
# ============================================================

def predict_student(student_data):

    # Convert dictionary to DataFrame
    student_df = pd.DataFrame([student_data])

    # --------------------------------------------------------
    # FEATURE ENGINEERING
    # --------------------------------------------------------

    sem1_enrolled = student_df[
        "Curricular units 1st sem (enrolled)"
    ].iloc[0]

    sem1_approved = student_df[
        "Curricular units 1st sem (approved)"
    ].iloc[0]

    sem2_enrolled = student_df[
        "Curricular units 2nd sem (enrolled)"
    ].iloc[0]

    sem2_approved = student_df[
        "Curricular units 2nd sem (approved)"
    ].iloc[0]

    if sem1_enrolled > 0:
        sem1_rate = sem1_approved / sem1_enrolled
    else:
        sem1_rate = 0

    if sem2_enrolled > 0:
        sem2_rate = sem2_approved / sem2_enrolled
    else:
        sem2_rate = 0

    average_rate = (
        sem1_rate + sem2_rate
    ) / 2

    student_df["Sem1_Approval_Rate"] = sem1_rate
    student_df["Sem2_Approval_Rate"] = sem2_rate
    student_df["Average_Approval_Rate"] = average_rate

    # --------------------------------------------------------
    # MAKE SURE FEATURES ARE IN EXACT MODEL ORDER
    # --------------------------------------------------------

    student_df = student_df[MODEL_FEATURES]

    # --------------------------------------------------------
    # PREDICTION
    # --------------------------------------------------------

    prediction = model.predict(student_df)[0]

    probabilities = model.predict_proba(student_df)[0]

    probability_dict = {
        str(class_name): float(prob)
        for class_name, prob
        in zip(model.classes_, probabilities)
    }

    return prediction, probability_dict