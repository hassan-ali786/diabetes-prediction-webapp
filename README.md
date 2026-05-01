# Healthcare Disease Prediction Web Application

An end-to-end Machine Learning web application that predicts the likelihood of diabetes using clinical health parameters. The system leverages supervised learning techniques and provides real-time predictions through a Flask-based web interface.

---

## Project Overview

This application analyzes patient health metrics and predicts diabetes risk while following a complete machine learning lifecycle:

- Data preprocessing and feature scaling  
- Model training using XGBoost Classifier  
- Model evaluation using Precision, Recall, F1-score, and Accuracy  
- Deployment using Flask  
- Professional frontend integration for real-time predictions  

---

## Machine Learning Model

**Algorithm:** XGBoost Classifier  

### Why XGBoost

- High performance on structured datasets  
- Handles complex feature relationships  
- Strong generalization capability  
- Better accuracy compared to traditional models  

---

## Dataset Information

**Dataset:** Pima Indian Diabetes Dataset  
(National Institute of Diabetes and Digestive and Kidney Diseases)

### Features

- Pregnancies  
- Glucose Level  
- Blood Pressure  
- Skin Thickness  
- Insulin Level  
- BMI  
- Diabetes Pedigree Function  
- Age  

**Target:**  
Outcome (0 = No Diabetes, 1 = Diabetes)

---

## Model Performance Metrics

| Metric     | Value |
|------------|-------|
| Accuracy   | 75%   |
| Precision  | 0.74  |
| Recall     | 0.72  |
| F1-Score   | 0.73  |

### Metric Explanation

- **Accuracy:** Overall correct predictions  
- **Precision:** Correctly predicted positive cases  
- **Recall:** Ability to detect actual positive cases  
- **F1-Score:** Balance between Precision and Recall  

---

## Project Structure

```bash
Diabetes-Disease-Prediction/
├── app/
│   └── app.py
│
├── models/
│   ├── diabetes_model.pkl
│   └── scaler.pkl
│
├── dataset/
│   └── pima_diabetes.csv
│
├── static/
│   └── style.css
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── screenshots/
│   └── homepage.png
│
├── train_model.py
├── requirements.txt
├── .gitignore
└── README.md

```


## Installation Guide

### 1. Clone the Repository

```bash
git clone https://github.com/hassan-ali786/Healthcare-Disease-Prediction.git
cd Healthcare-Disease-Prediction
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Train the Model

```bash
python train_model.py
```

### 4. Run the Application

```bash
python app.py
```

Open your browser and navigate to:

```
http://127.0.0.1:5000
```

---

## Key Features

- Real-time diabetes prediction  
- Professional healthcare interface  
- Machine Learning integration using XGBoost  
- Evaluation using Accuracy, Precision, Recall, and F1-score  
- Modular and production-ready architecture  

---

## Technology Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=flat&logo=flask&logoColor=white)
![XGBoost](https://img.shields.io/badge/XGBoost-FF6600?style=flat)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=flat&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat&logo=numpy&logoColor=white)

---

## Real-World Applications

- Hospitals and clinics  
- Telemedicine platforms  
- Healthcare AI solutions  
- Medical research and analytics  

---

## Future Improvements

- Integration with LightGBM for comparison  
- Explainable AI (SHAP values)  
- User authentication system  
- Cloud deployment (AWS, Render, Docker)  
- REST API development  
- Database integration for patient records  
- Multi-disease prediction system  

---

## Author

Hassan Ali  
Data Scientits And Machine Learning Engineer
GitHub: https://github.com/hassan-ali786  

---

## Application Screenshot

![Home Page](screenshots/homepage.png)
