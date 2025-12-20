import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# Load data
df = pd.read_csv("../data/study_logs.csv")

X = df[
    [
        "study_minutes",
        "break_minutes",
        "focus_level",
        "distractions",
        "hour_of_day",
        "day_of_week"
    ]
]

y = df["productivity_score"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestRegressor(
    n_estimators=200,
    random_state=42
)

model.fit(X_train, y_train)

predictions = model.predict(X_test)
mae = mean_absolute_error(y_test, predictions)

print("Model trained successfully")
print("Mean Absolute Error:", mae)

with open("productivity_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model saved as productivity_model.pkl")
