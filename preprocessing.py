from sklearn.preprocessing import LabelEncoder

def encode_category(df):

    encoder = LabelEncoder()

    df['Region'] = encoder.fit_transform(df['Region'])

    return df