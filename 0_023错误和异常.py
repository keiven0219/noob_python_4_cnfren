# https://www.runoob.com/python3/python3-errors-execptions.html
# 异常处理
# try/except
# 一个 try 语句可能包含多个except子句，分别来处理不同的特定的异常。最多只有一个分支会被执行。
# 处理程序将只针对对应的 try 子句中的异常进行处理，而不是其他的 try 的处理程序中的异常。
# 一个except子句可以同时处理多个异常，这些异常将被放在一个括号里成为一个元组，例如:
# except (RuntimeError, TypeError, NameError):
#     pass

import sys
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except IOError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()
    finally:
        print('这句话，无论异常是否发生都会执行。')