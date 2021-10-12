import pandas as pd
import matplotlib.pyplot as plt


df_my_index = pd.read_csv('c:/big-data/carbon point 20200831.csv', index_col=0, encoding = 'cp949')

df_my_index['합계 (세대수)'].plot(kind='bar', color=('b', 'darkorange', 'g', 'r', 'm'))
plt.show()

