from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)


def evaluate(model, X_test, y_test):

    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)
    precision = precision_score(y_test, predictions)
    recall = recall_score(y_test, predictions)
    f1 = f1_score(y_test, predictions)

    print("\nModel Performance")

    print(f"Accuracy : {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall   : {recall:.4f}")
    print(f"F1 Score : {f1:.4f}")

    print("\nConfusion Matrix")
    print(confusion_matrix(y_test, predictions))

    report = classification_report(y_test, predictions)

    print("\nClassification Report")
    print(report)

    with open("results/metrics.txt", "w") as file:

        file.write("MODEL EVALUATION\n")
        file.write("=========================\n\n")

        file.write(f"Accuracy : {accuracy:.4f}\n")
        file.write(f"Precision: {precision:.4f}\n")
        file.write(f"Recall   : {recall:.4f}\n")
        file.write(f"F1 Score : {f1:.4f}\n\n")

        file.write("Classification Report\n")
        file.write(report)