import pandas as pd

# 文件路径
file_path = r"C:\Users\HP2\Desktop\formatted_data.csv"

# 读取 CSV 文件
try:
    df = pd.read_csv(file_path)
    
    # 检查列名，确保第一行是列名
    if not pd.api.types.is_string_dtype(df.columns):
        raise ValueError("第一行不是列名，请检查文件格式。")

    # 删除包含缺失值的行
    df = df.dropna()

    # 删除包含特殊字符 '?' 的行
    for column in df.columns:
        df = df[~df[column].astype(str).str.contains('\?')]

    # 确保所有数据为数值类型
    df = df.apply(pd.to_numeric, errors='coerce')

    # 再次删除转换后可能产生的缺失值
    df = df.dropna()

    # 输出清洗后的数据形状
    print(f"清洗后的数据形状: {df.shape}")

    # 保存清洗后的数据到新的 CSV 文件
    cleaned_file_path = r"C:\Users\HP2\Desktop\cleaned_data.csv"
    df.to_csv(cleaned_file_path, index=False)
    print(f"清洗后的数据已保存到: {cleaned_file_path}")

except FileNotFoundError:
    print(f"文件未找到，请检查路径是否正确: {file_path}")
except Exception as e:
    print(f"发生错误: {e}")