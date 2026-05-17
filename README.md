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