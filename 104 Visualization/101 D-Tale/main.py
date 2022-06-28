import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('CN.xlsx', sheet_name='Sheet1')
# print(df)
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
# print(df.head(10))  # View first 10 data rows
# print(df.describe())
# print(df.info())
# print('---')

df.drop(df.head(4).index, inplace=True)
df.drop(df.tail(3).index, inplace=True)
df.columns = ['Date', 'M2', 'M2%', 'Sh index', 'Real Estate', 'Real Estate%']
df['Date'] = pd.to_datetime(df['Date'])
df['M2'] = pd.to_numeric(df['M2'], errors='ignore')
df['M2%'] = pd.to_numeric(df['M2%'], errors='ignore')
df['Sh index'] = pd.to_numeric(df['Sh index'], errors='ignore')
df['Real Estate'] = pd.to_numeric(df['Real Estate'], errors='ignore')
df['Real Estate%'] = pd.to_numeric(df['Real Estate%'], errors='ignore')
format_dict = {'Date': '${:%m-%Y}',
               'M2': '${0:,.2f}', 'M2%': '${:.2%}',
               'Sh index': '${0:,.2f}',
               'Real Estate': '${0:,.2f}', 'Real Estate%': '${:.2%}'}
#print(df.head(10).style.format(format_dict).highlight_max(color='darkgreen').highlight_min(color='#ff0000'))
print(df.head(10).style.format(format_dict).to_html())
print('.\n'*3)
#print(df.tail(10).style.format(format_dict).highlight_max(color='darkgreen').highlight_min(color='#ff0000'))
print(df.tail(10).style.format(format_dict).to_html())
print(df.describe())
print(df.info())
print('---')
# df.style.format(format_dict).to_excel('output.xlsx', 'Sheet1')

plt.plot(df['Date'], df['M2'], 'g^', label='M2%')
plt.plot(df['Date'], df['Sh index']*1000, 'r-', label='Sh index')
plt.plot(df['Date'], df['Real Estate']*100, 'bs', label='Real Estate')
plt.xlabel('Date')
plt.title('M2')
plt.grid(True)
plt.legend()
plt.show()

