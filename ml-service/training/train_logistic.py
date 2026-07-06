from sklearn.linear_model import LogisticRegression

def train_logistic(X_train, y_train):

    print("\nTraining Logistic Regression...")

    model = LogisticRegression(
        random_state=42,
        max_iter=1000
    )

    model.fit(X_train, y_train)

    print("Logistic Regression completed.")

    return model