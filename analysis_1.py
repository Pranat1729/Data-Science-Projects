import pandas as pd
import numpy as np
from scipy import stats

df = pd.read_csv(r"C:\Users\Pranat\Documents\Analysis\Features-data-set_1_-_2_.csv")
MarkDown_1 = df['MarkDown1']
print(MarkDown_1)
MarkDown_2 = df['MarkDown2']
MarkDown_3 = df['MarkDown3']
MarkDown_4 = df['MarkDown4']
MarkDown_5 = df['MarkDown5']
IsHoliday = df['IsHoliday']

#list_1 = df['Markdown1'].tolist()
x = np.array(df['MarkDown1'])
y = np.array(df['MarkDown2'])
z = np.array(df['MarkDown3'])
n = np.array(df['MarkDown4'])
m = np.array(df['MarkDown5'])
a = np.array(df['IsHoliday'])
A = [x,y,z,n,m]
B=[]
for i in range(len(A)):
	b = stats.pointbiserialr(A[i],a) 
	#print(b)
	B.append(b)
print(B)
#a = stats.pointbiserialr(x,a) 
#print(a)
