#!/usr/bin/env
#coding=utf-8

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError,ValueError):
        pass

    return False


# 测试字符串和数字
print(is_number('foo'))
print(is_number('1'))  #
print(is_number('1.3'))  
print(is_number('-1.37'))
print(is_number('1e3'))

# 测试 Unicode
# 阿拉伯语 5
print(is_number('٥'))
# 泰语 2
print(is_number('๒'))
# 中文数字
print(is_number('四'))
# 版权号
print(is_number('©'))
