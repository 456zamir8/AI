'''Aim: Implement the SVM algorithm for binary classification.
    Train a SVM Model using the given datasets.
    Evaluate the performance on test data and analyze the results.'''


import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv('AI practical 2/datasets/PlayTenis.csv')

# Mapping categorical variables to numbers
df['outlook'] = df['outlook'].map({'overcast': 0, 'rainy': 1, 'sunny': 2}) 
df['temp'] = df['temp'].map({'cool': 0, 'hot': 1, 'mild': 2})
df['humidity'] = df['humidity'].map({'high': 0, 'normal': 1})
df['windy'] = df['windy'].map({'no': 0, 'yes': 1})
df['play'] = df['play'].map({'no': 0, 'yes': 1})

# Dividing the datasets into dependent and independent variables
X = df[['outlook', 'temp', 'humidity', 'windy']]
y = df['play']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the SVM model
model = SVC(kernel='linear')  # You can choose different kernels like 'rbf', 'poly', etc.
model.fit(X_train, y_train)

# Make predictions on the test data
y_pred = model.predict(X_test)

# Evaluate the performance of the model
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print("\nAccuracy Score:", accuracy_score(y_test, y_pred))

# Visualize the confusion matrix
plt.figure(figsize=(8, 6))
sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt='d', cmap='Blues')
plt.title('Confusion Matrix')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()

