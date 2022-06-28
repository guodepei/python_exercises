import dtale
import pandas as pd

if __name__ == '__main__':
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

      dtale.show(df, subprocess=False, open_browser=True)