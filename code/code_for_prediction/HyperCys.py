#!/usr/bin/env python
# coding: utf-8
import numpy as np
import pandas as pd
import pickle as pk
import math
import lightgbm as lgb
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from lightgbm import LGBMClassifier
from mlxtend.classifier import StackingCVClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import roc_curve, roc_auc_score, accuracy_score, precision_score, confusion_matrix, recall_score, f1_score, auc, matthews_corrcoef
from imblearn.pipeline import make_pipeline
from sklearn.ensemble import ExtraTreesClassifier
from sklearn import preprocessing
import joblib


covalent = pd.read_excel('D:/HyperCys/data/train_dataset.xlsx')

X=covalent.loc[:, covalent.columns!= 'label']
y=covalent['label']

scaler = StandardScaler()
X = scaler.fit_transform(X)
print('data scaled')

classifier1 = SVC(C=100,  gamma= 0.001, kernel="sigmoid",probability=True,random_state=42)

classifier2 = KNeighborsClassifier(9)

classifier3 = LogisticRegression(C=0.1)

classifier4 = lgb.LGBMClassifier(colsample_bytree=0.3,max_depth=15,n_estimators=100, num_leaves=50)

classifier5=MLPClassifier(alpha= 10, hidden_layer_sizes=(50, 50, 50), learning_rate='adaptive', solver='adam')

classifier6= RandomForestClassifier(criterion="gini", max_depth= 3000, min_samples_split= 4, n_estimators= 80) # Define classifier
# stacked classifier
clf = StackingCVClassifier(classifiers = [make_pipeline(scaler, classifier1), make_pipeline(scaler, classifier2), make_pipeline(scaler,  classifier3), make_pipeline(scaler,  classifier4), make_pipeline(scaler,  classifier5), make_pipeline(scaler,  classifier6)],
							shuffle = False,
							use_probas = True,
							cv = 10,
						   verbose=2,
						   n_jobs=-1,
							store_train_meta_features = True,
							use_features_in_secondary =True,
							meta_classifier =make_pipeline(scaler, LogisticRegression(C=0.1))
)


clf.fit(X,y)
print('model file created')
print('saving model file in disk')
modelfile = 'D:/HyperCys/model/hypercys.model'
joblib.dump(clf, modelfile)
print('model file saved')



test_df = pd.read_excel('D:/HyperCys/data/test_dataset.xlsx')
X_test = test_df
X_test = scaler.transform(X_test) 

y_pred = clf.predict(X_test)
y_pred_prob = clf.predict_proba(X_test)
y_pred = np.column_stack([y_pred, y_pred_prob])

output_file = 'D:/HyperCys/model/prediction.predict'
out_file = open(output_file, 'wb')
np.savetxt(fname=output_file, X=y_pred, fmt='%d %0.4f %0.4f', header='predClass, probNonCov, probCov', comments='')






