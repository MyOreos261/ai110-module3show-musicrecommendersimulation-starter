"""
Command line runner for the Music Recommender Simulation.

Run from the project root with:  python -m src.main
Add --experiment to rerun every profile with the experimental weights
(energy doubled, genre halved).
"""

import sys

from src.recommender import load_songs, recommend_songs, EXPERIMENT_WEIGHTS

PROFILES = {
    # Starter / default profile
    "High-Energy Pop": {"genre": "pop", "mood": "happy", "energy": 0.8, "likes_acoustic": False},
    "Chill Lofi": {"genre": "lofi", "mood": "chill", "energy": 0.35, "likes_acoustic": True},
    "Deep Intense Rock": {"genre": "rock", "mood": "intense", "energy": 0.9, "likes_acoustic": False},
    # Adversarial / edge cases
    "Conflicted (sad but high energy)": {"genre": "folk", "mood": "sad", "energy": 0.9},
    "Unknown Genre (polka)": {"genre": "polka", "mood": "happy", "energy": 0.5},
}


def print_recommendations(name: str, prefs: dict, recommendations: list) -> None:
    """Print one profile's top results in a readable block."""
    print("=" * 64)
    print(f"Profile: {name}")
    print("  " + ", ".join(f"{key}={value}" for key, value in prefs.items()))
    print("-" * 64)
    for rank, (song, score, explanation) in enumerate(recommendations, start=1):
        print(f"{rank}. {song['title']} by {song['artist']}  [{song['genre']}/{song['mood']}]")
        print(f"   Score: {score:.2f}")
        for reason in explanation.split("; "):
            print(f"     - {reason}")
    print()


def main() -> None:
    songs = load_songs("data/songs.csv")
    weights = EXPERIMENT_WEIGHTS if "--experiment" in sys.argv else None
    if weights:
        print(f"EXPERIMENT MODE: weights = {weights}")
    print()

    for name, prefs in PROFILES.items():
        recommendations = recommend_songs(prefs, songs, k=5, weights=weights)
        print_recommendations(name, prefs, recommendations)


if __name__ == "__main__":
    main()
