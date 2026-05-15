import pandas as pd

def preprocess_reviews(df):
    """
    Clean and preprocess review dataset.
    """

    # Remove missing values
    df = df.dropna(
        subset=["review", "rating"]
    )

    # Remove duplicate reviews using review_id
    df = df.drop_duplicates(
        subset=["review_id"]
    )

    # Normalize dates
    df["date"] = pd.to_datetime(
        df["date"]
    ).dt.strftime("%Y-%m-%d")

    return df