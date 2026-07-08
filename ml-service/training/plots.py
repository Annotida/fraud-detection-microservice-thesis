import matplotlib.pyplot as plt
from sklearn.metrics import (
    ConfusionMatrixDisplay,
    RocCurveDisplay,
    PrecisionRecallDisplay
)


def plot_confusion_matrix(model, X_test, y_test):

    plt.figure(figsize=(6, 5))

    ConfusionMatrixDisplay.from_estimator(
        model,
        X_test,
        y_test,
        cmap="Blues",
        values_format="d"
    )

    plt.title("Confusion Matrix - Random Forest")
    plt.xlabel("Predicted Class")
    plt.ylabel("Actual Class")

    plt.tight_layout()

    plt.savefig(
        "results/confusion_matrix.png",
        dpi=300
    )

    plt.close()

    print("Confusion Matrix saved.")


def plot_roc_curve(model, X_test, y_test):

    plt.figure(figsize=(6, 5))

    RocCurveDisplay.from_estimator(
        model,
        X_test,
        y_test
    )

    plt.title("ROC Curve - Random Forest")

    plt.tight_layout()

    plt.savefig(
        "results/roc_curve.png",
        dpi=300
    )

    plt.close()

    print("ROC Curve saved.")


def plot_precision_recall_curve(model, X_test, y_test):

    plt.figure(figsize=(6, 5))

    PrecisionRecallDisplay.from_estimator(
        model,
        X_test,
        y_test
    )

    plt.title("Precision-Recall Curve - Random Forest")

    plt.tight_layout()

    plt.savefig(
        "results/precision_recall_curve.png",
        dpi=300
    )

    plt.close()

    print("Precision-Recall Curve saved.")