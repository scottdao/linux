import  matplotlib.pyplot as plt

# ### 绘制简单曲线

# plt.plot([1,3,5],[4,8,10])
# 安装 matplotlib seaborn

# plt.show()
# ## 绘制numpy曲线

# import numpy as np
# 利用numpy的方法绘制图形
# x = np.linspace(-np.pi*2, np.pi*2, 100) # 域:-2pi 到 2pi
# plt.figure(1,dpi=500) # 创建图表,dpi表示精度,图像精度；
# for i in range(1, 5):
#    plt.plot(x, np.sin(x / i))
# plt.show()


### 直方图

# plt.figure(1, dpi=100)
# data = [1,2,3,41,21,1,1,1,2,2,2,3,6,4]
# plt.hist(data)# 统计数据出现的次数
# plt.show();

###  散点图
import numpy as np

# x = np.arange(1,10)
# y = x
# fig = plt.figure()
# plt.scatter(x,y,c = 'r', marker = 'o') # c = 'r' 表示点的颜色为红色，maker ='o' 表示点为圆形
# plt.show()

# seaborn 进行数据可视化
import pandas as pd
import seaborn as sns

csv  = pd.read_csv('./tq.csv')
# 设置样式
sns.set(style='white', color_codes=True)

# 设置绘制格式散点图

sns.jointplot(x='12', y='4', data=csv, size=5)

# displot 绘制曲线
sns.distplot(csv('120'))

plt.show()

