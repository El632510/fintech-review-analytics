import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Initialize tools
stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()


def preprocess_text(text):
    """
    NLP preprocessing pipeline:
    - lowercase
    - tokenization
    - stop-word removal
    - lemmatization
    """

    # Convert to lowercase
    text = str(text).lower()

    # Tokenization
    tokens = word_tokenize(text)

    # Remove stopwords and non-alphabetic tokens
    filtered_tokens = [
        word for word in tokens
        if word.isalpha()
        and word not in stop_words
    ]

    # Lemmatization
    lemmatized_tokens = [
        lemmatizer.lemmatize(word)
        for word in filtered_tokens
    ]

    return " ".join(lemmatized_tokens)