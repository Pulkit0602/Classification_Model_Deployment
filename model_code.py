# Import necessary libraries
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Generate or load your dataset
# For this example, let's use the built-in Iris dataset for classification.
from sklearn.datasets import load_iris
data = load_iris()
X, y = data.data, data.target

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Random Forest classifier[]
rf_classifier = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42)
# Train the classifier on the training data
rf_classifier.fit(X_train, y_train)

# Make predictions on the test data
y_pred = rf_classifier.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred, target_names=data.target_names)

print(f"Accuracy: {accuracy:.2f}")
print(report)


import pickle

# Save the trained Random Forest model to a file
with open('random_forest_model.pkl', 'wb') as model_file:
    pickle.dump(rf_classifier, model_file)
