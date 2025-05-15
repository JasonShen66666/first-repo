# 导入必要的库
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline


# 设置文件路径和工作表名称
file_path = 'C:/Users/Jason Shen/Desktop/油藏工程/实习3-递减及试井/压力回复.xlsx'  # 替换为你的 Excel 文件路径
sheet_name = 'Sheet2'    # 替换为你的表名

# 读取 Excel 数据
data = pd.read_excel(file_path, sheet_name=sheet_name)

pd.set_option('display.max_rows', 10)  # 最多显示 10 行
# 检查数据
print(data)

# 提取自变量（X）和因变量（Y）
X = data[['X']]  # 替换为你的 Excel 表中自变量的列名
Y = data['Y']     # 替换为你的 Excel 表中因变量的列名

X_slice = X.iloc[5:]  # 切片索引5到最后
Y_slice = Y.iloc[5:]
# 生成插值模型

X_smooth = np.linspace(X.values.min(), X.values.max(), 300)  # 在 X 范围内生成更多点
spline = make_interp_spline(X.values.flatten() , Y.values)  # 将 X 转换为一维数组,创建插值模型
Y_smooth = spline(X_smooth)                   # 计算平滑曲线对应的 Y 值

# 创建线性回归模型
model = LinearRegression()

# 拟合模型
model.fit(X_slice,Y_slice)

# 获取回归系数和截距
coefficient = model.coef_[0]
intercept = model.intercept_

# 输出回归方程
print(f"回归方程:Y = {coefficient:.4f}*X + {intercept:.4f}")

# 预测因变量
Y_pred = model.predict(X_slice)

# 在 X 和 Y_pred 列的前面添加元素(延长拟合曲线！！！！)
new_X=[-2]
new_Y=[-2*coefficient+intercept]
# 确保新列长度与原 data 长度一致
X_slice1 = np.insert(X_slice.values, 0, new_X)  # 在 X_slice 的最前面插入 new_X(转为np数组)
Y_pred1 = np.insert(Y_pred, 0, new_Y)    # 在 Y_pred 的最前面插入 new_Y


# 评估模型
mse = mean_squared_error(Y_slice.values, Y_pred)
r2 = r2_score(Y_slice, Y_pred)
print(f"均方误差 (MSE): {mse:.8f}")

print(f"决定系数 (R²): {r2:.4f}")




# 可视化
plt.scatter(X, Y, color='blue', label='实际值')
plt.plot(X_smooth, Y_smooth, color='green', label='实际线')
plt.plot(X_slice1, Y_pred1, linestyle='--',color='red', label='预测值')
plt.xlabel('lg(∆t)')
plt.ylabel('Pws')
plt.title('MDH curve')
#plt.title('Honor curve')
#plt.legend()
plt.show()
