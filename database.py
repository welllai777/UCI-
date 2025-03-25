import pandas as pd
import mysql.connector
from mysql.connector import Error

# 1. 读取Excel文件
file_path = r"C:\Users\HP2\Desktop\latestdata.xlsx"
df = pd.read_excel(file_path, sheet_name="Sheet1")

# 2. 连接到MySQL数据库
def connect_to_db():
    try:
        conn = mysql.connector.connect(
            host="localhost",          # MySQL服务器地址
            user="root",      # MySQL用户名
            password="123456",  # MySQL密码
            database="shujuwajueUCI"     # 数据库名称
        )
        return conn
    except Error as e:
        print(f"连接数据库时出错: {e}")
        return None

# 3. 创建表
def create_table(conn):
    try:
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS heart_disease_data (
                age_range VARCHAR(50),
                gender VARCHAR(10),
                chest_pain_type VARCHAR(50),
                resting_blood_pressure VARCHAR(50),
                serum_cholesterol VARCHAR(50),
                fasting_blood_sugar VARCHAR(50),
                resting_ecg VARCHAR(50),
                max_heart_rate VARCHAR(50),
                exercise_induced_angina VARCHAR(10),
                st_depression VARCHAR(50),
                peak_st_segment VARCHAR(50),
                major_vessels VARCHAR(50),
                resting_wall_motion_abnormality VARCHAR(50),
                heart_disease_diagnosis VARCHAR(50)
            )
        """)
        conn.commit()
        cur.close()
    except Error as e:
        print(f"创建表时出错: {e}")

# 4. 插入数据
def insert_data(conn, df):
    try:
        cur = conn.cursor()
        # 将DataFrame转换为元组列表
        data_tuples = [tuple(row) for row in df.to_numpy()]
        # 插入数据
        insert_query = """
            INSERT INTO heart_disease_data (
                age_range, gender, chest_pain_type, resting_blood_pressure, serum_cholesterol, 
                fasting_blood_sugar, resting_ecg, max_heart_rate, exercise_induced_angina, 
                st_depression, peak_st_segment, major_vessels, resting_wall_motion_abnormality, 
                heart_disease_diagnosis
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cur.executemany(insert_query, data_tuples)
        conn.commit()
        cur.close()
    except Error as e:
        print(f"插入数据时出错: {e}")

# 5. 查询数据
def query_data(conn, age_range):
    try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM heart_disease_data WHERE age_range = %s", (age_range,))
        rows = cur.fetchall()
        for row in rows:
            print(row)
        cur.close()
    except Error as e:
        print(f"查询数据时出错: {e}")

# 6. 更新数据
def update_data(conn, age_range, new_diagnosis):
    try:
        cur = conn.cursor()
        cur.execute("""
            UPDATE heart_disease_data
            SET heart_disease_diagnosis = %s
            WHERE age_range = %s
        """, (new_diagnosis, age_range))
        conn.commit()
        cur.close()
    except Error as e:
        print(f"更新数据时出错: {e}")

# 7. 主函数
def main():
    # 连接到数据库
    conn = connect_to_db()
    if conn is None:
        return
    
    # 创建表
    create_table(conn)
    
    # 插入数据
    insert_data(conn, df)
    
    # 查询数据
    print("查询年龄范围为51-60的数据：")
    query_data(conn, "51-60")
    
    # 更新数据
    update_data(conn, "51-60", "1")
    print("更新后的数据：")
    query_data(conn, "51-60")
    
    # 关闭连接
    conn.close()

if __name__ == "__main__":
    main()