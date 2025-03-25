import pandas as pd

# 定义文件路径
file_path = r"C:\Users\HP2\Desktop\processed.cleveland.data"

# 定义列名
column_names = [
    'age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 
    'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal', 'num'
]

# 读取数据文件
data = pd.read_csv(file_path, header=None, names=column_names)

# 确保数据按目标顺序排列
data = data[['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 
             'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal', 'num']]

# 打印数据框
print(data)

# 保存到新的文件
data.to_csv(r"C:\Users\HP2\Desktop\formatted_data.csv", index=False, header=True)

print("数据已成功格式化并保存到 C:\\Users\\HP2\\Desktop\\formatted_data.csv")