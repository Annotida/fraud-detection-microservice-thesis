"""
Risk Profiles for Business Fraud Detection Dataset

This file contains the risk scores used to generate the synthetic
banking transaction dataset. Higher scores indicate higher fraud risk.
"""

# =====================================================
# MERCHANT RISK SCORES
# =====================================================

MERCHANT_RISK = {

    # -------------------------
    # Trusted Merchants
    # -------------------------

    "Amazon": -0.3,
    "Takealot": -0.3,
    "Checkers": -0.2,
    "Pick n Pay": -0.2,
    "Woolworths": -0.2,
    "Makro": -0.1,
    "Clicks": -0.2,
    "Dis-Chem": -0.2,
    "Shell": -0.1,
    "Engen": -0.1,
    "Uber": -0.2,
    "Bolt": -0.2,
    "Netflix": -0.4,
    "Spotify": -0.4,
    "Apple": -0.1,
    "Google Play": -0.1,
    "Steam": -0.1,

    # -------------------------
    # Medium Risk
    # -------------------------

    "Electronics Store": 1.0,
    "Jewellery Store": 1.5,
    "Luxury Boutique": 1.2,
    "Gaming Marketplace": 1.1,
    "Travel Agency": 0.8,
    "Airline Booking": 0.8,
    "Hotel Booking": 0.7,

    # -------------------------
    # High Risk
    # -------------------------

    "Crypto Exchange": 3.0,
    "Dark Web Market": 3.5,
    "Unknown Merchant": 2.5,
    "Offshore Transfer": 3.0,
    "Anonymous Wallet": 3.2
}

# =====================================================
# LOCATION RISK SCORES
# =====================================================

LOCATION_RISK = {

    # -------------------------
    # Low Risk Countries
    # -------------------------

    "South Africa": 0.2,
    "Botswana": 0.2,
    "Namibia": 0.2,
    "Zimbabwe": 0.3,
    "Zambia": 0.3,
    "Kenya": 0.4,

    # -------------------------
    # Medium Risk Countries
    # -------------------------

    "United Kingdom": 0.8,
    "Germany": 0.8,
    "France": 0.8,
    "United States": 1.0,
    "Canada": 0.8,
    "Australia": 0.8,
    "UAE": 1.2,

    # -------------------------
    # Higher Risk Countries
    # -------------------------

    "Nigeria": 2.5,
    "Russia": 3.0,
    "North Korea": 3.5,
    "Iran": 3.0
}

# =====================================================
# TRANSACTION TYPE RISK
# =====================================================

TRANSACTION_TYPE_RISK = {

    # Everyday Transactions

    "POS": 0.1,
    "ONLINE": 0.2,
    "ATM": 0.4,
    "MOBILE_PAYMENT": 0.2,

    # Business Transactions

    "BANK_TRANSFER": 0.8,
    "INTERNATIONAL_TRANSFER": 2.5,
    "WIRE_TRANSFER": 3.0,

    # High Risk

    "CRYPTO": 3.0,
    "CASH_WITHDRAWAL": 2.0
}

# =====================================================
# DEVICE RISK
# =====================================================

DEVICE_RISK = {

    "KNOWN_DEVICE": 0.0,

    "NEW_DEVICE": 1.0,

    "UNKNOWN_DEVICE": 2.5,

    "BLACKLISTED_DEVICE": 4.0
}

# =====================================================
# CUSTOMER PERSONAS
# =====================================================

CUSTOMER_PERSONAS = {

    "Student": {
        "avg_transaction": (50, 800),
        "preferred_hours": (16, 23)
    },

    "Professional": {
        "avg_transaction": (300, 5000),
        "preferred_hours": (8, 19)
    },

    "Business Owner": {
        "avg_transaction": (1000, 50000),
        "preferred_hours": (7, 18)
    },

    "Traveller": {
        "avg_transaction": (300, 10000),
        "preferred_hours": (6, 23)
    },

    "High Risk": {
        "avg_transaction": (500, 80000),
        "preferred_hours": (0, 23)
    }

}

# =====================================================
# MERCHANT CATEGORIES
# =====================================================

TRUSTED_MERCHANTS = [

    "Amazon",
    "Takealot",
    "Checkers",
    "Pick n Pay",
    "Woolworths",
    "Makro",
    "Clicks",
    "Dis-Chem",
    "Shell",
    "Engen",
    "Uber",
    "Bolt",
    "Netflix",
    "Spotify",
    "Apple",
    "Google Play"

]

MEDIUM_RISK_MERCHANTS = [

    "Electronics Store",
    "Jewellery Store",
    "Luxury Boutique",
    "Gaming Marketplace",
    "Travel Agency",
    "Airline Booking",
    "Hotel Booking"

]

HIGH_RISK_MERCHANTS = [

    "Crypto Exchange",
    "Dark Web Market",
    "Unknown Merchant",
    "Offshore Transfer",
    "Anonymous Wallet"

]

# =====================================================
# DATASET CONFIGURATION
# =====================================================

NUM_CUSTOMERS = 500

TRANSACTIONS_PER_CUSTOMER = 40

FRAUD_THRESHOLD = 6

# =====================================================
# KNOWN DEVICES
# =====================================================

KNOWN_DEVICES = [

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

]

# =====================================================
# COUNTRIES
# =====================================================

COUNTRIES = [

    "South Africa",
    "Botswana",
    "Namibia",
    "Zimbabwe",
    "Zambia",
    "Kenya",
    "United Kingdom",
    "Germany",
    "France",
    "United States",
    "Canada",
    "Australia",
    "UAE",
    "Nigeria",
    "Russia",
    "North Korea",
    "Iran"

]

# =====================================================
# TRANSACTION TYPES
# =====================================================

TRANSACTION_TYPES = [

    "POS",
    "ONLINE",
    "ATM",
    "MOBILE_PAYMENT",
    "BANK_TRANSFER",
    "INTERNATIONAL_TRANSFER",
    "WIRE_TRANSFER",
    "CRYPTO",
    "CASH_WITHDRAWAL"

]



# =====================================================
# PERSONA LIST
# =====================================================

PERSONAS = list(CUSTOMER_PERSONAS.keys())



# =====================================================
# ALL MERCHANTS
# =====================================================

ALL_MERCHANTS = (

    TRUSTED_MERCHANTS +

    MEDIUM_RISK_MERCHANTS +

    HIGH_RISK_MERCHANTS

)