import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
font_path = "C:/Windows/Fonts/NGULIM.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)


df_my_index = pd.read_csv('c:/big-data/carbon point 20210900.csv', index_col=0, encoding = 'cp949', sep = ',', thousands = ',')

df_my_index['참여가구'].plot(kind='bar', color=('b'))

plt.show()