# Application Usage and Test Scenarios

## 1. How to Start the Application with Docker
From the project folder, run:

```bash
docker build -t student-performance-predictor .
docker run --rm -p 5056:5000 student-performance-predictor
```

Then open:

```text
http://127.0.0.1:5056/
```

## 2. How to Use the Application
1. Open the home page.
2. Enter values in all four fields:
   - Study hours per week
   - Attendance percentage
   - Previous grade
   - Assignment completion score
3. Click `Predict Result`.
4. Review the prediction page.
5. Click `Try Another Prediction` to return to the form.

## 3. Test Scenario 1: Likely Pass
Input values:

| Field | Value |
|---|---:|
| Study hours per week | 6 |
| Attendance percentage | 75 |
| Previous grade | 60 |
| Assignment completion score | 70 |

Expected outcome:

| Output | Expected Value |
|---|---|
| Prediction | Pass |
| Risk Level | Low Risk |

Screenshot:

![Pass Result](docs/screenshots/02-pass-result.png)

## 4. Test Scenario 2: Likely Fail
Input values:

| Field | Value |
|---|---:|
| Study hours per week | 2 |
| Attendance percentage | 45 |
| Previous grade | 35 |
| Assignment completion score | 40 |

Expected outcome:

| Output | Expected Value |
|---|---|
| Prediction | Fail |
| Risk Level | High Risk |

Screenshot:

![Fail Result](docs/screenshots/03-fail-result.png)

## 5. Test Scenario 3: Borderline Student
Input values:

| Field | Value |
|---|---:|
| Study hours per week | 4 |
| Attendance percentage | 60 |
| Previous grade | 50 |
| Assignment completion score | 55 |

Expected outcome:

| Output | Expected Value |
|---|---|
| Prediction | Pass or Fail depending on the trained Decision Tree |
| Risk Level | Medium Risk is likely for borderline values |

This scenario is useful for checking how the model behaves with values close to the pass/fail boundary.

## 6. Validation Checks
The form requires all fields before submission. The browser prevents submission if a required field is empty.

Recommended checks:

- Submit a strong student profile and confirm the result is low risk.
- Submit a weak student profile and confirm the result is high risk.
- Click `Try Another Prediction` and confirm the app returns to the home page.
- Confirm that the result page shows the exact input values entered by the user.

## 7. Expected Application Flow
```text
Home Page
User enters student data
User clicks Predict Result
Flask sends data to model.py
Decision Tree model predicts Pass or Fail
Result page displays prediction, risk level, and input values
```

