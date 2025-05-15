# 导入所需的库
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# 读取 Excel 文件
# 修改文件路径和表名为你的实际文件
file_path = 'C:/Users/Jason Shen/Desktop/油藏工程/实习3-递减及试井/二元回归.xlsx'  # 替换为你的 Excel 文件路径
sheet_name = 'Sheet1'    # 替换为你的表名
data = pd.read_excel(file_path, sheet_name=sheet_name)

# 打印数据前几行，检查是否正确读取
print("数据预览：")
print(data.head())

# 假设 Excel 中列名为 'X1', 'X2', 和 'Y'，根据实际表头替换
X1 = data['Q']
X2 = data['Qt']
Y = data['Gp']

# 将两个自变量合并为一个二维数组
X = np.column_stack((X1, X2))

# 创建线性回归模型
model = LinearRegression()

# 拟合模型
model.fit(X, Y)

# 输出回归系数和截距
print("回归系数 (Coefficients):", model.coef_)
print("截距 (Intercept):", model.intercept_)

# 预测
Y_pred = model.predict(X)

# 评估模型
mse = mean_squared_error(Y, Y_pred)
r2 = r2_score(Y, Y_pred)

print("均方误差 (Mean Squared Error):", mse)
print("决定系数 (R^2):", r2)

# 可视化（二维散点图，以 X1 为横轴）
plt.scatter(X1, Y, color='blue', label='实际值')
plt.scatter(X1, Y_pred, color='red', label='预测值')
plt.plot(X1, Y_pred, color='green', label='拟合线')
plt.xlabel('X1')
plt.ylabel('Y')
plt.legend()
plt.title('多元线性回归 (X1 vs Y)')
plt.show()
