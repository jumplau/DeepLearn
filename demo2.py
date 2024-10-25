import torch

'''最简单且最有用的操作是按元素（elementwise）运算'''
x=torch.tensor([1,2,4,8])
y=torch.tensor([2,2,2,2])

print(x)
print(y)

print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x**y)  #幂指运算

print(torch.exp(x))
'''除了按元素计算外，我们还可以执行线性代数运算，
包括向量点积和矩阵乘法。 我们将在 2.3节中解释线性代数的重点内容'''
print('-------------------------------------')
X = torch.arange(12, dtype=torch.float32).reshape((3,4))
Y = torch.tensor([[2.0, 1, 4, 3], [1, 2, 3, 4], [4, 3, 2, 1]])
print(torch.cat((X, Y), dim=0))
print(torch.cat((X, Y), dim=1))
print(X==Y)