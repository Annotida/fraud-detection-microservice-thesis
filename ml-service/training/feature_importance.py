import matplotlib.pyplot as plt
import pandas as pd


def plot_feature_importance(model):

    feature_names = [
        "Time",
        "V1","V2","V3","V4","V5","V6","V7","V8","V9","V10",
        "V11","V12","V13","V14","V15","V16","V17","V18","V19","V20",
        "V21","V22","V23","V24","V25","V26","V27","V28",
        "Amount"
    ]

    importance = model.feature_importances_

    df = pd.DataFrame({
        "Feature": feature_names,
        "Importance": importance
    })

    df = df.sort_values(
        by="Importance",
        ascending=False
    )

    print("\nTop 10 Most Important Features")
    print(df.head(10))

    plt.figure(figsize=(10,6))
    plt.bar(df["Feature"][:10], df["Importance"][:10])
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    plt.title("Top 10 Most Important Features")
    plt.xlabel("Feature")
    plt.ylabel("Relative Feature Importance")
    plt.grid(axis="y", linestyle="--", alpha=0.4)

    plt.savefig("results/feature_importance.png")

    print("\nFeature importance graph saved.")