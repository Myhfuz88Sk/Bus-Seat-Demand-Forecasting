import pandas as pd

def create_time_features(df):
    """
    Creates time-based features from the 'doj' column.

    Args:
        df (pd.DataFrame): The input DataFrame with a 'doj' column.

    Returns:
        pd.DataFrame: The DataFrame with added time-based features.
    """
    df['day_of_week'] = df['doj'].dt.dayofweek
    df['day_of_month'] = df['doj'].dt.day
    df['month'] = df['doj'].dt.month
    df['year'] = df['doj'].dt.year
    df['week_of_year'] = df['doj'].dt.isocalendar().week.astype(int)
    df['is_weekend'] = (df['doj'].dt.dayofweek >= 5).astype(int) # Saturday and Sunday
    return df

def merge_transactions_data(df_main, df_transactions, dbd_value=15):
    """
    Merges main dataframe (train/test) with transactions data based on doj, srcid, destid
    and a specific days before departure (dbd) value.

    Args:
        df_main (pd.DataFrame): The main DataFrame (e.g., train or test).
        df_transactions (pd.DataFrame): The transactions DataFrame.
        dbd_value (int): The 'Days Before Departure' value to filter transactions by.

    Returns:
        pd.DataFrame: The merged DataFrame.
    """
    
    df_transactions_filtered = df_transactions[df_transactions['dbd'] == dbd_value].copy()

    transaction_cols_to_merge = ['doj', 'srcid', 'destid', 'cumsum_seatcount', 'cumsum_searchcount']

    df_merged = pd.merge(
        df_main,
        df_transactions_filtered[transaction_cols_to_merge],
        on=['doj', 'srcid', 'destid'],
        how='left'
    )
    return df_merged