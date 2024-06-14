import numpy as np
import pandas as pd
from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.models import BayesianNetwork
from pgmpy.inference import VariableElimination

makecall = pd.read_csv('C:/Users/bharg/OneDrive/Desktop/2_2sem metiral\AI/Data.csv')

print('sample instances from the dataset are given below')
print(makecall.head())
print('\nAttributes and datatypes')
print(makecall.dtypes)

model = BayesianNetwork([('Burglary', 'Alarm'), ('Earthquake', 'Alarm'), ('Alarm', 'jhoncalls'), ('Alarm', 'marycalls')])
print('\nLearning CPD using maximum likelihood estimation')
model.fit(makecall, estimator=MaximumLikelihoodEstimator)

print('\nInferencing with Bayesian Network:')
makecall_infer = VariableElimination(model)

print('\n1. Probability of making a phone call given evidence=Alarm')
q1 = makecall_infer.query(variables=['jhoncalls'], evidence={'Alarm': 1})
print(q1)

print('\n2. Probability of making a phone call given evidence=Alarm')
q2 = makecall_infer.query(variables=['marycalls'], evidence={'Alarm': 1})
print(q2)

print('\n3. Probability of making a phone call given evidence=Burglary')
q3 = makecall_infer.query(variables=['jhoncalls'], evidence={'Burglary': 1})
print(q3)

print('\n4. Probability of making a phone call given evidence=Burglary')
q4 = makecall_infer.query(variables=['marycalls'], evidence={'Burglary': 1})
print(q4)
