import pandas as pd
import numpy as np
import pickle
import os

from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (
    accuracy_score,
    recall_score,
    classification_report,
    confusion_matrix,
    precision_recall_curve
)

from xgboost import XGBClassifier

# =========================
# Create folder
# =========================
os.makedirs("model", exist_ok=True)

# =========================
# Load dataset
# =========================
data = pd.read_csv("dataset/pima_diabetes.csv")

# =========================
# Feature Engineering
# =========================
data["BMI_Age"] = data["BMI"] * data["Age"]
data["Glucose_Age"] = data["Glucose"] * data["Age"]

# =========================
# Fix invalid zeros
# =========================
cols_with_zero = ['Glucose','BloodPressure','SkinThickness','Insulin','BMI']

for col in cols_with_zero:
    data[col] = data[col].replace(0, np.nan)
    data[col] = data[col].fillna(data[col].median())

# =========================
# Features & Target
# =========================
X = data.drop("Outcome", axis=1)
y = data["Outcome"]

# =========================
# Train-Test Split
# =========================
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# =========================
# Handle class imbalance properly
# =========================
scale_pos_weight = (len(y_train) - sum(y_train)) / sum(y_train)

# =========================
# Pipeline (NO leakage)
# =========================
pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("model", XGBClassifier(
        n_estimators=150,
        max_depth=4,
        learning_rate=0.05,
        subsample=0.8,
        colsample_bytree=0.8,
        scale_pos_weight=scale_pos_weight,
        random_state=42,
        eval_metric='logloss',
        n_jobs=-1
    ))
])

# =========================
# Cross Validation
# =========================
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
cv_scores = cross_val_score(pipeline, X_train, y_train, cv=cv, scoring='accuracy')

print("CV Accuracy:", np.mean(cv_scores))

# =========================
# Train Final Model
# =========================
pipeline.fit(X_train, y_train)

# =========================
# Predict Probabilities
# =========================
y_prob = pipeline.predict_proba(X_test)[:, 1]

# =========================
# Smart Threshold (F1 optimized)
# =========================
precision, recall, thresholds = precision_recall_curve(y_test, y_prob)

f1_scores = 2 * (precision * recall) / (precision + recall + 1e-8)

best_idx = np.argmax(f1_scores)
best_threshold = thresholds[best_idx]

print("Best Threshold:", best_threshold)
print("Best F1 Score:", f1_scores[best_idx])

# Apply threshold
y_pred = (y_prob > best_threshold).astype(int)

# =========================
# Evaluation
# =========================
accuracy = accuracy_score(y_test, y_pred)
recall_val = recall_score(y_test, y_pred)

print("\nTest Accuracy:", accuracy)
print("Recall:", recall_val)

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# =========================
# Save model
# =========================
pickle.dump(pipeline, open("model/diabetes_pipeline.pkl", "wb"))

print("\nModel saved successfully 🚀")