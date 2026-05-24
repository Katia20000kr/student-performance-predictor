import pandas as pd
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier



data = pd.read_csv("../student_data.csv")


print("First rows:")
print(data.head())


print("\nMissing values:")
print(data.isnull().sum())


features = ["study_hours", "attendance", "previous_grade", "assignment_score"]
target = "result"

X = data[features]
y = data[target]

# 5. Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)


predictions = model.predict(X_test)


accuracy = accuracy_score(y_test, predictions)
print("\nAccuracy:", accuracy)
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, predictions))
print("\nClassification Report:")
print(classification_report(y_test, predictions))


example_student = pd.DataFrame(
    [[6, 75, 60, 70]],
    columns=features,
)
example_prediction = model.predict(example_student)
print("\nExample Prediction:", example_prediction[0])
