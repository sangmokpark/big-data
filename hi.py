import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
font_path = "C:/Windows/Fonts/NGULIM.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

df_avg = pd.read_csv('c:/big-data/carbon 20210900.csv', encoding = 'cp949', index_col=0)
df_my_index = pd.read_csv('c:/big-data/df_avg.csv', index_col=0, encoding = 'cp949', thousands = ',')


df_my_index.plot(kind='bar', color=('b', 'r'))
df_avg.plot(kind='bar', color=('g'))
plt.show()