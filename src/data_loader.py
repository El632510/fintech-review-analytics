import pandas as pd

def load_data(filepath):
    """
    Load CSV dataset.
    """

    df = pd.read_csv(filepath)

    return df