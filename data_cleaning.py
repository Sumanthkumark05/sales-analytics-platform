def clean_data(df):

    df.dropna(inplace=True)

    df.drop_duplicates(inplace=True)

    return df