import torch
'''在某些情况下，即使形状不同，我们仍然可以通过调用 广播机制（broadcasting mechanism）来执行按元素操作。 这种机制的工作方式如下：

通过适当复制元素来扩展一个或两个数组，以便在转换之后，两个张量具有相同的形状；

对生成的数组执行按元素操作'''

a = torch.arange(3).reshape((3, 1))
b = torch.arange(2).reshape((1, 2))
print(a)
print(b)

'''如果让它们相加，它们的形状不匹配。 我们将两个矩阵广播为一个更大的
矩阵，如下所示：矩阵a将复制列， 矩阵b将复制行，然后再按元素相加。'''
print(a+b)
