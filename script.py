# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np
from sklearn import preprocessing

# Opening the dataframe
df = pd.read_csv('Data.csv')

print(df.head())

# Assigning the target variable
Y = df['income_n']

X = df.drop(['income_n'], axis='columns')

# Splitting the data 
import sklearn as sk
from sklearn.model_selection import train_test_split

# Here, I have split the data into ratio 70:35
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=42)

X_train.shape

# Random Forrest Classifier
from sklearn.ensemble import RandomForestClassifier


rf = RandomForestClassifier(criterion = "gini")
rftree = rf.fit(X_train, y_train)
rftree

print("Accuracy on the training subsets: {:.3f}".format(rftree.score(X_train, y_train)))
print("Accuracy on the test subsets: {:.3f}".format(rftree.score(X_test, y_test)))

# Saving model to disk
import pickle
pickle.dump(rf, open('model.pkl', 'wb'))

# Loading model to campare the results
model = pickle.load(open('model.pkl', 'rb'))
model
