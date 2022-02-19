import pandas as pd, os
import matplotlib.pyplot as plt

path = "archive/heart.csv"

x = lambda a : pd.read_csv(a) 


data = x(path)

print(data.head())
print(data.shape)


# plt data 


data.hist(bins=50,figsize=(20,15))
plt.savefig("assets/images/data_visualize")
plt.show()
