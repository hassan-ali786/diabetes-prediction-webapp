from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

# Load trained pipeline (IMPORTANT: must be same model you trained)
model = pickle.load(open("model/diabetes_pipeline.pkl", "rb"))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():

    try:
        # Get 8 inputs from form
        values = [float(x) for x in request.form.values()]

        preg, glu, bp, skin, ins, bmi, dpf, age = values

        # FEATURE ENGINEERING (must match training)
        bmi_age = bmi * age
        glu_age = glu * age

        # FINAL 10 FEATURES (THIS FIXES YOUR ERROR)
        final_features = np.array([[
            preg,
            glu,
            bp,
            skin,
            ins,
            bmi,
            dpf,
            age,
            bmi_age,
            glu_age
        ]])

        # Prediction
        prediction = model.predict(final_features)[0]
        probability = model.predict_proba(final_features)[0][1]

        # Result
        if prediction == 1:
            result = "Diabetic"
            risk = round(probability * 100, 2)
        else:
            result = "Non-Diabetic"
            risk = round((1 - probability) * 100, 2)

        return render_template(
            "result.html",
            result=result,
            risk=risk
        )

    except Exception as e:
        return f"Error: {str(e)}"


if __name__ == "__main__":
    app.run(debug=True)