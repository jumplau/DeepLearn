import pandas as pd

# 创建一个字典，包含一些人工数据
data = {
    'House_ID': [1, 2, 3, 4, 5],
    'Size_sqft': [1500, 2000, 2500, 3000, 3500],
    'Bedrooms': [3, 4, 3, 5, 4],
    'Price': [300000, 400000, 500000, 600000, 700000]
}

# 将字典转换为DataFrame
df = pd.DataFrame(data)

# 指定CSV文件的保存路径
file_path = '../../data/house.csv'

# 将DataFrame写入CSV文件
df.to_csv(file_path, index=False)

print(f"数据集已保存到 {file_path}")
