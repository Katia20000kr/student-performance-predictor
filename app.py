from flask import Flask, render_template, request

from model import calculate_risk_level, predict_student_performance


app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    study_hours = float(request.form["study_hours"])
    attendance = float(request.form["attendance"])
    previous_grade = float(request.form["previous_grade"])
    assignment_score = float(request.form["assignment_score"])

    prediction = predict_student_performance(
        study_hours, attendance, previous_grade, assignment_score
    )
    risk_level = calculate_risk_level(
        prediction, study_hours, attendance, previous_grade, assignment_score
    )

    student_input = {
        "Study hours per week": study_hours,
        "Attendance percentage": attendance,
        "Previous grade": previous_grade,
        "Assignment completion score": assignment_score,
    }

    return render_template(
        "result.html",
        prediction=prediction,
        risk_level=risk_level,
        student_input=student_input,
    )


if __name__ == "__main__":
    app.run(debug=True)
