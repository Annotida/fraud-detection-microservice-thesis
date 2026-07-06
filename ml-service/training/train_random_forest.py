from sklearn.ensemble import RandomForestClassifier

def train_random_forest(X_train, y_train):

    print("\nTraining Random Forest Model...")

    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )

    model.fit(X_train, y_train)

    print("Model training completed.")

    return model