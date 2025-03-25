import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import font_manager

# 设置 Matplotlib 的字体为支持中文的字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # Windows 系统常用字体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 设置 Seaborn 的字体
sns.set(font='SimHei')  # 设置 Seaborn 使用支持中文的字体
sns.set_style("whitegrid")  # 设置 Seaborn 的绘图风格

# 1. 读取Excel文件
file_path = r"C:\Users\HP2\Desktop\latestdata.xlsx"
df = pd.read_excel(file_path, sheet_name="Sheet1")

# 2. 数据预处理
# 将目标变量（心脏病诊断）转换为二进制（0表示无心脏病，1表示有心脏病）
df['心脏病诊断'] = df['心脏病诊断'].apply(lambda x: 1 if x > 0 else 0)

# 将年龄列转换为数值
def convert_age(age):
    try:
        if isinstance(age, str):
            if '+' in age:  # 处理 71+ 的情况
                return int(age.replace('+', ''))
            elif '-' in age:  # 处理 61-70 的情况
                start, end = age.split('-')
                return (int(start) + int(end)) / 2
            else:  # 处理纯数字的情况
                return int(age)
        else:  # 如果已经是数值类型，直接返回
            return float(age)
    except (ValueError, AttributeError):
        return float('nan')  # 处理异常情况，返回 NaN

df['年龄'] = df['年龄'].apply(convert_age)

# 将静息血压列转换为数值
def convert_blood_pressure(bp):
    try:
        if isinstance(bp, str):
            if '+' in bp:  # 处理 171+ 的情况
                return int(bp.replace('+', ''))
            elif '-' in bp:  # 处理 131-150 的情况
                start, end = bp.split('-')
                return (int(start) + int(end)) / 2
            else:  # 处理纯数字的情况
                return int(bp)
        else:  # 如果已经是数值类型，直接返回
            return float(bp)
    except (ValueError, AttributeError):
        return float('nan')  # 处理异常情况，返回 NaN

df['静息血压'] = df['静息血压'].apply(convert_blood_pressure)

# 将血清总胆固醇列转换为数值（取范围的中点）
def convert_cholesterol(chol):
    try:
        if isinstance(chol, str):
            if '-' in chol:  # 处理范围值（如 200-300）
                start, end = chol.split('-')
                return (int(start) + int(end)) / 2
            else:  # 处理纯数字的情况
                return int(chol)
        else:  # 如果已经是数值类型，直接返回
            return float(chol)
    except (ValueError, AttributeError):
        return float('nan')  # 处理异常情况，返回 NaN

df['血清总胆固醇'] = df['血清总胆固醇'].apply(convert_cholesterol)

# 将最大心率列转换为数值（取范围的中点）
def convert_max_hr(hr):
    try:
        if isinstance(hr, str):
            if '-' in hr:  # 处理范围值（如 100-150）
                start, end = hr.split('-')
                return (int(start) + int(end)) / 2
            else:  # 处理纯数字的情况
                return int(hr)
        else:  # 如果已经是数值类型，直接返回
            return float(hr)
    except (ValueError, AttributeError):
        return float('nan')  # 处理异常情况，返回 NaN

df['最大心率'] = df['最大心率'].apply(convert_max_hr)

# 处理分类变量（如性别）
# 假设性别列名为 '性别'，将其转换为数值编码
if '性别' in df.columns:
    df['性别'] = df['性别'].map({'男': 1, '女': 0})  # 将 '男' 转换为 1，'女' 转换为 0

# 3. 绘制各特征之间的相关性热图
# 只选择数值列进行相关性计算
numerical_columns = df.select_dtypes(include=['number']).columns
plt.figure(figsize=(12, 8))
corr_matrix = df[numerical_columns].corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('各特征之间的相关性热图')
plt.show()

# 4. 针对目标变量，展示不同特征的分布差异
# 选择一些关键特征进行可视化
features = ['年龄', '静息血压', '血清总胆固醇', '最大心率']

# 逐个特征绘制分布图
for feature in features:
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df, x=feature, hue='心脏病诊断', kde=True, palette='Set1', multiple='stack')
    plt.title(f'{feature} 的分布（按心脏病诊断分组）', fontproperties='SimHei')  # 显式设置字体
    plt.xlabel(feature, fontproperties='SimHei')  # 显式设置字体
    plt.ylabel('频数', fontproperties='SimHei')  # 显式设置字体
    plt.show()