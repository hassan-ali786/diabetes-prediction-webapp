# Healthcare Disease Prediction Web Application

An end-to-end Machine Learning web application that predicts the likelihood of diabetes using clinical health parameters. The system leverages supervised learning techniques and provides real-time predictions through a professional web interface.

---

## Project Overview

This application analyzes patient health metrics and predicts diabetes risk while following a complete machine learning lifecycle:

- Data preprocessing and feature scaling  
- Model training using Random Forest Classifier  
- Model evaluation using Precision, Recall, F1-score, and Accuracy  
- Deployment using Flask  
- Professional frontend integration for real-time predictions  

---

## Machine Learning Model

**Algorithm:** Random Forest Classifier  

### Why Random Forest

- High performance on tabular healthcare datasets  
- Resistant to overfitting  
- Strong generalization capability  
- Stable performance on small datasets  

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
| Accuracy   | 73%   |
| Precision  | 0.71  |
| Recall     | 0.68  |
| F1-Score   | 0.69  |

### Metric Explanation

- **Accuracy:** Overall correct predictions  
- **Precision:** Correctly predicted positive cases  
- **Recall:** Proportion of actual positive cases correctly identified  
- **F1-Score:** Balance between Precision and Recall, critical in healthcare systems  

---

## Project Structure

```
Diabetes-Disease-Prediction/
│
├── model/
│   ├── diabetes_model.pkl
│   ├── scaler.pkl
│   └── metrics.pkl
├── static/
│   └── style.css
├── templates/
│   ├── index.html
│   └── result.html
├── screenshots/
│   └── home_page.png
├── train_model.py
├── app.py
├── requirements.txt
└── README.md
```

---

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
- Professional and user-friendly healthcare interface  
- Machine Learning integration using Random Forest  
- Evaluation using Accuracy, Precision, Recall, and F1-score  
- Modular and production-ready architecture  

---

## Technology Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=flat&logo=flask&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=flat&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat&logo=numpy&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=black)

---

## Real-World Applications

- Hospitals and clinics  
- Telemedicine platforms  
- Healthcare AI solutions  
- Medical research and analytics  

---

## Future Improvements

- Integration with XGBoost and LightGBM for improved accuracy  
- Prediction probability visualization  
- Feature importance visualization  
- User authentication system  
- Cloud deployment (AWS, Render, Docker)  
- REST API development  
- Database integration for patient records  
- Multi-disease prediction system using deep learning  

---

## Author

Hassan Ali  
Data Scientist and Machine Learning Engineer  


## Application Screenshot

![Healthcare Web App](https://github.com/hassan-ali786/Diabetes-Prediction-Webapp/blob/main/screenshots/home_page.png)

---


