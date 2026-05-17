## Comparison of DistilBERT and VADER Sentiment Predictions

DistilBERT was selected because it is a transformer-based model fine-tuned for sentiment analysis and provides better contextual understanding than lexicon-based approaches such as VADER or TextBlob.

The comparison between DistilBERT and VADER showed that both models were generally consistent in identifying strongly positive and strongly negative reviews. Reviews containing clear expressions such as "excellent app" or "bad update" were similarly classified by both approaches.

However, some differences were observed in short or ambiguous reviews. VADER, being a lexicon-based model, sometimes struggled to capture contextual meaning in user feedback. In contrast, DistilBERT demonstrated stronger contextual understanding and produced more reliable confidence scores for complex review text.

Overall, DistilBERT was selected as the primary sentiment analysis model for this project due to its transformer-based architecture and improved natural language understanding capabilities.
## Scraping Methodology

Customer reviews were collected from the Google Play Store using the `google-play-scraper` Python package. Reviews were gathered for three Ethiopian banking mobile applications:

- Commercial Bank of Ethiopia (CBE)
- Bank of Abyssinia (BOA)
- Dashen Bank

### Data Collection Process

1. Installed and configured the `google-play-scraper` library.
2. Identified the Google Play application IDs for each banking application.
3. Scraped review data programmatically using Python.
4. Collected more than 400 reviews per bank to satisfy project requirements.
5. Combined all reviews into a single dataset for preprocessing and analysis.

### Extracted Fields

The following information was collected from each review:

- review_id
- review text
- rating
- review date
- bank name
- source platform

### Data Cleaning

The collected reviews were cleaned before analysis by:

- removing duplicate reviews using `review_id`
- dropping rows with missing review text or ratings
- normalizing dates into `YYYY-MM-DD` format
- standardizing column names

### Date Range

The dataset contains the most recent reviews available during the scraping period in May 2026.

### Limitations

Some limitations encountered during scraping include:

- Google Play review availability changes over time
- Some reviews were extremely short or non-informative
- Rate limits and pagination constraints from Google Play Store
- Review counts may vary slightly between scraping sessions

### Tools and Technologies

- Python
- google-play-scraper
- Pandas
- Jupyter Notebook
- VS Code


  ## PostgreSQL Database Schema

The project uses PostgreSQL to persist cleaned and processed mobile banking app reviews collected from Google Play Store. The relational database is designed with two tables: `banks` and `reviews`.

### Banks Table

The `banks` table stores metadata about the banks and their corresponding mobile applications.

| Column | Data Type | Description |
|---|---|---|
| bank_id | INTEGER PRIMARY KEY | Unique identifier for each bank |
| bank_name | VARCHAR(255) | Name of the bank |
| app_name | VARCHAR(255) | Mobile application name |

### Reviews Table

The `reviews` table stores scraped review data together with sentiment analysis and thematic analysis results.

| Column | Data Type | Description |
|---|---|---|
| review_id | VARCHAR(255) PRIMARY KEY | Unique review identifier |
| bank_id | INTEGER FOREIGN KEY | References `banks(bank_id)` |
| review_text | TEXT | User review text |
| rating | INTEGER | Star rating (1–5) |
| review_date | DATE | Date of the review |
| sentiment_label | VARCHAR(50) | Sentiment classification (positive, negative, neutral) |
| sentiment_score | FLOAT | Confidence score from sentiment model |
| identified_theme | VARCHAR(255) | Extracted review theme |
| source | VARCHAR(100) | Review source platform |

### Relationship Design

- One bank can have many reviews.
- The relationship between `banks` and `reviews` is implemented using the `bank_id` foreign key.
- The schema supports scalable storage and querying of processed customer feedback data.

### Verification Queries

The following SQL queries were used to verify data integrity:

- Count total reviews per bank
- Compute average rating per bank
- Check for null values in important columns

The database contains over 1,000 processed review records inserted using Python and `psycopg2`.