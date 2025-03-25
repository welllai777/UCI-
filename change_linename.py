import pandas as pd

# 读取原始数据
import pandas as pd

# 指定文件路径
file_path = r"C:\Users\HP2\Desktop\cleaned_data.csv"  # 使用原始字符串（r"..."）防止转义问题

# 读取 CSV 文件
df = pd.read_csv(file_path)

# 打印前几行以确认数据加载成功
print(df.head())


# 列名映射
column_mapping = {
    'age': '年龄',
    'sex': '性别',
    'cp': '胸痛类型',
    'trestbps': '静息血压',
    'chol': '血清总胆固醇',
    'fbs': '空腹血糖',
    'restecg': '静息心电图结果',
    'thalach': '最大心率',
    'exang': '运动诱发的心绞痛',
    'oldpeak': 'ST段下降',
    'slope': '运动高峰ST段',
    'ca': '主要血管',
    'thal': '静息时的室壁运动异常',
    'num': '心脏病诊断'
}
df.rename(columns=column_mapping, inplace=True)

# 定性特征映射（未定义值处理）
value_mappings = {
    '性别': {1: '男', 0: '女'},
    '胸痛类型': {1: '典型心绞痛', 2: '非典型心绞痛', 3: '非心绞痛性疼痛', 4: '无症状'},
    '空腹血糖':{1:'大于120mg/dl',0:'小于等于120mg/dl'},
    '静息心电图结果': {0: '正常', 1: 'ST-T波异常', 2: '左心室肥厚'},
    '运动诱发的心绞痛': {1: '是', 0: '否'},
    '运动高峰ST段': {1: '上升型', 2: '平坦型', 3: '下降型'},
    '静息时的室壁运动异常': {0: '没有', 3: '正常', 6: '固定缺陷', 7: '可逆缺陷'},
    '心脏病诊断': {0: '无病', 1: '轻度', 2: '中度', 3: '重度', 4: '极重度'}
}

# 进行映射转换，未定义值填充“未知”
for col, mapping in value_mappings.items():
    df[col] = df[col].map(mapping).fillna('未知')

# 选择最终列顺序
final_columns = [
    '年龄', '性别', '胸痛类型', '静息血压', '血清总胆固醇',
    '空腹血糖', '静息心电图结果', '最大心率', '运动诱发的心绞痛',
    'ST段下降', '运动高峰ST段', '主要血管',
    '静息时的室壁运动异常', '心脏病诊断'
]
df = df[final_columns]

# 保存清理后的数据
output_path = r"C:\Users\HP2\Desktop\cleaned_transformed_data.csv"
df.to_csv(output_path, index=False, encoding="utf-8-sig")  # 确保编码正确
print(f"数据清理完成，已保存至 {output_path}")
