from sklearn.model_selection import train_test_split

def prepare_data(df):

    X = df.drop("Class", axis=1)
    y = df["Class"]

    print("\nFeature Matrix Shape:")
    print(X.shape)

    print("\nTarget Shape:")
    print(y.shape)

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    print("\nTraining Set:")
    print(X_train.shape)

    print("\nTesting Set:")
    print(X_test.shape)

    return X_train, X_test, y_train, y_test