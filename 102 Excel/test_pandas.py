import pandas as pd
from pandas import DataFrame

# 3.8.2 pandas读写Excel
def fun3_8_2():
    data = pd.read_excel(r'申万财务模型5.0.4中英文版-20200320.xlsm', sheet_name='公司说明')
    print(data)

    # 增加行数据，在第5行新增
    # data.loc[4] = ['4', 'john', 'pandas']

    # 增加列数据，给定默认值None
    data['new_col'] = None

    # 保存数据
    DataFrame(data).to_excel('new.xlsx', sheet_name='公司说明', index=False, header=True)


if __name__ == '__main__':
    fun3_8_2()