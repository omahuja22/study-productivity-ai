def calculate_productivity_score(
    study_minutes,
    break_minutes,
    focus_level,
    distractions
):
    """
    Returns productivity score between 0 and 100
    """

    # Normalize study time (ideal = 120 mins)
    study_score = min(study_minutes / 120, 1) * 40

    # Focus contribution (1–5 scale)
    focus_score = (focus_level / 5) * 30

    # Distraction penalty
    distraction_penalty = min(distractions * 5, 20)

    # Break penalty (ideal break <= 30 mins)
    break_penalty = min(break_minutes / 30, 1) * 10

    score = study_score + focus_score - distraction_penalty - break_penalty

    # Clamp score between 0 and 100
    score = max(0, min(int(score), 100))

    return score
