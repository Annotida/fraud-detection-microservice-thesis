MERCHANT_RISK = {

    # Trusted Retail
    "Amazon": -0.3,
    "Takealot": -0.2,
    "Checkers": -0.2,
    "Shoprite": -0.2,
    "Pick n Pay": -0.2,
    "Woolworths": -0.2,
    "Makro": -0.1,
    "Game": -0.1,
    "Clicks": -0.2,
    "Dis-Chem": -0.2,

    # E-commerce
    "Temu": 0.3,
    "Shein": 0.4,
    "AliExpress": 0.5,
    "eBay": 0.4,

    # Banking
    "Capitec": -0.3,
    "FNB": -0.3,
    "Standard Bank": -0.3,
    "Nedbank": -0.3,
    "Absa": -0.3,

    # Medium Risk
    "Luxury Store": 2.0,
    "Jewellery Store": 2.2,
    "Electronics Warehouse": 1.8,

    # High Risk
    "Crypto Exchange": 3.0,
    "Bitcoin ATM": 3.0,
    "Dark Web Market": 3.5,
    "Illegal Goods": 3.5,
    "Unknown Merchant": 2.5,

    "Unknown": 1.5
}

LOCATION_RISK = {

    # Low Risk
    "South Africa": 0.2,
    "Pretoria": 0.2,
    "Johannesburg": 0.2,
    "Cape Town": 0.3,
    "Durban": 0.3,
    "Bloemfontein": 0.3,
    "Port Elizabeth": 0.3,

    # Medium Risk
    "Zimbabwe": 0.5,
    "Botswana": 0.5,
    "Namibia": 0.5,
    "Kenya": 0.8,
    "Uganda": 0.8,

    # Higher Risk
    "Nigeria": 2.5,
    "Russia": 3.0,
    "Belarus": 2.8,
    "Iran": 2.8,

    # Highest Risk
    "North Korea": 3.5,

    # Business Hubs
    "Dubai": 2.5,
    "Hong Kong": 2.0,

    "Unknown": 1.5
}

TRANSACTION_TYPE_RISK = {

    "POS": 0.2,
    "ATM": 0.4,
    "CARD": 0.3,

    "ONLINE": 1.0,
    "ECOMMERCE": 1.0,

    "TRANSFER": 1.5,
    "WIRE_TRANSFER": 2.5,

    "CRYPTO": 3.0,

    "INTERNATIONAL_TRANSFER": 3.0,

    "MOBILE_PAYMENT": 0.8,

    "QR_PAYMENT": 0.7,

    "CASH_WITHDRAWAL": 0.6
}

KNOWN_DEVICES = {

    "DEVICE001",
    "DEVICE002",
    "DEVICE003",
    "DEVICE004",
    "DEVICE005",
    "DEVICE006",
    "DEVICE007",
    "DEVICE008",
    "DEVICE009",
    "DEVICE010"
}

AMOUNT_THRESHOLDS = {
    "LOW": 500,
    "MEDIUM": 2000,
    "HIGH": 5000
}