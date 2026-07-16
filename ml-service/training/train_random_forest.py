from sklearn.ensemble import RandomForestClassifier


def train_random_forest(X_train, y_train):

    print("\nTraining Random Forest Model...")

    model = RandomForestClassifier(

        n_estimators=300,

        max_depth=12,

        min_samples_split=5,

        min_samples_leaf=2,

        class_weight="balanced",

        random_state=42,

        n_jobs=-1
    )

    model.fit(X_train, y_train)

    print("Model training completed.")

    return model