import random
import uuid
from datetime import datetime
import pandas as pd
from pathlib import Path

random.seed(42)

from risk_profiles import (
    MERCHANT_RISK,
    LOCATION_RISK,
    TRANSACTION_TYPE_RISK,
    DEVICE_RISK,
    CUSTOMER_PERSONAS,
    PERSONAS,
    TRUSTED_MERCHANTS,
    MEDIUM_RISK_MERCHANTS,
    HIGH_RISK_MERCHANTS,
    KNOWN_DEVICES,
    COUNTRIES,
    TRANSACTION_TYPES,
    NUM_CUSTOMERS,
    TRANSACTIONS_PER_CUSTOMER,
    FRAUD_THRESHOLD,
    ALL_MERCHANTS
)

# ===========================================
# CUSTOMER GENERATION
# ===========================================

def generate_customers():
    
    customers = []

    for i in range(NUM_CUSTOMERS):

        customer_id = f"CUST{i+1:05d}"

        persona = random.choice(PERSONAS)

        persona_profile = CUSTOMER_PERSONAS[persona]

        average_transaction = random.randint(
            persona_profile["avg_transaction"][0],
            persona_profile["avg_transaction"][1]
        )

        home_country = random.choice(COUNTRIES)

        preferred_device = random.choice(KNOWN_DEVICES)

        if persona == "Student":

            usual_merchants = random.sample([
                "Takealot",
                "Uber",
                "Netflix",
                "Spotify",
                "Checkers"
            ], 3)

        elif persona == "Professional":

            usual_merchants = random.sample([
                "Amazon",
                "Checkers",
                "Woolworths",
                "Shell",
                "Makro"
            ], 3)

        elif persona == "Business Owner":

            usual_merchants = random.sample([
                "Electronics Store",
                "Travel Agency",
                "Amazon",
                "Makro",
                "Airline Booking"
            ], 3)

        elif persona == "Traveller":

            usual_merchants = random.sample([
                "Airline Booking",
                "Hotel Booking",
                "Uber",
                "Amazon",
                "Shell"
            ], 3)

        else:

            usual_merchants = random.sample(ALL_MERCHANTS, 3)

        customer = {

            "customer_id": customer_id,

            "persona": persona,

            "home_country": home_country,

            "preferred_device": preferred_device,

            "average_transaction": average_transaction,

            "usual_merchants": usual_merchants

        }

        customers.append(customer)

    return customers
    
# ===========================================
# TRANSACTION GENERATION
# ===========================================

def generate_transactions(customers):
    
    transactions = []

    for customer in customers:

        for _ in range(TRANSACTIONS_PER_CUSTOMER):

            merchant = random.choice(customer["usual_merchants"])

            amount = round(
                random.uniform(
                    customer["average_transaction"] * 0.5,
                    customer["average_transaction"] * 1.5
                ),
                2
            )

            transaction_type = random.choice(TRANSACTION_TYPES)

            device = customer["preferred_device"]

            country = customer["home_country"]

            hour = random.randint(0, 23)

            # --------------------------------------------------
            # Introduce realistic fraud -- 10% of transactions
            # --------------------------------------------------

            if random.random() < 0.10:

                suspicious_features = random.randint(2, 4)

                anomalies = random.sample(
                    ["merchant", "device", "country", "amount", "transaction_type", "hour"],
                    suspicious_features
                )

                if "merchant" in anomalies:
                    merchant = random.choice(HIGH_RISK_MERCHANTS)

                if "device" in anomalies:
                    device = random.choice([
                        "UNKNOWN_DEVICE",
                        "BLACKLISTED_DEVICE"
                    ])

                if "country" in anomalies:
                    country = random.choice([
                        "Nigeria",
                        "Russia",
                        "North Korea",
                        "Iran"
                    ])

                if "amount" in anomalies:
                    amount *= random.uniform(5, 15)

                if "transaction_type" in anomalies:
                    transaction_type = random.choice([
                        "CRYPTO",
                        "WIRE_TRANSFER",
                        "INTERNATIONAL_TRANSFER"
                    ])

                if "hour" in anomalies:
                    hour = random.randint(0, 4)
                    
            timestamp = datetime.now().replace(
                hour=hour,
                minute=random.randint(0, 59),
                second=random.randint(0, 59),
                microsecond=0
            )

            transaction = {

                "transaction_id": str(uuid.uuid4()),
                
                "timestamp": timestamp.isoformat(),

                "customer_id": customer["customer_id"],

                "persona": customer["persona"],

                "merchant": merchant,

                "amount": round(amount, 2),

                "country": country,

                "transaction_type": transaction_type,

                "device": device,
                
                "preferred_device": customer["preferred_device"],

                "hour": hour

            }

            score, label = calculate_fraud_score(transaction)

            transaction["fraud_score"] = score
            transaction["label"] = label

            transactions.append(transaction)

    return transactions

# ===========================================
# FRAUD SCORING
# ===========================================

def calculate_fraud_score(transaction):
    score = 0

    # Merchant risk
    score += MERCHANT_RISK.get(transaction["merchant"], 1)

    # Country risk
    score += LOCATION_RISK.get(transaction["country"], 1)

    # Transaction type
    score += TRANSACTION_TYPE_RISK.get(
        transaction["transaction_type"],
        1
    )

    # Device risk
    score += DEVICE_RISK.get(
        transaction["device"],
        1
    )

    # Large amount
    if transaction["amount"] > 50000:
        score += 4
    
    elif transaction["amount"] > 10000:
        score += 2

    # Night transactions
    if transaction["hour"] <= 5:
        score += 1

    label = 1 if score >= FRAUD_THRESHOLD else 0

    return round(score, 2), label

# ===========================================
# SAVE DATASET
# ===========================================

def save_dataset(transactions):
    
    df = pd.DataFrame(transactions)

    output_dir = Path(__file__).parent / "datasets"
    output_dir.mkdir(exist_ok=True)

    output_file = output_dir / "business_transactions.csv"

    df.to_csv(output_file, index=False)

    print("=" * 50)
    print("Business dataset generated successfully!")
    print(f"Saved to: {output_file}")
    print(f"Transactions: {len(df)}")
    print(f"Fraud Cases: {(df['label'] == 1).sum()}")
    print(f"Legitimate: {(df['label'] == 0).sum()}")
    print("=" * 50)
    
    summary = df["label"].value_counts()

    print("\nLabel Distribution")
    print(summary)

    print("\nFraud Percentage")
    print(round(summary[1] / len(df) * 100, 2), "%")
    

def main():

    customers = generate_customers()

    transactions = generate_transactions(customers)

    save_dataset(transactions)

if __name__ == "__main__":
    main()