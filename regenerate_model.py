"""
Regenerate iris_model.pkl with compatible library versions for PythonAnywhere
Run this script after installing numpy==1.24.3 and scikit-learn==1.3.2
"""

# import the necessary libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import pickle

print(f"Using numpy version: {np.__version__}")
print(f"Using scikit-learn version: {__import__('sklearn').__version__}")

# Load the dataset
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
data = pd.read_csv(url, names=column_names)

# Preprocess the data
X = data.drop('class', axis=1)
y = data['class']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the Decision Tree Classifier
dtree = DecisionTreeClassifier(random_state=42)
dtree.fit(X_train, y_train)

# Save model to file
with open('iris_model.pkl', 'wb') as file:
    pickle.dump(dtree, file)

print("\n✓ Model has been regenerated and saved as 'iris_model.pkl'")
print("✓ This model is now compatible with PythonAnywhere")
print(f"✓ Model accuracy on test set: {dtree.score(X_test, y_test):.2%}")
