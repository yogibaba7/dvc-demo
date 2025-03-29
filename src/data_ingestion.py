import pandas as pd 
import numpy as np 
import os
df = pd.read_csv('https://raw.githubusercontent.com/yogibaba7/EndToEndMlproject/refs/heads/main/artifacts/train.csv')

df = df[['gender','math_score']]

df.to_csv(os.path.join('data','students.csv'))