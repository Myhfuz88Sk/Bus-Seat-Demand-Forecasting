import pandas as pd

def load_data(train_path, test_path, transactions_path):
    """
    Loads the train, test, and transactions datasets.

    Args:
        train_path (str): Path to the train.csv file.
        test_path (str): Path to the test.csv file.
        transactions_path (str): Path to the transactions.csv file.

    Returns:
        tuple: A tuple containing pandas DataFrames for train, test, and transactions data.
    """
    try:
        df_train = pd.read_csv(train_path)
        df_test = pd.read_csv(test_path)
        df_transactions = pd.read_csv(transactions_path)

        df_train['doj'] = pd.to_datetime(df_train['doj'], format='ISO8601')
        df_test['doj'] = pd.to_datetime(df_test['doj'], format='ISO8601')
        
        df_transactions['doj'] = pd.to_datetime(df_transactions['doj'], format='ISO8601')
        df_transactions['doi'] = pd.to_datetime(df_transactions['doi'], format='ISO8601')

        return df_train, df_test, df_transactions
    except FileNotFoundError as e:
        print(f"Error loading file: {e}. Please ensure all data files are in the 'data/' directory.")
        return None, None, None
    except Exception as e:
        print(f"An unexpected error occurred during data loading: {e}. Please ensure your date columns are consistently in YYYY-MM-DD format.")
        return None, None, None