from django.db import models

# Create your models here.
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split, cross_val_score
from joblib import dump
import joblib

# Read your dataset
data = pd.read_csv('farming_dataset.csv')

# Split the data into features (X) and target variable (y)
X = data.drop('Farming_Income', axis=1)
y = data['Farming_Income']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define the preprocessing steps
numeric_features = X.select_dtypes(include=['int64', 'float64']).columns
categorical_features = X.select_dtypes(include=['object']).columns

numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='mean'))
])

categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)
    ])

# Create the model pipeline
trained_model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', RandomForestRegressor(n_estimators=100, random_state=42))
])

# Fit the model on the training data
trained_model.fit(X_train, y_train)


# Function to predict farming income for new input features
def predict_farming_income_function(input_features):

    columns_used_in_training = X.columns

    # Make sure the input features have the same columns as the training data
    input_data = pd.DataFrame([input_features], columns=columns_used_in_training)
    # input_data = pd.DataFrame([input_features], columns=X.columns)
    print(input_data)

    # Preprocess the input features
    preprocessed_input = trained_model.named_steps['preprocessor'].transform(input_data)

    # Predict the farming income
    predicted_income = trained_model.named_steps['regressor'].predict(preprocessed_input)

    return predicted_income[0]

filename='finalized_model.sav'
joblib.dump(trained_model,filename)