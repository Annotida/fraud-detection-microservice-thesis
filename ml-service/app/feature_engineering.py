from datetime import datetime
from app.schemas import TransactionRequest

from app.risk_profiles import (
    MERCHANT_RISK,
    LOCATION_RISK,
    TRANSACTION_TYPE_RISK,
    KNOWN_DEVICES,
    AMOUNT_THRESHOLDS
)

KNOWN_DEVICES = {
    "DEVICE001",
    "DEVICE002",
    "DEVICE003"
}


def build_features(transaction: TransactionRequest):

    # Current hour (0-23)
    hour = datetime.now().hour

    # Time feature
    time_feature = hour * 3600

    # Device score
    device_score = (
        0.1
        if transaction.deviceId in KNOWN_DEVICES
        else 2.0
    )

    # Merchant score
    merchant_score = MERCHANT_RISK.get(
        transaction.merchant,
        0.5
    )

    # Location score
    location_score = LOCATION_RISK.get(
        transaction.location,
        0.5
    )

    # Transaction type score
    transaction_score = TRANSACTION_TYPE_RISK.get(
        transaction.transactionType,
        0.5
    )

    # Amount score
    amount = transaction.amount

    if amount < AMOUNT_THRESHOLDS["LOW"]:
        amount_score = 0.1
    elif amount < AMOUNT_THRESHOLDS["MEDIUM"]:
        amount_score = 0.5
    elif amount < AMOUNT_THRESHOLDS["HIGH"]:
        amount_score = 1.0
    else:
        amount_score = 3.0
    
    # Business hours (08:00–18:00)
    business_hours = 1 if 8 <= hour <= 18 else 0

    # High value transaction
    high_value = 1 if amount >= 5000 else 0

    # High risk merchant
    high_risk_merchant = 1 if merchant_score >= 2 else 0

    # High risk location
    high_risk_location = 1 if location_score >= 2 else 0

    # Unknown device
    unknown_device = 1 if device_score >= 2 else 0

    # Online transaction
    online_transaction = (
        1 if transaction.transactionType == "ONLINE"
        else 0
    )

    # Night transaction
    night_transaction = (
        1 if hour >= 22 or hour <= 5
        else 0
    )

    # Weekend placeholder
    weekend = 0

    features = [

        time_feature,

        merchant_score,
        location_score,
        device_score,
        transaction_score,
        amount_score,

        business_hours,
        high_value,
        high_risk_merchant,
        high_risk_location,
        unknown_device,
        online_transaction,
        night_transaction,
        weekend,

        *([0] * 15),

        amount
    ]

    return [features]