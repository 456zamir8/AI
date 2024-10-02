import pandas as pd
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('AI practical 2/datasets/PlayTenis.csv')

# Mapping categorical variables to numbers
df['outlook'] = df['outlook'].map({'overcast': 0, 'rainy': 1, 'sunny': 2}) 
df['temp'] = df['temp'].map({'cool': 0, 'hot': 1, 'mild': 2})
df['humidity'] = df['humidity'].map({'high': 0, 'normal': 1})
df['windy'] = df['windy'].map({'no': 0, 'yes': 1})
df['play'] = df['play'].map({'no': 0, 'yes': 1})

# Dividing the datasets into dependent and independent variables
conditions = ['outlook', 'temp', 'humidity', 'windy']
X = df[conditions]
y = df['play']

# Splitting the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and fit the decision tree
dtree = DecisionTreeClassifier()
dtree.fit(X_train, y_train)

# Predicting on the test set
y_pred = dtree.predict(X_test)

# Evaluating the model's accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy of the decision tree: {accuracy * 100:.2f}%")

# Optional: Visualize the decision tree
plt.figure(figsize=(12, 8))
tree.plot_tree(dtree, filled=True, feature_names=conditions, class_names=['No', 'Yes'], rounded=True)
plt.show()

# Taking user input for prediction
print("\nPlease enter the following details to predict if you can go out to play:")
outlook = input("Outlook (overcast, rainy, sunny): ").strip().lower()
temp = input("Temperature (cool, hot, mild): ").strip().lower()
humidity = input("Humidity (high, normal): ").strip().lower()
windy = input("Windy (yes, no): ").strip().lower()

# Mapping user input to numeric values
outlook_map = {'overcast': 0, 'rainy': 1, 'sunny': 2}
temp_map = {'cool': 0, 'hot': 1, 'mild': 2}
humidity_map = {'high': 0, 'normal': 1}
windy_map = {'no': 0, 'yes': 1}

# Creating a DataFrame for user input
user_input = pd.DataFrame({
    'outlook': [outlook_map.get(outlook)],
    'temp': [temp_map.get(temp)],
    'humidity': [humidity_map.get(humidity)],
    'windy': [windy_map.get(windy)]
})

# Making prediction
prediction = dtree.predict(user_input)

# Displaying the prediction result
if prediction[0] == 1:
    print("Prediction: You can go out to play!")
else:
    print("Prediction: You cannot go out to play.")
