import pandas as pd

from app.schemas import TransactionRequest
from app.model_loader import label_encoders

# ==========================================================
# KAGGLE FEATURE ENGINEERING (ARCHIVED)
# ==========================================================
#
# from datetime import datetime
# from app.risk_profiles import (
#     MERCHANT_RISK,
#     LOCATION_RISK,
#     TRANSACTION_TYPE_RISK,
#     KNOWN_DEVICES,
#     AMOUNT_THRESHOLDS
# )
#
# def build_features(transaction: TransactionRequest):
#
#     hour = datetime.now().hour
#
#     time_feature = hour * 3600
#
#     device_score = (
#         0.1
#         if transaction.deviceId in KNOWN_DEVICES
#         else 2.0
#     )
#
#     merchant_score = MERCHANT_RISK.get(
#         transaction.merchant,
#         0.2
#     )
#
#     location_score = LOCATION_RISK.get(
#         transaction.location,
#         0.2
#     )
#
#     transaction_score = TRANSACTION_TYPE_RISK.get(
#         transaction.transactionType,
#         0.3
#     )
#
#     amount = transaction.amount
#
#     if amount < AMOUNT_THRESHOLDS["LOW"]:
#         amount_score = 0.1
#     elif amount < AMOUNT_THRESHOLDS["MEDIUM"]:
#         amount_score = 0.5
#     elif amount < AMOUNT_THRESHOLDS["HIGH"]:
#         amount_score = 1.0
#     else:
#         amount_score = 3.0
#
#     business_hours = 1 if 8 <= hour <= 18 else 0
#
#     high_value = 1 if amount >= 5000 else 0
#
#     high_risk_merchant = 1 if merchant_score >= 2 else 0
#
#     high_risk_location = 1 if location_score >= 2 else 0
#
#     unknown_device = 1 if device_score >= 2 else 0
#
#     online_transaction = (
#         1 if transaction.transactionType == "ONLINE"
#         else 0
#     )
#
#     night_transaction = (
#         1 if hour >= 22 or hour <= 5
#         else 0
#     )
#
#     weekday = datetime.now().weekday()
#
#     weekend = 1 if weekday >= 5 else 0
#
#     features = [
#         time_feature,
#         merchant_score,
#         location_score,
#         device_score,
#         transaction_score,
#         amount_score,
#         business_hours,
#         high_value,
#         high_risk_merchant,
#         high_risk_location,
#         unknown_device,
#         online_transaction,
#         night_transaction,
#         weekend,
#         *([0] * 15),
#         amount
#     ]
#
#     return [features]


# ==========================================================
# BUSINESS MODEL FEATURE ENGINEERING (ACTIVE)
# ==========================================================

def build_features(transaction: TransactionRequest):

    data = pd.DataFrame([{
        "persona": transaction.persona,
        "merchant": transaction.merchant,
        "amount": transaction.amount,
        "country": transaction.country,
        "transaction_type": transaction.transactionType,
        "device": transaction.deviceId,
        "preferred_device": transaction.preferredDevice,
        "hour": transaction.hour
    }])

    categorical_columns = [
        "persona",
        "merchant",
        "country",
        "transaction_type",
        "device",
        "preferred_device"
    ]

    for column in categorical_columns:
        data[column] = label_encoders[column].transform(data[column])

    return data