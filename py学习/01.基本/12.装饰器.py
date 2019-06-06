def set_func(func):
    def call_func(a):
        func(a)
    return call_func


# 装饰器有不同的内存空间
# 先执行装饰器，然后装饰器调用func(a)来执行test，func = test()。
# 装饰器加载时候就执行了，不是调用才执行
@set_func
def test(num):
    print(num)

test(100)
# 等于 XX = set_func(test)






print('*'*20)

# 通用装饰器加return返回
def set_func1(func):
    def call_func(*args, **kwargs):
        # 拆包
        return func(*args, **kwargs)
    return call_func


@set_func1
def test1(num, *args, **kwargs):
    print(num,args,kwargs)
    return 'ok'

a = test1(100)
b = test1(100, 200, 300)
c = test1(100, 200, 300, z=100, x=200, c=300)
print(a)













# 类方法
@classmethod
def abc(cls):
    print("2")



# 静态方法，不需要传递参数
@staticmethod
def bcd():
    print("3")


