import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
from sklearn import linear_model
Carbon_Prediction = linear_model.LinearRegression()


x = [[2019], [2020], [2021]]
y = [[66.12],[54.71],[60.37]]
Carbon_Prediction.fit(x,y)

plt.scatter(x, y, color='black')
y_pred = Carbon_Prediction.predict(x)

plt.plot(x, y_pred, color ='blue', linewidth=3)
plt.show()