# Data Quality Checks and PostgreSQL Loader

This repository contains Python functions to perform quality checks on a dataset and load the cleaned data into a PostgreSQL database. These tools are designed to streamline the data preprocessing and ingestion pipeline.

## Features

data_qual_checks(df)

A preloading quality check function that evaluates a given pandas DataFrame for:

- **Missing reviews**: Counts rows where the review column is null.
- **Missing ratings**: Counts rows where the rating column is null.
- **Invalid ratings**: Counts rows where rating values are outside the valid range of 1 to 5.

The function returns a dictionary summarizing these issues.

**Input**:
• A pandas DataFrame with review and rating columns.

**Output**:

```python
{
    'missing_reviews_count': <number>,
    'missing_ratings_count': <number>,
    'invalid_ratings_count': <number>
}
```
**load_data_postgres(df, table_name, conn_string)**


A utility function to load the validated DataFrame into a PostgreSQL database table.

**Parameters**:

- df: A pandas DataFrame to load.
- table_name: Name of the target PostgreSQL table.
- conn_string: The connection string for the PostgreSQL database.

**Features**:

    •	Uses SQLAlchemy to connect to PostgreSQL.
    •	Ensures the data is loaded without overwriting the existing table structure.

### Dependencies

- This project requires the following Python libraries:
- pandas: For DataFrame manipulation.
- numpy: For numerical computations.
- sqlalchemy: To interface with the PostgreSQL database.
- json: To handle JSON operations.
- app_store_scraper: For scraping data from app stores (optional,   depending on your pipeline setup).

Install them via pip:
```python
pip install pandas numpy sqlalchemy app_store_scraper
```

### Usage

1. Perform Data Quality Checks:

```python
import pandas as pd
from your_module_name import data_qual_checks

# Example DataFrame
data = {'review': ['Great app!', None, 'Okay app'], 'rating': [5, None, 7]}
df = pd.DataFrame(data)

# Perform checks
results = data_qual_checks(df)
print(results)
```

2. Load Data into PostgreSQL:

```python
from your_module_name import load_data_postgres

# Connection string example
conn_string = "postgresql://user:password@localhost:5432/mydatabase"

# Load data into table
load_data_postgres(df, "app_reviews", conn_string)
```

### Project Structure
```python
.
├── README.md
├── your_script.py # Replace with your script name
├── requirements.txt # List of dependencies
```

### License

This project is licensed under the MIT License. See the LICENSE file for details.
