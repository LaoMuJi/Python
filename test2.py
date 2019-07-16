import time

def abc():
    for a in qwe:
        for b in qwe:
            if b == a:
                continue
            for e in qwe:
                if e == b or e==a:
                    continue
                for g in qwe:
                    if g == e or g ==a or g==b:
                        continue
                    for l in qwe:
                        if l == g or l == e or l==b or l==a:
                            continue
                        for n in qwe:
                            if n == l or n == g or n == e or n == b or n == a:
                                continue
                            for o in qwe:
                                if o == n or o == l or o == g or o == e or o == b or o == a:
                                    continue
                                for r in qwe:
                                    if r == o or r == n or r == l or r == g or r == e or r == b or r == a:
                                        continue
                                    x = int('{0}{1}{2}{3}{4}{5}'.format(d, o, n, a, l, d))
                                    y = int('{0}{1}{2}{3}{4}{5}'.format(g, e, r, a, l, d))
                                    z = int('{0}{1}{2}{3}{4}{5}'.format(r, o, b, e, r, t))
                                    if x + y == z:
                                        print("donald:%d" % x)
                                        print("gerald:{0}".format(y))
                                        print("robert:{0}".format(z))

if __name__ == '__main__':
    time1 = time.time()
    d,t = 5,0
    qwe = [1, 2, 3, 4, 6, 7, 8, 9]
    abc()
    print('用时',time.time()-time1,'秒')

