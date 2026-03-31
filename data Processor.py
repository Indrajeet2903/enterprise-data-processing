from validator import validate_data

def process_data(df):
    if df is None:
        return None

    df = validate_data(df)

    # Example transformation
    if 'salary' in df.columns:
        df['salary'] = df['salary'] * 1.1

    return df
