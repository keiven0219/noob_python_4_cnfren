# ctrl+/         快捷注释/快捷取消注释
# ctrl+p         查看参数
# table          table
# shift+table    撤销table

# import sys
# print(sys.getdefaultencoding())
# for i in range(0,10):
#     print(i,end='-')

# num_list = [1, 2, 3, 4, 5, 6]
# it = iter(num_list) #迭代器 next（）
# for num in it:
#     print(num,end='000')

import sys
num_list = [1, 2, 3, 4, 5, 6]
it = iter(num_list) #迭代器 next（）
while True:
    try:
        print(next(it))
    except StopIteration:
        sys.exit()