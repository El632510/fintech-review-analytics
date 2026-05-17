from transformers import pipeline
import pandas as pd

# Load model function
def load_sentiment_model():

    sentiment_pipeline = pipeline(
        "sentiment-analysis",
        model="distilbert-base-uncased-finetuned-sst-2-english"
    )

    return sentiment_pipeline


def analyze_sentiment(review_text, sentiment_pipeline):

    try:

        result = sentiment_pipeline(
            str(review_text)[:512]
        )[0]

        label = result["label"]
        score = result["score"]

        if label == "POSITIVE":
            sentiment = "positive"
        else:
            sentiment = "negative"

        return pd.Series([sentiment, score])

    except Exception:

        return pd.Series(["neutral", 0.0])