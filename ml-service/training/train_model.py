from load_data import load_dataset
from preprocess import prepare_data
from train_random_forest import train_random_forest
from train_logistic import train_logistic
from evaluate import evaluate
from save_model import save_model
from feature_importance import plot_feature_importance
from balance_data import apply_smote

from plots import (
    plot_confusion_matrix,
    plot_roc_curve,
    plot_precision_recall_curve
)


def main():

    # Load dataset
    df = load_dataset()

    # Prepare data
    X_train, X_test, y_train, y_test = prepare_data(df)
    
    # Balance the training data
    X_train, y_train = apply_smote(
        X_train,
        y_train
    )

    # --------------------------
    # Random Forest
    # --------------------------

    random_forest = train_random_forest(
        X_train,
        y_train
    )

    print("\nEvaluating Random Forest")

    evaluate(
        random_forest,
        X_test,
        y_test
    )

    # --------------------------
    # Logistic Regression
    # --------------------------

    logistic = train_logistic(
        X_train,
        y_train
    )

    print("\nEvaluating Logistic Regression")

    evaluate(
        logistic,
        X_test,
        y_test
    )

    # --------------------------
    # Save Best Model
    # --------------------------

    save_model(random_forest)
    
    plot_feature_importance(random_forest)
    
      #code for graphs
    plot_confusion_matrix(
        random_forest,
        X_test,
        y_test
    )

    plot_roc_curve(
        random_forest,
        X_test,
        y_test
    )

    plot_precision_recall_curve(
        random_forest,
        X_test,
        y_test
    )


if __name__ == "__main__":
    main()

#Random Forest is the selected model
#The Random Forest model outperformed Logistic Regression on every evaluation metric.
#For a fraud detection system, the most important metric is often recall,
# because missing fraudulent transactions (false negatives) can be more costly than investigating a few legitimate ones.

#Your results:
#Logistic Regression Recall = 70.41%
#Random Forest Recall = 81.63%
#Random Forest detected 11% more fraud cases than Logistic Regression on this test set.