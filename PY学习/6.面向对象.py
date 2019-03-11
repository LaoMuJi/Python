# 私有属性
class X(object):

    # 首先执行
    def __init__(self, num):
        # 私有变量
        self.num = num
        self.__b = "我是b变量"
        # print(self.__b)

    # 私有属性
    def __siyou(self):
        self.a = 1
        print(self.a, self.num)

    def abc(self):
        print('干活中')


class Y(X):

    def de(self):
        # 调用子
        self.abc()
        # super()代表得到父类
        super().abc
        print('干活中2')


# 私有
x = X('99')
print(x._X__b)  # 我是b变量
x._X__siyou()  # 1, 99


# 调用子
y = Y('99')
y.de()  # 干活中 干活中 干活中2




class Z():

    def zzz(self):
        print("1")

    # 类方法
    @classmethod
    def abc(cls):
        print("2")

    # 静态方法
    @staticmethod
    def bcd():
        print("3")


z = Z()
z.zzz()
z.abc()
z.bcd()