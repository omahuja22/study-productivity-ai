from flask import Flask, render_template, request, redirect, url_for
import pickle
import pandas as pd
from datetime import datetime, timedelta
import os

app = Flask(__name__)

MODEL_PATH = os.path.join("model", "productivity_model.pkl")
DATA_PATH = os.path.join("data", "study_logs.csv")

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

# ---------------- HOME ----------------
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        study_minutes = int(request.form["study_minutes"])
        break_minutes = int(request.form["break_minutes"])
        focus_level = int(request.form["focus_level"])
        distractions = int(request.form["distractions"])
        hour_of_day = int(request.form["hour_of_day"])
        day_of_week = datetime.now().weekday()

        features = [[
            study_minutes,
            break_minutes,
            focus_level,
            distractions,
            hour_of_day,
            day_of_week
        ]]

        prediction = int(model.predict(features)[0])

        new_row = {
            "date": datetime.now().strftime("%Y-%m-%d"),
            "subject": "General",
            "study_minutes": study_minutes,
            "break_minutes": break_minutes,
            "focus_level": focus_level,
            "distractions": distractions,
            "hour_of_day": hour_of_day,
            "day_of_week": day_of_week,
            "productivity_score": prediction
        }

        df = pd.read_csv(DATA_PATH)
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        df.to_csv(DATA_PATH, index=False)

        return redirect(url_for("dashboard"))

    return render_template("index.html")

# ---------------- DASHBOARD ----------------
@app.route("/dashboard")
def dashboard():
    df = pd.read_csv(DATA_PATH)

    total_sessions = len(df)
    avg_score = round(df["productivity_score"].mean(), 1)
    latest_score = int(df.iloc[-1]["productivity_score"])

    dates = df["date"].tolist()
    scores = df["productivity_score"].tolist()

    # Focus distribution
    high = len(df[df["productivity_score"] >= 70])
    mid = len(df[(df["productivity_score"] >= 40) & (df["productivity_score"] < 70)])
    low = len(df[df["productivity_score"] < 40])
    focus_distribution = [high, mid, low]

    # -------- Best Study Time Insight --------
    best_hour = (
        df.groupby("hour_of_day")["productivity_score"]
        .mean()
        .idxmax()
    )

    best_time_insight = f"Your productivity is highest around {best_hour}:00 hours."

    # -------- Weekly Summary --------
    df["date"] = pd.to_datetime(df["date"])
    last_7 = df[df["date"] >= datetime.now() - timedelta(days=7)]
    prev_7 = df[
        (df["date"] < datetime.now() - timedelta(days=7)) &
        (df["date"] >= datetime.now() - timedelta(days=14))
    ]

    weekly_avg = round(last_7["productivity_score"].mean(), 1) if not last_7.empty else avg_score
    prev_avg = round(prev_7["productivity_score"].mean(), 1) if not prev_7.empty else weekly_avg

    weekly_change = round(weekly_avg - prev_avg, 1)

    # -------- Insight Text --------
    if avg_score >= 70:
        health_insight = "Excellent consistency. Keep this routine."
    elif avg_score >= 40:
        health_insight = "Moderate productivity. Small changes can improve results."
    else:
        health_insight = "Low productivity detected. Consider reducing distractions."

    return render_template(
        "dashboard.html",
        total_sessions=total_sessions,
        avg_score=avg_score,
        latest_score=latest_score,
        dates=dates,
        scores=scores,
        focus_distribution=focus_distribution,
        best_time_insight=best_time_insight,
        weekly_avg=weekly_avg,
        weekly_change=weekly_change,
        health_insight=health_insight
    )

if __name__ == "__main__":
    app.run(debug=True)
