💳 Fraud Detection Classification

📌 About the Project

Fraud Detection Classification is a Machine Learning project that predicts whether a financial transaction is fraudulent or genuine based on transaction-related features.

The project uses classification algorithms and provides a user-friendly Streamlit web application for making predictions.

🎯 Objective

The objective of this project is to build a machine learning model that can identify potentially fraudulent transactions and help reduce financial fraud.

🤖 Machine Learning Algorithms

- Naive Bayes
- K-Nearest Neighbors (KNN)
- Logistic Regression

📊 Features Used

The dataset contains features related to:

- Transaction Amount
- Merchant Category
- Card Type
- Authentication Method
- Channel
- Device Type
- Hours Since Last Transaction
- Transaction Count in Last 24 Hours
- Distance From Home
- Card Age
- Customer Age
- Account Balance
- Velocity Score
- Time of Day
- Day of Week
- Merchant Risk Score
- Prior Disputes

Target Variable

"is_fraud"

- "0" → Genuine Transaction
- "1" → Fraudulent Transaction

🔄 Workflow

Dataset
   ↓
Data Understanding
   ↓
Data Cleaning
   ↓
Missing & Duplicate Value Check
   ↓
Feature Selection
   ↓
Train-Test Split
   ↓
Model Training
   ↓
Model Evaluation
   ↓
Model Saving using Pickle
   ↓
Streamlit Deployment

🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Pickle
- Streamlit
- Jupyter Notebook
- GitHub

📁 Project Structure

Fraud_Detection_Classification/
│
├── app.py
├── fraud_detection.ipynb
├── model.pkl
├── requirements.txt
└── README.md

🚀 How to Run

1. Clone the repository

git clone YOUR_GITHUB_REPOSITORY_URL

2. Navigate to the project folder

cd Fraud_Detection_Classification

3. Install dependencies

pip install -r requirements.txt

4. Run the Streamlit application

streamlit run app.py

🌐 Streamlit App

The Streamlit application allows users to enter transaction details and predicts whether the transaction is fraudulent or genuine.

📈 Model Evaluation

The classification models are evaluated using metrics such as:

- Accuracy
- Confusion Matrix
- Precision
- Recall
- F1-Score

👩‍💻 Author

Sofiya

B.Tech – Artificial Intelligence & Machine Learning
