import collections


class Class1():
    def __init__(self):
        pass
    def __next__(self):
        return Class2


class Class2():
    def __iter__(self):
        pass
    def __next__(self):
        return 11


a = Class1()

print(isinstance(Class1,collections.Iterable))
print(isinstance(Class2,collections.Iterable))

# c = iter(a)
# for b in c:
#     print(b)