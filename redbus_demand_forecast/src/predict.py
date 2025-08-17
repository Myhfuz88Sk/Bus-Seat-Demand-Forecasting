import pandas as pd
from src.feature_engineering import create_time_features, merge_transactions_data

def predict_demand(model, df_test, df_transactions, features):
    """
    Generates demand predictions on the test dataset.

    Args:
        model: The trained machine learning model.
        df_test (pd.DataFrame): The test DataFrame.
        df_transactions (pd.DataFrame): The transactions DataFrame.
        features (list): A list of feature column names used for training.

    Returns:
        pd.DataFrame: A DataFrame with 'route_key' and predicted 'final_seatcount'.
    """
    df_test_processed = create_time_features(df_test)

   
    df_test_processed = merge_transactions_data(df_test_processed, df_transactions, dbd_value=30)

    if 'cumsum_seatcount' in features and 'cumsum_searchcount' in features:
        df_test_processed['cumsum_seatcount'] = df_test_processed['cumsum_seatcount'].fillna(0)
        df_test_processed['cumsum_searchcount'] = df_test_processed['cumsum_searchcount'].fillna(0)
    elif 'cumsum_seatcount' in features:
        df_test_processed['cumsum_seatcount'] = df_test_processed['cumsum_seatcount'].fillna(0)
    elif 'cumsum_searchcount' in features:
        df_test_processed['cumsum_searchcount'] = df_test_processed['cumsum_searchcount'].fillna(0)


    X_test = df_test_processed[features]
    predictions = model.predict(X_test)

    submission_df = pd.DataFrame({
        'route_key': df_test['route_key'],
        'final_seatcount': predictions
    })
    return submission_df