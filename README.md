# ai-career-suggestion-tool
AI-powered Career Suggestion Tool using Machine Learning and Flask that predicts suitable career paths based on user skills and interests with confidence scoring and input validation.
AI Career Suggestion Tool is a machine learning–based web application that predicts suitable career paths based on user-provided skills and interests. The system uses Natural Language Processing (NLP) techniques and a multi-class classification model to analyze input text and generate career recommendations with confidence scoring and input validation.
---
## Project Overview
This project demonstrates the practical implementation of:
- Text preprocessing
- TF-IDF feature extraction
- Multi-class classification
- Probability-based confidence scoring
- Input validation and filtering
- Flask-based web deployment
The application allows users to enter their skills and interests in natural language format. The model processes the input and predicts the most relevant career domain.
---
## Key Features
- Career prediction based on skills and interests
- Confidence percentage display
- Intelligent validation to reject invalid or meaningless inputs
- Clean, responsive user interface
- Modular project structure
- Ready for deployment
---
## Technical Stack
- Python
- Flask
- Scikit-learn
- Pandas
- NumPy
- TF-IDF Vectorizer
- Logistic Regression
---
## How It Works
1. The user enters skills and interests.
2. The input text is combined and transformed using TF-IDF vectorization.
3. A trained Logistic Regression classifier predicts the most suitable career category.
4. Prediction probabilities are calculated.
5. If the confidence score is below a defined threshold, the system rejects the input as unclear.
6. Otherwise, the predicted career and confidence percentage are displayed.
---
## Model Details
- Algorithm: Logistic Regression
- Feature Extraction: TF-IDF
- Classification Type: Multi-class classification
- Confidence Filtering: Probability threshold-based validation
- Additional Validation: Regex-based repetitive input detection
---
## Project Structure
ai-career-suggestion-tool/
│
├── app.py
├── requirements.txt
│
├── model/
│ ├── career_model.pkl
│ └── label_encoder.pkl
│
├── data/
│ └── dataset.csv
│
├── templates/
│ └── index.html
│
└── README.md
---
## Installation and Setup
https://github.com/Awikumari/ai-career-suggestion-tool/edit/main/README.md
## 
Create a virtual environment:
python -m venv venv
venv\Scripts\activate (Windows)
## 
Install dependencies: pip install -r requirements.txt
Run the application: 
python app.py
## 
Open in browser:
http://127.0.0.1:5000
---
## Validation Logic
The system prevents unreliable predictions by:
- Rejecting repeated or spam-like inputs (e.g., aaaaaaaa)
- Rejecting extremely short or meaningless text
- Blocking predictions when confidence probability is below threshold
This ensures more realistic and reliable career recommendations.
---
## Future Enhancements
- Top 3 career recommendations
- Confidence visualization graph
- Resume-based career prediction
- Deployment on cloud platforms
- User authentication and profile saving
---
## Author
Awi Kumari  
