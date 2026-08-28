import pandas as pd
from scipy.stats import skew, kurtosis


def eda_summary(df: pd.DataFrame):
    """
    Print a compact exploratory data analysis summary.

    Includes:
    - dataframe structure
    - missing-value counts
    - numeric summary statistics
    - skewness and kurtosis
    - categorical value counts and proportions

    Parameters
    ----------
    df : pd.DataFrame
        Input dataframe to profile.
    """

    print("=== Structure ===")
    df.info()

    print("\n=== Missing Values ===")
    print(df.isna().sum())

    numeric_cols = df.select_dtypes(include="number").columns

    if len(numeric_cols) > 0:
        print("\n=== Numeric Summary ===")

        summary = df[numeric_cols].describe().T

        summary["skew"] = [
            skew(df[col].dropna())
            for col in numeric_cols
        ]

        summary["kurtosis"] = [
            kurtosis(df[col].dropna())
            for col in numeric_cols
        ]

        print(summary)

    categorical_cols = df.select_dtypes(
        include=["object", "category"]
    ).columns

    if len(categorical_cols) > 0:
        print("\n=== Categorical Summary ===")

        for col in categorical_cols:
            print(f"\n--- {col} ---")

            print("Counts:")
            print(df[col].value_counts(dropna=False))

            print("\nProportions:")
            print(
                df[col].value_counts(
                    normalize=True,
                    dropna=False
                )
            )