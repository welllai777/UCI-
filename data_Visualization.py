import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 读取数据
file_path = "C:\\Users\\HP2\\Desktop\\cleaned_transformed_data.csv"
df = pd.read_csv(file_path)

# 设置全局绘图风格
sns.set(style="whitegrid")

# **设置 Matplotlib 显示中文**
plt.rcParams['font.sans-serif'] = ['SimHei']  # 黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 1. 绘制特征相关性热图
plt.figure(figsize=(12, 8))
corr_matrix = df.corr(numeric_only=True)  # 计算数值型特征的相关性
sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap="coolwarm", linewidths=0.5)
plt.title("特征相关性热图")
plt.show()

# 2. 目标变量（心脏病诊断）与不同特征的分布差异
target_col = "心脏病诊断"  # 你的目标变量列名

# 选择一些关键数值特征进行对比
num_features = ["年龄", "静息血压", "血清总胆固醇", "最大心率", "ST段下降"]
fig, axes = plt.subplots(2, 3, figsize=(15, 10))

for i, feature in enumerate(num_features):
    row, col = divmod(i, 3)
    sns.boxplot(x=df[target_col], y=df[feature], ax=axes[row, col])
    axes[row, col].set_title(f"{feature} vs {target_col}")

plt.tight_layout()
plt.show()

# 3. 使用散点图矩阵探索数据的多维关系
selected_features = ["年龄", "最大心率", "血清总胆固醇", "ST段下降", "心脏病诊断"]
sns.pairplot(df[selected_features], hue=target_col, palette="husl")
plt.show()
