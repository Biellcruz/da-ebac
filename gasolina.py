import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('gasolina.csv')
print(df)

df.plot(x='dia', y='venda', kind='line')
plt.savefig('gasolina.png')