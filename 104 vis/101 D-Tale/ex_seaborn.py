import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_excel('CN.xlsx', sheet_name='Sheet1')

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

fig, ax = plt.subplots(figsize=(8, 6))
fig.subplots_adjust(right=0.75)  # reserving space for the 3rd y-axis
ax2 = ax.twinx()
ax3 = ax.twinx()
ax3.spines.right.set_position(("axes", 1.2))  # move the 3rd y-axis outside
sns.set()
sns.set_style('ticks')
sns.set_context('paper')

p1 = sns.lineplot(data=df, x="Date", y="M2", color="orange", linewidth=5, ax=ax)
ax.lines[0].set_linestyle("--")
p2 = sns.lineplot(data=df, x="Date", y="Sh index", color="red", ax=ax2)
p3 = sns.lineplot(data=df, x="Date", y="Real Estate", color="blue", ax=ax3)

fig.legend(labels=["M2", "sh index", "Real Estate"], loc="upper left", bbox_to_anchor=(0,1), bbox_transform=ax.transAxes)
ax.set_title('The influence of M2')
plt.show()
