# **Spam Email Detection**
Overview

This project implements a Spam Email Detection system using Natural Language Processing (NLP) and Machine Learning. The model is trained using a dataset of emails labeled as either 'ham' (not spam) or 'spam'. The system leverages TF-IDF vectorization and a Naive Bayes classifier for text classification.

## Features

Preprocessing of email text (conversion to lowercase, removal of stop words, and n-gram extraction)

TF-IDF vectorization for feature extraction

Hyperparameter tuning using GridSearchCV

Training and evaluation of a Naive Bayes classifier

Function to classify new emails as spam or ham

Model serialization using joblib

## Requirements

Ensure you have the following dependencies installed:

pip install pandas scikit-learn joblib

## Dataset

The dataset used in this project is mail_data.xls, which contains email messages labeled as 'ham' or 'spam'. The dataset is preprocessed and split into training and testing sets.

## Installation & Usage

Clone this repository:

git clone https://github.com/yourusername/spam-email-detection.git
cd spam-email-detection

Run the script to train the model:

python spam_email_detection.py

To classify a new email, use the classify_new_email function:

from joblib import load

best_nb_classifier = load('spam_email_detection.pkl')

def classify_new_email(email, vectorizer, model):
    email_tfidf = vectorizer.transform([email])
    result = model.predict(email_tfidf)
    return 'spam' if result == 1 else 'ham'

new_email = "You have won 5 lottery coupons!"
print(f"This email is {classify_new_email(new_email, tfidf_vectorizer, best_nb_classifier)}!")

## Model Performance

The model achieved:

Training Accuracy: 100%

Test Accuracy: 99%

Saving and Loading the Model

The trained model is saved as spam_email_detection.pkl and can be loaded for future use:

import joblib
model = joblib.load('spam_email_detection.pkl')

Author

Developed by Riddhi Shah
