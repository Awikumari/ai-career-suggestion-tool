from flask import Flask, render_template, request
import pickle
import numpy as np
import re

app = Flask(__name__)


with open("model/career_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("model/label_encoder.pkl", "rb") as f:
    label_encoder = pickle.load(f)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    skills = request.form["skills"].strip().lower()
    interests = request.form["interests"].strip().lower()

    combined = skills + " " + interests

    

    if not skills or not interests:
        return render_template("index.html",
                               prediction_text="Please enter both skills and interests.")

    
    if re.search(r"(.)\1{4,}", combined):
        return render_template("index.html",
                               prediction_text="Invalid repetitive input detected.")

    
    if len(combined) < 4:
        return render_template("index.html",
                               prediction_text="Please enter meaningful skills and interests.")



    probs = model.predict_proba([combined])[0]

   
    if np.max(probs) < 0.25:
        return render_template("index.html",
                               prediction_text="Input unclear. Please enter more specific skills.")

  
    top3_indices = np.argsort(probs)[-3:][::-1]
    top3_careers = label_encoder.inverse_transform(top3_indices)

    results = []
    for i in range(3):
        career = top3_careers[i]
        confidence = round(probs[top3_indices[i]] * 100, 2)
        results.append({
            "career": career,
            "confidence": confidence
        })

    return render_template("index.html", top3_results=results)


if __name__ == "__main__":
    app.run(debug=True)