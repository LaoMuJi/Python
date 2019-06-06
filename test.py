def a(b):
    def c(d):
        print('Z')
        b(d)
    return c

@a
def e(f):
    print(f)

e(100)