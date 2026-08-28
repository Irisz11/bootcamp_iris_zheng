# Homework 06 — Data Preprocessing

## Cleaning Strategy

This homework applies reusable preprocessing functions to a raw dataset and saves the cleaned result to `data/processed/`.

### Missing Value Handling

Missing values in the numeric columns `age`, `income`, and `score` are filled using the median.

Median imputation was chosen because it is less sensitive to extreme values than mean imputation and allows all observations to remain in the dataset.

### Dropping Columns with Excessive Missingness

Columns with more than 50% missing values are removed.

The `extra_data` column was dropped because most of its values were missing. This assumes that the column is not essential to the analysis.

### Normalization

The numeric columns `age`, `income`, and `score` are normalized to the range [0, 1] using Min-Max scaling.

This makes variables with different magnitudes easier to compare.

`zipcode` is not normalized because it is an identifier rather than a continuous numerical feature.

`city` is preserved as a categorical variable.

### Reusable Cleaning Functions

The preprocessing logic is implemented in `src/cleaning.py` using three reusable functions:

- `fill_missing_median()`
- `drop_missing()`
- `normalize_data()`

Each function returns a cleaned copy of the input DataFrame so that the original data is not modified directly.

### Output

The raw dataset is loaded from:

`data/raw/sample_data.csv`

The cleaned dataset is saved to:

`data/processed/sample_data_cleaned.csv`

### Validation and Comparison

The notebook compares the original and cleaned datasets by checking:

- Dataset shape
- Missing values
- Numeric summary statistics
- The effect of normalization

After preprocessing, the cleaned dataset contains no missing values in the retained columns, and the normalized numeric features range from 0 to 1.

### Assumptions and Tradeoffs

Median imputation preserves all observations but may reduce variability in the affected columns.

Removing columns with excessive missingness simplifies the dataset but may discard potentially useful information.

Min-Max scaling improves feature comparability, but the transformed values are no longer expressed in their original units.