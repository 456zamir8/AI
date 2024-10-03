'''AIM: Naive Bayes' Classifier 
1.Implement the Naive Bayes algorithm for classification.
2.Train a Naive Bayes' model using a given dataset and calculate class probabilities.
3.Evaluate the accuracy of the model on test data and analyze the results.'''


import pandas as pd 
import matplotlib.pyplot as plt 
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB, CategoricalNB, GaussianNB
from sklearn.metrics import accuracy_score
import seaborn as sns 
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix, precision_score, recall_score, f1_score
import warnings
from sklearn.exceptions import UndefinedMetricWarning
warnings.filterwarnings("ignore", category=UndefinedMetricWarning)

df = pd.read_csv('AI practical 2\datasets\disease_dataset.csv')

# converting the dataset 
d = {'Step throat': 2, 'Allergy': 0, 'Cold': 1}
df['diagnosis'] = df['diagnosis'].map(d)

# setting the dimention of the plot
# plot for Sore Throat
fig, ax = plt.subplots(figsize = (6, 6))
sns.countplot(x = df['sore_throat'], data = df)
plt.title("Category wise count of 'Sore Throat'")
plt.xlabel("category")
plt.ylabel("Count")
# plt.show()

# plot for Fever
fig, ax = plt.subplots(figsize = (6, 6))
sns.countplot(x = df['fever'], data = df)
plt.title("Category wise count of 'Fever'")
plt.xlabel("category")
plt.ylabel("Count")
# plt.show()

# plot for swollen glands
fig, ax = plt.subplots(figsize = (6, 6))
sns.countplot(x = df['swollen_gland'], data = df)
plt.title("Category wise count of 'Swollen Glands'")
plt.xlabel("category")
plt.ylabel("Count")
# plt.show()

# plot for Congestion
fig, ax = plt.subplots(figsize = (6, 6))
sns.countplot(x = df['congestion'], data = df)
plt.title("Category wise count of 'Congestion'")
plt.xlabel("category")
plt.ylabel("Count")
# plt.show()

# plot for Headache
fig, ax = plt.subplots(figsize = (6, 6))
sns.countplot(x = df['headache'], data = df)
plt.title("Category wise count of 'Headache'")
plt.xlabel("category")
plt.ylabel("Count")
# plt.show()

# catagory wise count of daignosis
fig, ax = plt.subplots(figsize = (6, 6))
sns.countplot(x = df['diagnosis'], data = df)
plt.title("Category wise count of 'Diagnosis'")
plt.xlabel("category")
plt.ylabel("Count")
# plt.show()

X = df.drop('diagnosis', axis = 1)
y = df['diagnosis']

# Training algorithm
classifier = MultinomialNB()
classifier.fit(X, y)

# Training algorithm
classifier = CategoricalNB()
classifier.fit(X, y)

# Training algorithm
classifier = GaussianNB()
classifier.fit(X, y)

# creating a train test for the model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)

# creating a confusion matrix
classifier = MultinomialNB()
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("Accuracy: ", accuracy_score(y_test, y_pred))
print("Precision: ", precision_score(y_test, y_pred, zero_division=0))
print("Recall: ", recall_score(y_test, y_pred, zero_division=0))
print("F1 Score: ", f1_score(y_test, y_pred, zero_division=0))
print("Classification Report:\n", classification_report(y_test, y_pred, zero_division=0))