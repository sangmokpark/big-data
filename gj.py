import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
from sklearn import linear_model
Carbon_Prediction = linear_model.LinearRegression()


df_y = pd.read_csv('c:/big-data/carbon 20210900 gj.csv', encoding = 'cp949')
x = [[2009],[2019], [2020], [2021]]
y = [[0] ,[66.12],[54.71],[60.37]]
Carbon_Prediction.fit(x,y)

plt.scatter(x, y, color='black')
y_pred = Carbon_Prediction.predict(x)

plt.plot(x, y_pred, color ='blue', linewidth=3)
plt.show()