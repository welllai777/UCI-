import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import seaborn as sns
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # 导入 3D 绘图工具

# 1. 加载数据
file_path = r'C:\Users\HP2\Desktop\cleaned_data.csv'
data = pd.read_csv(file_path)

# 2. 数据预处理
X = data.drop('num', axis=1)  # 假设 'num' 是目标变量
y = data['num']

# 标准化数据
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 3. 应用PCA
pca = PCA(n_components=4)  # 使用 4 个主成分
X_pca = pca.fit_transform(X_scaled)

# 4. 解释结果
print("Explained variance ratio:", pca.explained_variance_ratio_)
print("Cumulative explained variance ratio:", pca.explained_variance_ratio_.cumsum())

# 将降维后的数据转换为DataFrame
columns = [f'PC{i+1}' for i in range(4)]  # 动态生成 4 个列名
pca_df = pd.DataFrame(data=X_pca, columns=columns)
pca_df['num'] = y

# 打印降维后的数据
print(pca_df.head())

# 保存降维后的数据
output_path = r'C:\Users\HP2\Desktop\pca_reduced_data.csv'
pca_df.to_csv(output_path, index=False)
print(f"降维后的数据已保存到: {output_path}")

# 5. 绘制成对主成分的散点图矩阵
plt.figure(figsize=(10, 10))
sns.pairplot(pca_df, vars=columns, hue='num', palette='viridis', plot_kws={'alpha': 0.7})
plt.suptitle('Pair Plot of Principal Components', y=1.02)
plt.show()

# 6. 绘制累计方差贡献率图
explained_variance_ratio = pca.explained_variance_ratio_
cumulative_explained_variance = explained_variance_ratio.cumsum()

plt.figure(figsize=(10, 6))
plt.bar(range(1, 5), explained_variance_ratio, alpha=0.6, label='Individual Explained Variance')
plt.plot(range(1, 5), cumulative_explained_variance, marker='o', linestyle='--', color='red', label='Cumulative Explained Variance')

plt.xlabel('Principal Components')
plt.ylabel('Explained Variance Ratio')
plt.title('Explained Variance Ratio by Principal Components')
plt.xticks(range(1, 5))
plt.legend()
plt.grid(True)
plt.show()

# 7. 3D 散点图（选择 PC1、PC2、PC3）
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# 绘制 3D 散点图
scatter = ax.scatter(pca_df['PC1'], pca_df['PC2'], pca_df['PC3'], c=pca_df['num'], cmap='viridis', alpha=0.7)

# 添加颜色条
cbar = plt.colorbar(scatter)
cbar.set_label('num')

# 设置坐标轴标签
ax.set_xlabel('PC1')
ax.set_ylabel('PC2')
ax.set_zlabel('PC3')

# 设置标题
plt.title('3D PCA of Cleaned Data (First 3 Components)')

# 显示图形
plt.show()

# 8. 绘制主成分之间的相关性热力图
correlation_matrix = pca_df[columns].corr()

plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Correlation Heatmap of Principal Components')
plt.show()