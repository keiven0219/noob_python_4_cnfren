# https://www.runoob.com/python3/python3-reg-expressions.html
# https://www.runoob.com/python3/python3-reg-expressions.html#flags   正则表达式修饰符 - 可选标志
# https://tool.oschina.net/ 包括正则表达式测试在内的一揽子工具

import re
print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.match('com', 'www.runoob.com'))         # 不在起始位置匹配