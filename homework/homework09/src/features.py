import pandas as pd


def add_spend_income_ratio(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add monthly spending relative to income.
    """
    result = df.copy()
    result["spend_income_ratio"] = (
        result["monthly_spend"] / result["income"]
    )
    return result


def add_income_credit_interaction(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add an interaction between income and credit score.
    """
    result = df.copy()
    result["income_credit_interaction"] = (
        result["income"] * result["credit_score"]
    )
    return result


def add_region_frequency(df: pd.DataFrame) -> pd.DataFrame:
    """
    Frequency-encode the region categorical column.
    """
    result = df.copy()

    frequencies = result["region"].value_counts(
        normalize=True
    )

    result["region_frequency"] = result["region"].map(
        frequencies
    )

    return result