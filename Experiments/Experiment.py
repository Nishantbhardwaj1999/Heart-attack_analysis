#import statements
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import pickle

#import DataSet
file_Path="D:\machineLearning\heart_attack_analysis\heart_health.csv"
heart_attack_df=pd.read_csv(file_Path)

#checking data set 
heart_attack_df.info()

#check data Indepth
heart_attack_df.sample()

#dealing with categorical Columns
mapping = {'M': 1, 'F': 0}
heart_attack_df['Sex'] = heart_attack_df['Sex'].replace(mapping)

mapping = {'Normal': 0, 'ST': 1, 'LVH': 2}
heart_attack_df['RestingECG'] = heart_attack_df['RestingECG'].replace(mapping)

mapping = {'Up': 0, 'Flat': 1, 'Down': 2}
heart_attack_df['ST_Slope'] = heart_attack_df['ST_Slope'].replace(mapping)

mapping = {'N': 0, 'Y': 1}
heart_attack_df['ExerciseAngina'] = heart_attack_df['ExerciseAngina'].replace(mapping)

mapping = {'ATA': 0, 'NAP': 1,"ASY":2,"TA":3}
heart_attack_df['ChestPainType'] = heart_attack_df['ChestPainType'].replace(mapping)

heart_attack_df.info()

# Split features and target variable
X = heart_attack_df.drop(columns=["HeartDisease"])
y = heart_attack_df["HeartDisease"]


# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Feature scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Initialize the model
model = RandomForestClassifier()

# Train the model
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)


# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
print(classification_report(y_test, y_pred))

#saving pickle file
with open('model.pkl', 'wb') as model_file:
    pickle.dump(model, model_file)