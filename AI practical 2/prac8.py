'''Aim:- Implement the K-NN Algorithm for classification or regression.
Apply K-NN Algorithm on the given dataset & predict the class or value for test data.'''


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, classification_report, roc_curve, roc_auc_score

df = pd.read_csv('AI practical 2/datasets/diabetes.csv')

X = df.drop('Outcome', axis=1).values
y = df['Outcome'].values

# Creating a train-test split for the model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42)

# Implementing KNN algorithm
neighbors = np.arange(1, 9)
train_accuracy = np.empty(len(neighbors))
test_accuracy = np.empty(len(neighbors))

for i, k in enumerate(neighbors):
    # Setup a KNN classifier with k neighbors
    knn = KNeighborsClassifier(n_neighbors=k)
    # Fit the model
    knn.fit(X_train, y_train)
    # Compute the accuracy on the training set
    train_accuracy[i] = knn.score(X_train, y_train) 
    # Compute accuracy on the test set
    test_accuracy[i] = knn.score(X_test, y_test)

# Visualizing the KNN in graph
plt.title("KNN Varying Number of Neighbors")
plt.plot(neighbors, test_accuracy, label='Testing Accuracy', marker='o')
plt.plot(neighbors, train_accuracy, label='Training Accuracy', marker='o')
plt.legend()
plt.xlabel('Number of Neighbors')
plt.ylabel('Accuracy')
plt.xticks(neighbors)
plt.grid()
plt.show()

# Fit the KNN model with n_neighbors = 7
knn = KNeighborsClassifier(n_neighbors=7)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)

# Confusion matrix
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:\n", cm)

# Display classification report
print("Classification Report:\n", classification_report(y_test, y_pred))

# Predict probabilities
y_pred_proba = knn.predict_proba(X_test)[:, 1]

# Calculate ROC curve
fpr, tpr, thresholds = roc_curve(y_test, y_pred_proba)

# Plot ROC curve
plt.plot([0, 1], [0, 1], 'k--')  # Diagonal line
plt.plot(fpr, tpr, label='KNN (n_neighbors = 7)')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve for KNN (n_neighbors = 7)')
plt.legend()
plt.show()

# Calculate and print ROC AUC score
roc_auc = roc_auc_score(y_test, y_pred_proba)
print("ROC AUC Score: ", roc_auc)

# Hyperparameter tuning using GridSearchCV
param_grid = {'n_neighbors': np.arange(1, 50)}  # Corrected parameter grid

knn = KNeighborsClassifier()
knn_cv = GridSearchCV(knn, param_grid, cv=5)
knn_cv.fit(X_train, y_train)  # Fit on training data
print("Best Score from Grid Search: ", knn_cv.best_score_)
print("Best Parameters from Grid Search: ", knn_cv.best_params_)
