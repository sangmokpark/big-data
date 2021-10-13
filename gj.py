import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
from sklearn import linear_model
Carbon_Prediction = linear_model.LinearRegression()


df_y = pd.read_csv('c:/big-data/carbon 20210900 gj.csv', encoding = 'cp949', index_col=0)
x = [[2019], [2020], [2021]]
y = df_y['참여율(%)']
Carbon_Prediction.fit(x,y)

plt.scatter(x, y, color='black')

y_pred =Carbon_Prediction(x)

plt.plot(x, y_pred, color = 'blue', linewidth=3)
plt.show()