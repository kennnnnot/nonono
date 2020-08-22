
# 输出初学
# print ("hello世界")#输出hello
# print (3%2)
# print(4/3)
# print("""goodmoring!
# oh,it's ok right?
# that's great!""")
# 2 == 3

# 函数初学
# def add(x,y):
#     return x + y

# def subtract(x,y):
#     return x - y

# def double_do(func,x,y):
#     return func(func(x,y),func(x,y))

# print(double_do(subtract,3,2))

# -*- coding: UTF-8 -*-

# 全局变量测试
a = 100

# def fun():
#     global a
#     a = a + 2
#     print("函数内输入：" + str(a))

# fun()
# print("函数外输出：" + str(a))
try:
    file = open('./pythontxt.txt','r',encoding='UDF-8')
    # txt = "hello world,我是中国人"
    # file.write = (txt)
    content = file.read()
    print(content)

finally:
    file.close()

