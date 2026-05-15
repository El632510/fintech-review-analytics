from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd

# Load VADER analyzer
analyzer = SentimentIntensityAnalyzer()

def analyze_vader_sentiment(review_text):
    """
    Analyze sentiment using VADER.
    """

    scores = analyzer.polarity_scores(
        str(review_text)
    )

    compound_score = scores["compound"]

    # Assign sentiment label
    if compound_score >= 0.05:
        sentiment = "positive"

    elif compound_score <= -0.05:
        sentiment = "negative"

    else:
        sentiment = "neutral"

    return pd.Series(
        [sentiment, compound_score]
    )