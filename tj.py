import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
from sklearn import linear_model
Carbon_Prediction = linear_model.LinearRegression()

x = [[1990], [2000], [2017], [2015],[2016], [2017], [2018]]
y = [[696.5],	[612.9], [519.7],	[472.0],	[458.7],
    [455.7],	[402]]
Carbon_Prediction.fit(x,y)

plt.scatter(x, y, color='black')
y_pred = Carbon_Prediction.predict(x)

plt.plot(x, y_pred, color ='blue', linewidth=3)
plt.show()

