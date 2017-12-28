import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression



df = pd.read_csv('train.csv',usecols=['LotArea','SalePrice'])



LotArea = df['LotArea']
LotArea =  np.array(LotArea).reshape((1460, -1))
SalePrice = df['SalePrice']
SalePrice = np.array(SalePrice).reshape((1460, -1))

model = LinearRegression()
model.fit(LotArea, SalePrice)

plt.scatter(LotArea, SalePrice,color='r')

plt.plot(LotArea, model.predict(LotArea),color='k')

plt.show()

