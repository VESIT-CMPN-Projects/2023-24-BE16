import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import joblib

# Load the dataset
df = pd.read_csv('poverty_prediction.csv')

# Define features and target variable
X = df.drop('Poverty_Status', axis=1)
y = df['Poverty_Status']

# Define categorical and numerical columns
categorical_cols = ['Education_Level', 'Employment_Type', 'Access_to_Healthcare', 'Access_to_Employment', 
                    'Access_to_Education', 'Access_to_Sanitation', 'Access_to_Water', 'Access_to_Internet',
                    'Household_Ownership']
numeric_cols = [col for col in X.columns if col not in categorical_cols]

# Define preprocessing steps
numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='mean')),  # Replace missing values with mean
    ('scaler', StandardScaler())  # Standardize features
])

categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),  # Replace missing values with most frequent
    ('onehot', OneHotEncoder(handle_unknown='ignore'))  # One-hot encode categorical variables
])

# Combine preprocessing steps for numerical and categorical features
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_cols),
        ('cat', categorical_transformer, categorical_cols)
    ])

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define the pipeline with preprocessing and model training steps
pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', RandomForestClassifier(n_estimators=100, random_state=42))
])

# Train the model
pipeline.fit(X_train, y_train)

# Make predictions on the test set
y_pred = pipeline.predict(X_test)

# Save the trained model as .sav file
joblib.dump(pipeline, 'trained_random_forest_model.sav')

def predict_poverty_status(input_features):
    # Load the columns used in training
    columns_used_in_training = X.columns

    # Make sure the input features have the same columns as the training data
    input_data = pd.DataFrame([input_features], columns=columns_used_in_training)

    # Preprocess the input features
    preprocessed_input = pipeline.named_steps['preprocessor'].transform(input_data)

    # Predict the poverty status
    predicted_status = pipeline.named_steps['classifier'].predict(preprocessed_input)

    return predicted_status[0]


# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Print classification report
print("Classification Report:")
print(classification_report(y_test, y_pred))