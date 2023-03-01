# https://www.runoob.com/python3/python3-inputoutput.html
# Python两种输出值的方式: 表达式语句和 print() 函数。
# 第三种方式是使用文件对象的 write() 方法，标准输出文件可以用 sys.stdout 引用。

# s = 'Hello, Runoob'
# print(str(s))
# print(repr(s))  #包含'  '

# 有两种方式输出一个平方与立方的表
# str.format()
# str = input("请输入：");
# print ("你输入的内容是: ", str)

# 读和写文件
# open(filename, mode)

f = open("python.txt", "w")
f.write( "Python 是一个非常好的语言。\n是的，的确非常好!!\n" )
# 关闭打开的文件
f.close()
# 第二个参数描述文件如何使用的字符。
# mode 可以是 'r' 如果文件只读,
# 'w' 只用于写 (如果存在同名文件则将被删除)
# 'a' 用于追加文件内容; 所写的任何数据都会被自动增加到末尾.
# 'r+' 同时用于读写。 mode 参数是可选的; 'r' 将是默认值。

f = open("python.txt", "r")
# str = f.read()
# str = f.readline()  #读一行
str = f.readlines() #全读 list
print(str)
# 关闭打开的文件
f.close()


