def validate_data(df):
    # Drop null values
    df = df.dropna()

    # Remove duplicates
    df = df.drop_duplicates()

    return df
