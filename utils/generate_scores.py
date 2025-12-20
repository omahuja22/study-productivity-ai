import pandas as pd
from score_calculator import calculate_productivity_score

df = pd.read_csv("../data/study_logs.csv")

scores = []

for _, row in df.iterrows():
    score = calculate_productivity_score(
        row["study_minutes"],
        row["break_minutes"],
        row["focus_level"],
        row["distractions"]
    )
    scores.append(score)

df["productivity_score"] = scores
df.to_csv("../data/study_logs.csv", index=False)

print("Productivity scores generated successfully!")
