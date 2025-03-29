import pandas as pd 
import numpy as np 
import os
df = pd.read_csv('https://raw.githubusercontent.com/yogibaba7/EndToEndMlproject/refs/heads/main/artifacts/train.csv')

df = df[['gender','lunch','math_score','reading_score','writing_score']]

df = df[df['math_score']>70]

df.to_csv(os.path.join('data','students.csv'))