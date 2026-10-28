from src.recommender import Song, UserProfile, Recommender

def make_small_recommender() -> Recommender:
    songs = [
        Song(
            id=1,
            title="Test Pop Track",
            artist="Test Artist",
            genre="pop",
            mood="happy",
            energy=0.8,
            tempo_bpm=120,
            valence=0.9,
            danceability=0.8,
            acousticness=0.2,
        ),
        Song(
            id=2,
            title="Chill Lofi Loop",
            artist="Test Artist",
            genre="lofi",
            mood="chill",
            energy=0.4,
            tempo_bpm=80,
            valence=0.6,
            danceability=0.5,
            acousticness=0.9,
        ),
    ]
    return Recommender(songs)


def test_recommend_returns_songs_sorted_by_score():
    user = UserProfile(
        favorite_genre="pop",
        favorite_mood="happy",
        target_energy=0.8,
        likes_acoustic=False,
    )
    rec = make_small_recommender()
    results = rec.recommend(user, k=2)

    assert len(results) == 2
    # Starter expectation: the pop, happy, high energy song should score higher
    assert results[0].genre == "pop"
    assert results[0].mood == "happy"


def test_explain_recommendation_returns_non_empty_string():
    user = UserProfile(
        favorite_genre="pop",
        favorite_mood="happy",
        target_energy=0.8,
        likes_acoustic=False,
    )
    rec = make_small_recommender()
    song = rec.songs[0]

    explanation = rec.explain_recommendation(user, song)
    assert isinstance(explanation, str)
    assert explanation.strip() != ""


def test_scoring_modes_change_the_ranking():
    from src.recommender import recommend_songs, STRATEGIES

    songs = [
        {"title": "Pop But Intense", "genre": "pop", "mood": "intense", "energy": 0.8, "acousticness": 0.2},
        {"title": "Rock But Happy", "genre": "rock", "mood": "happy", "energy": 0.8, "acousticness": 0.2},
    ]
    prefs = {"genre": "pop", "mood": "happy", "energy": 0.8}

    genre_first = recommend_songs(prefs, songs, k=1, strategy=STRATEGIES["genre-first"])
    mood_first = recommend_songs(prefs, songs, k=1, strategy=STRATEGIES["mood-first"])

    assert genre_first[0][0]["title"] == "Pop But Intense"
    assert mood_first[0][0]["title"] == "Rock But Happy"


def test_mood_first_gives_partial_credit_for_related_mood():
    from src.recommender import STRATEGIES

    song = {"title": "Lazy Sunday", "genre": "jazz", "mood": "relaxed", "energy": 0.4, "acousticness": 0.8}
    score, reasons = STRATEGIES["mood-first"].score({"genre": "lofi", "mood": "chill"}, song)

    assert score == 1.0
    assert reasons[0].startswith("related mood")
