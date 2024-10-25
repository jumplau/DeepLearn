

'''# 读取整个文件
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

# 逐行读取文件
with open('example.txt', 'r') as file:
    for line in file:
        print(line.strip())  # 使用 strip() 去掉行尾的换行符'''
import os

if os.path.exists('example.txt'):
    print("File exists.")
else:
    print("File does not exist.")



# 写入文件
with open('example.txt', 'w') as file:
    file.write("Hello, World!\n")
    file.write("This is a new line.\n")

# 追加文件
with open('example.txt', 'a') as file:
    file.write("This line is appended.\n")


#关闭文件
file = open('example.txt', 'r')
# 处理文件
file.close()  # 关闭文件