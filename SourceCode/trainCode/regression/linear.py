__author__ = 'wsjswy'


import pandas as pd
from sklearn import  linear_model
import matplotlib.pyplot as plt

# read data
data_name = pd.read_fwf("brain_body.txt")
x_values = data_name[['Brain']]
y_values = data_name[['Body']]

# train model on data
body_reg = linear_model.LinearRegression()
body_reg.fit(x_values, y_values)


#显示结果

plt.scatter(x_values, y_values) #描点
plt.plot(x_values, body_reg.predict(x_values)) # 拟合直线
plt.show() #画图
