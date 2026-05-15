from pathlib import Path

import pandas as pd
from sklearn.tree import DecisionTreeClassifier


BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "student_data.csv"
FEATURES = ["study_hours", "attendance", "previous_grade", "assignment_score"]
TARGET = "result"


def train_model():
    data = pd.read_csv(DATA_PATH)
    X = data[FEATURES]
    y = data[TARGET]

    model = DecisionTreeClassifier(random_state=42)
    model.fit(X, y)
    return model


_MODEL = train_model()


def predict_student_performance(
    study_hours, attendance, previous_grade, assignment_score
):
    input_data = pd.DataFrame(
        [[study_hours, attendance, previous_grade, assignment_score]],
        columns=FEATURES,
    )
    return _MODEL.predict(input_data)[0]


def calculate_risk_level(
    prediction, study_hours, attendance, previous_grade, assignment_score
):
    risk_score = 0

    if study_hours < 4:
        risk_score += 1
    if attendance < 60:
        risk_score += 1
    if previous_grade < 50:
        risk_score += 1
    if assignment_score < 55:
        risk_score += 1
    if prediction == "Fail":
        risk_score += 1

    if risk_score <= 1:
        return "Low Risk"
    if risk_score <= 3:
        return "Medium Risk"
    return "High Risk"
