import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
import joblib

# Load dataset
df = pd.read_csv("your_dataset.csv")

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df['TEXT'], df['LABEL'], test_size=0.2, random_state=42)

# Define pipeline
pipeline = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('clf', RandomForestClassifier()) # You can replace this with any other classifier
])

# Train model
pipeline.fit(X_train, y_train)

# Evaluate model
predictions = pipeline.predict(X_test)
print(classification_report(y_test, predictions))

# Save the model
joblib.dump(pipeline, 'fraud_detection_model.pkl')
