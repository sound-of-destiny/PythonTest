
# the python test
import sys
import random
import math
from sys import path  # 导入特定的成员
print('================Python import mode==========================')
print('命令行参数为:')
for i in sys.argv:
    print(i)
# print('path:', path)  # 因为已经导入path成员，所以此处引用时不需要加sys.path

if True:
    print("true")
elif False:
    print("false")
else:
    print("default")  # 缩进不一致，会导致运行错误

count = 10  # 整形变量
count = abs(count)
long = True  # bool变量
miles = 100.0  # 浮点型变量
word = '字符串'
sentence = "这是一个句子。"
paragraph = """这是一
个段落，
    可以由多
        行组成"""
print(paragraph)

a, b, c, d = 20, 5.5, True, 4+3j
print(type(a), type(b), type(c), type(d))

print('================python string==========================')
# 字符串(string)
str = "runoob"
print(str)           # 输出字符串
print(str[0:-1])     # 输出第一个到倒数第二个的所有字符
print(str[0])        # 输出字符串第一个字符
print(str[2:5])      # 输出从第三个开始到第五个的字符
print(str[2:])       # 输出从第三个开始的后的所有字符
print(str * 2)       # 输出字符串两次
print(str + "TEST")  # 连接字符串

print('================python list==========================')
# 列表(list)
list = ['abcd', 786, 2.23, 'runoob', 70.2]
tinylist = [123, 'runoob']
it = iter(list)
print(list)             # 输出完整列表
print(list[0])          # 输出列表第一个元素
print(list[1:3])        # 从第二个开始输出到第三个元素
print(list[2:])         # 输出从第三个元素开始的所有元素
print(tinylist * 2)     # 输出两次列表
print(list + tinylist)  # 连接列表
print(next(it))

print('================python tuple==========================')
# 元组(tuple)
tuple = ('abcd', 786, 2.23, 'runoob', 70.2)
tinytuple = (123, 'runoob')
print(tuple)  # 输出完整元组
print(tuple[0])  # 输出元组的第一个元素
print(tuple[1:3])  # 输出从第二个元素开始到第三个元素
print(tuple[2:])  # 输出从第三个元素开始的所有元素
print(tinytuple * 2)  # 输出两次元组
print(tuple + tinytuple)  # 连接元组

print('================python set==========================')
# 集合(set)
student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
print(student)  # 输出集合，重复的元素被自动去掉
# 成员测试
if ('Rose' in student):
    print('Rose 在集合中')
else:
    print('Rose 不在集合中')

# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')

print(a)
print(a - b)  # a和b的差集
print(a | b)  # a和b的并集
print(a & b)  # a和b的交集
print(a ^ b)  # a和b中不同时存在的元素

print('================python dictionary==========================')
# 字典(dictionary)
dict = {}
dict['one'] = "1 - 菜鸟教程"
dict[2] = "2 - 菜鸟工具"
tinydict = {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}

print(dict['one'])          # 输出键为 'one' 的值
print(dict[2])              # 输出键为 2 的值
print(tinydict)             # 输出完整的字典
print(tinydict.keys())      # 输出所有键
print(tinydict.values())    # 输出所有值

ran = random.random()
print(ran)

n = 100
sum = 0
counter = 1
while counter <= n:
    sum = sum + counter
    counter += 1

print("1 到 %d 之和为: %d" % (n, sum))


# 计算面积函数
def area(width, height):
    return width * height


def print_welcome(name):
    print("Welcome", name)


print_welcome("Runoob")
w = 4
h = 5
print("width =", w, " height =", h, " area =", area(w, h))


# 可写函数说明
def print_info(arg1, *vartuple):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    for var in vartuple:
        print(var)
    return


# 调用printinfo 函数
print_info(10)
print_info(70, 60, 50)

# 可写函数说明 lambda
two_sum = lambda arg1, arg2: arg1 + arg2
max = lambda arg1, arg2: arg1 if(arg1>arg2) else arg2

# 调用sum函数
print("相加后的值为 : ", two_sum(10, 20))
print("相加后的值为 : ", two_sum(20, 20))


class MyClass:
    """一个简单的类实例"""
    i = 12345

    def f(self):
        return 'hello world'


# 实例化类
x = MyClass()

# 访问类的属性和方法
print("MyClass 类的属性 i 为：", x.i)
print("MyClass 类的方法 f 输出为：", x.f())


# input("\n\n按下 enter 键后退出。\n")


