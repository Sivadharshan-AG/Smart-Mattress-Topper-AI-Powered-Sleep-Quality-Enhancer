import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import joblib

# Load dataset (sample: pressure, motion, heart_rate → sleep_stage)
data = pd.read_csv("sample_dataset.csv")

X = data[["pressure", "motion", "heart_rate"]]
y = data["sleep_stage"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = DecisionTreeClassifier()
model.fit(X_train, y_train)

print("Accuracy:", model.score(X_test, y_test))

joblib.dump(model, "sleep_model.pkl")
