MERCHANT_RISK = {

    "Amazon": -0.3,
    "Takealot": -0.2,
    "Shoprite": 0.1,
    "Checkers": 0.1,

    "Luxury Store": 2.0,
    "Crypto Exchange": 3.0,
    "Unknown": 1.5
}

LOCATION_RISK = {

    "Pretoria": 0.2,
    "Johannesburg": 0.2,
    "Cape Town": 0.3,
    "Durban": 0.3,

    "Dubai": 2.5,
    "Unknown": 1.5
}

TRANSACTION_TYPE_RISK = {

    "POS": 0.2,
    "ATM": 0.4,
    "ONLINE": 1.0,
    "TRANSFER": 1.5
}

KNOWN_DEVICES = {
    "DEVICE001",
    "DEVICE002",
    "DEVICE003"
}

AMOUNT_THRESHOLDS = {
    "LOW": 500,
    "MEDIUM": 2000,
    "HIGH": 5000
}