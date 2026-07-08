from imblearn.over_sampling import SMOTE


def apply_smote(X_train, y_train):

    print("\nApplying SMOTE...")

    smote = SMOTE(
        random_state=42
    )

    X_resampled, y_resampled = smote.fit_resample(
        X_train,
        y_train
    )

    print("SMOTE completed.")

    print(f"Original samples : {len(y_train)}")
    print(f"Balanced samples : {len(y_resampled)}")

    return X_resampled, y_resampled