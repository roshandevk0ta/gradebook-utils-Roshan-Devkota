# gradebook/gradebook.py
"""
Gradebook utility functions for computing grades.
"""
def average(scores):
    """Compute the average of a list of scores."""
    return sum(scores) / len(scores) if scores else 0.0
def curve(scores, points):
    """
    Return a new list of scores after adding `points` to each.
    Scores are clamped at a minimum of 0 to avoid negative results.
    """
    return [max(0, s + points) for s in scores]