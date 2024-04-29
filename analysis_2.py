import pandas as pd
import numpy as np
import scipy as sp

df = pd.read_csv(r"C:\Users\Pranat\Dropbox\PC\Documents\Analysis\sales-data-set-_1_.csv")
ds = df['Date']
sales = df['Weekly_Sales']
x = np.array(df['Date'])
y = np.array(df['Weekly_Sales'])
XY = np.array([x,y])

D = {}
for i in ds:
	D[i] = 0

# CORE ######################################### SIZE MUST BE SAME AND THERE MUST BE A CORRESPONDENCE BETWEEN LISTS..
for el_index in range(len(x)):
	if D[x[el_index]] == D[x[el_index]]:
		D[x[el_index]] += y[el_index]
	else:
		D[x[el_index]] = y[el_index]
###############################################

#print(D.items()) ## gives list of tuples 
try:
	D_ = {"ds": D.keys(), "y":D.values()}
except Exception as e:
	print(e)  
D_n = pd.DataFrame.from_dict(D_)
print(D_n)
D_n.to_csv(r"C:\Users\Pranat\Dropbox\PC\Documents\Analysis\cleaned_sales_data.csv")


######## WANT: D to be our new data frame. So, we want D as new csv file and then reuploaded to perform analysis.












#D_keys = list(D.keys())

# result = {}

# for i in D_keys:
# 	result[D[i]] = i;print(result)
# 	for j in D_keys[D_keys.index(i):]:
# 		if i == j:
# 			a += D[j] ## it is adding keys of dict with same keys, we want it to add values with the same key in the dict.
# 			print(a)
# 		else:
# 			break
# 	break
