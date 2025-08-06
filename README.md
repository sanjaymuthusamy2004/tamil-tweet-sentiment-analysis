# 📊 Tamil Tweet Sentiment Analysis using NLP

This project focuses on analyzing and classifying **Tamil tweets** into three sentiment categories: **Positive**, **Negative**, and **Neutral** using **Natural Language Processing (NLP)** techniques and **Machine Learning** models.

---

## 📌 Overview

🚀 **Goal**: Build a sentiment analysis system for Tamil-language tweets  
🧠 **Models Used**: Random Forest, Support Vector Machine (SVM), Logistic Regression & Naive Bayes  </br>
🛠️ **Tech Stack**: Python, Scikit-learn, TF-IDF, Pandas, Matplotlib  
💬 **Language**: Tamil  
📈 **Classification Output**: `Positive`, `Neutral`, `Negative`  

---

## 🧠 Technologies & Tools Used

| Category             | Tools / Libraries                                           |
|----------------------|-------------------------------------------------------------|
| Programming Language | Python                                                      |
| NLP Techniques       | Text preprocessing, TF-IDF vectorization                    |
| ML Algorithms        | Random Forest, SVM (Support Vector Machine), Logistic Regression & Naive Bayes                 |
| Model Optimization   | GridSearchCV                                                |
| Data Handling        | Pandas, NumPy                                               |
| Visualization        | Matplotlib                                                  |
| Model Serialization  | Joblib (`.pkl` files)                                       |

---

## 🗃️ Project Files & Descriptions

| File Name                     | Description                                                                 |
|------------------------------|-----------------------------------------------------------------------------|
| `Twitter_tamil_Analysis.csv` | The main dataset containing Tamil tweets with sentiment labels              |
| `rf_sentiment_model.pkl`     | Trained **Random Forest** sentiment classification model                    |
| `svm_sentiment_model.pkl`    | Trained **SVM** sentiment classification model                              |
| `lr_sentiment_model.pkl`     | Trained **Logistic Regression** sentiment classification model                    |
| `nb_sentiment_model.pkl`     | Trained **Naive Bayes** sentiment classification model                              |
| `tfidf_vectorizer.pkl`       | **TF-IDF vectorizer** used to convert text to numerical features            |
| `sentiment_analysis.py`      | Python script for model training, evaluation, and predictions *(create this)*|


---

## 🧪 How the Project Works

1. **Data Loading**: Import the Tamil tweets dataset (`Twitter_tamil_Analysis.csv`)
2. **Text Preprocessing**: Clean and normalize the text (removal of punctuations, lowercasing, etc.)
3. **Vectorization**: Use TF-IDF to convert cleaned text into numerical format
4. **Model Training**: Train the **Random Forest**, **SVM**, **Logistic Regression** & **Naive Bayes** Logistics classifiers
5. **Evaluation**: Assess the model using accuracy, F1-score, and confusion matrix
6. **Model Saving**: Save the trained models and TF-IDF vectorizer using Joblib
7. **Future Prediction**: Load `.pkl` files and predict sentiment of new Tamil tweets


---

## 📊 Model Evaluation Results

| Model                | Accuracy | F1 Score |
|---------------------|----------|----------|
| Random Forest        | 85%      | 0.84     |
| SVM                  | 82%      | 0.81     |
| Logistic Regression  | 80%      | 0.79     |
| Naive Bayes          | 76%      | 0.75     |



---

## 🌐 Real-World Applications

- 🗳️ **Election sentiment analysis** — Understand public opinion in Tamil Nadu elections  
- 🛍️ **Product reviews** — Analyze customer reviews for Tamil-speaking audiences  
- 💬 **Customer feedback systems** — Monitor sentiment from Tamil social platforms  
- 📢 **Social trend monitoring** — Track trending topics and sentiments in Tamil tweets  

---


## 🔧 Setup Instructions

### ✅ Prerequisites
Make sure you have the following installed:
- Python 3.7+
- pip (Python package installer)

### 📦 Install Dependencies
Create a virtual environment (optional) and install dependencies:
```bash
pip install -r requirements.txt
