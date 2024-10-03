AIM: Adaboost Ensemble Learning 
1.Implement the Adaboost algorithm to create an ensemble of weak classifiers.
2.Train the ensemble model on a given dataset and evaluate its performance.
3.Compare the results with individual weak classifiers. 


import pandas as pd
from sklearn import model_selection
from sklearn.ensemble import AdaBoostClassifier


url = r"C:\Users\zamir\zamir\AI\AI practical 2\datasets\car_buying_dataset.csv"
dataframe = pd.read_csv(url)

# Separate features (X) and target variable (Y)
X = dataframe.drop('buy_car', axis=1)
Y = dataframe['buy_car']

# Convert categorical features to numerical form and store the columns
X = pd.get_dummies(X)
feature_columns = X.columns

# Set the parameters for AdaBoost
seed = 7
num_trees = 30

# Set up the AdaBoost model
model = AdaBoostClassifier(n_estimators=num_trees, random_state=seed)

# Fit the model on the entire dataset
model.fit(X, Y)

# Evaluate the model using cross-validation
results = model_selection.cross_val_score(model, X, Y)
print("Cross-Validation Mean Accuracy:", results.mean())

# Function to make predictions based on user input
def predict_car_purchase():
    print("Please enter the following details about the car:")
    
    # Get user input
    price = float(input("Price (in USD): "))
    mileage = float(input("Mileage (in miles): "))
    age = int(input("Age (in years): "))
    engine_size = float(input("Engine Size (in liters): "))
    fuel_type = input("Fuel Type (petrol, diesel, electric): ").lower()
    transmission = input("Transmission (manual, automatic): ").lower()
    
    # Prepare the new data for prediction
    new_data = {
        'price': price,
        'mileage': mileage,
        'age': age,
        'engine_size': engine_size,
        'fuel_type_petrol': 1 if fuel_type == 'petrol' else 0,
        'fuel_type_diesel': 1 if fuel_type == 'diesel' else 0,
        'fuel_type_electric': 1 if fuel_type == 'electric' else 0,
        'transmission_manual': 1 if transmission == 'manual' else 0,
        'transmission_automatic': 1 if transmission == 'automatic' else 0
    }

    # Convert to DataFrame
    new_df = pd.DataFrame([new_data])

    # Ensure the new_df has the same columns as the training data
    new_df = new_df.reindex(columns=feature_columns, fill_value=0)

    # Make the prediction
    prediction = model.predict(new_df)
    return prediction[0]

# Get user prediction
should_buy = predict_car_purchase()
if should_buy == 1:
    print("Recommendation: Yes, you should buy the car!")
else:
    print("Recommendation: No, you should not buy the car.")
