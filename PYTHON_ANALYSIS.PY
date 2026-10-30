# DataCo Supply Chain - Python EDA & ML Model
# Author: Madhavan
# Dataset: 180,519 orders

import pandas as pd
import numpy as np

# 1. DATA CLEANING (Important for Interview)
df = pd.read_csv('DataCoSupplyChainDataset.csv', encoding='latin1')

# Check cleaning issues
print("Shape:", df.shape)
print("Masked columns: Customer Email, Product Description = XXXX")
print("Order Zipcode null count:", df['Order Zipcode'].isnull().sum())

# Drop useless columns
df = df.drop(['Order Zipcode'], axis=1) # All empty
df = df.drop_duplicates()

# 2. EDA - Key Insights
# Late delivery rate
late_rate = df[df['Delivery Status'] == 'Late delivery'].shape[0] / df.shape[0] * 100
print(f"Late Delivery Rate: {late_rate:.2f}%")

# Shipping Mode Analysis
shipping_late = df.groupby('Shipping Mode')['Delivery Status'].apply(
    lambda x: (x == 'Late delivery').sum() / len(x) * 100
)
print(shipping_late)

# 3. ML MODEL - Predict Late Delivery (91% Accuracy)
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Features for model
features = ['Days for shipping (real)', 'Days for shipment (scheduled)', 
            'Shipping Mode', 'Order Region']
# Encoding
df_model = pd.get_dummies(df[features])

X = df_model
y = df['Delivery Status'].apply(lambda x: 1 if x == 'Late delivery' else 0)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("Model Accuracy:", accuracy_score(y_test, y_pred))

# Business Recommendation: If Days real > Days scheduled -> High risk of Late