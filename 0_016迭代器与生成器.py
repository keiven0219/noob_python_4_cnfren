# https://www.runoob.com/python3/python3-iterator-generator.html
# 迭代器有两个基本的方法：iter() 和 next()。
# 迭代器是一个可以记住遍历的位置的对象。
import sys

# list=[1,2,3,4]
# it = iter(list)    # 创建迭代器对象
# # print (next(it))   # 输出迭代器的下一个元素
# # print (next(it))
#
# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         sys.exit()

# 生成器
def fibonacci(n):  # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a + b
        counter += 1

f = fibonacci(10)  # f 是一个迭代器，由生成器返回生成

while True:
    try:
        print(next(f), end=" ")
    except StopIteration:
        sys.exit()