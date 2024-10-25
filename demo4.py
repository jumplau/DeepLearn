import os
#预处理数据，读取数据集


os.makedirs(os.path.join('..', 'data'), exist_ok=True)
data_file=os.path.join('..', 'data', 'house_tiny.csv')
with open('data_file', 'w') as f:
    f.write('NumRooms,Alley,Price\n')  # 列名
    f.write('NA,AMI,133300\n')  # 每行表示一个数据样本
    f.write('2,NA,106000\n')
    f.write('4,NA,178100\n')
    f.write('NA,FVAA,155000\n')


