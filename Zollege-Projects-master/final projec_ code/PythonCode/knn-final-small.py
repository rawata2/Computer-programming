#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 11 18:01:26 2018

@author: Kuldeep Rawat
"""

# Importing the libraries
import glob, os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
os.chdir("C:/Users/kuldeep/Desktop/Cricket data original/knn")
# Write the pattern: pattern
pattern = '*.csv'
# Save all file matches: csv_files
csv_files_name = glob.glob(pattern)

df0 = pd.read_csv(csv_files_name[0])

X = df0.iloc[:, 2:5].values
y = df0.iloc[:, 1].values

'''
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X_1 = LabelEncoder()
X[:, 0] = labelencoder_X_1.fit_transform(X[:, 0])

onehotencoder = OneHotEncoder(categorical_features = [1])
X = onehotencoder.fit_transform(X).toarray()
X = X[:, 0]
'''
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Fitting K-NN to the Training set
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors = 10, metric = 'minkowski', p = 2) #Metric = Minkowski with p=2 is Euclidian Distance
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
#Accuracy
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_test, y_pred)


