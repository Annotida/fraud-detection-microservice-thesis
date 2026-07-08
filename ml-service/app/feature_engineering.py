from app.schemas import TransactionRequest


def build_features(transaction: TransactionRequest):

    """
    Builds a 30-feature vector expected by the Random Forest model.
    This is Version 1 of the feature engineering pipeline.
    """

    features = [

        # Time
        0,

        # V1 - V28 placeholders
        *([0] * 28),

        # Amount
        transaction.amount
    ]

    return [features]