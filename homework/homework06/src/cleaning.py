import pandas as pd
from sklearn.preprocessing import MinMaxScaler


def fill_missing_median(df: pd.DataFrame, columns=None) -> pd.DataFrame:
    """
    Fill missing numeric values with the median.

    Parameters
    ----------
    df : pd.DataFrame
        Input DataFrame.
    columns : list or None
        Columns to fill. If None, all numeric columns are used.

    Returns
    -------
    pd.DataFrame
        DataFrame with missing numeric values filled.
    """
    result = df.copy()

    if columns is None:
        columns = result.select_dtypes(include="number").columns

    for col in columns:
        result[col] = result[col].fillna(result[col].median())

    return result


def drop_missing(df: pd.DataFrame, threshold=0.5) -> pd.DataFrame:
    """
    Drop columns whose proportion of missing values exceeds the threshold.

    Parameters
    ----------
    df : pd.DataFrame
        Input DataFrame.
    threshold : float
        Maximum allowed proportion of missing values in a column.

    Returns
    -------
    pd.DataFrame
        DataFrame with columns having excessive missingness removed.
    """
    result = df.copy()

    missing_ratio = result.isna().mean()
    columns_to_drop = missing_ratio[missing_ratio > threshold].index

    return result.drop(columns=columns_to_drop)

def normalize_data(df: pd.DataFrame, columns) -> pd.DataFrame:
    """
    Normalize selected numeric columns to the range [0, 1].

    Parameters
    ----------
    df : pd.DataFrame
        Input DataFrame.
    columns : list
        Numeric columns to normalize.

    Returns
    -------
    pd.DataFrame
        DataFrame with normalized columns.
    """
    result = df.copy()

    scaler = MinMaxScaler()
    result[columns] = scaler.fit_transform(result[columns])

    return result