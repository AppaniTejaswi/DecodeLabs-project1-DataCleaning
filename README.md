Data Cleaning and Preparation

Objective

Clean and prepare a dataset for analysis using Python and Pandas.

Dataset Information

- Rows: 1200
- Columns: 14

Data Cleaning Steps

1. Loaded dataset using Pandas.
2. Identified missing values using "isnull().sum()".
3. Checked duplicate rows using "duplicated().sum()".
4. Found 309 missing values in the CouponCode column.
5. Filled missing CouponCode values with "No Coupon".
6. Verified no missing values remained.
7. Saved the cleaned dataset.

Results

- Missing values before cleaning: 309
- Missing values after cleaning: 0
- Duplicate rows: 0

Tools Used

- Python
- Pandas
