import csv
import time
import pandas as pd
from collections import Counter
from matplotlib import pyplot as plt

data = pd.read_csv('Satelite_Channel_List1.csv')
category = data['Category']

cat_counter = Counter()

for name in category:
    cat_counter.update(name.split('\n'))

num = []
genre = []

for item in cat_counter.most_common(15):
    genre.append(item[0])
    num.append(item[1])

num.reverse()
genre.reverse()

plt.style.use('fivethirtyeight')

plt.barh(genre, num)

plt.title('Number of Channels per Genre')
plt.ylabel('Genre')
plt.xlabel('# Channels')

plt.tight_layout()

plt.show()