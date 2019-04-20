d = 5
t = 0


def abc():
    for a in range(0,10):
        for b in range(0, 10):
            for e in range(0, 10):
                for g in range(0, 10):
                    for l in range(0, 10):
                        for n in range(0, 10):
                            for o in range(0, 10):
                                for r in range(0, 10):

                                    x = int('{0}{1}{2}{3}{4}{5}'.format(d, o, n, a, l, d))
                                    y = int('{0}{1}{2}{3}{4}{5}'.format(g, e, r, a, l, d))
                                    z = int('{0}{1}{2}{3}{4}{5}'.format(r, o, b, e, r, t))
                                    if x + y == z:
                                        print(z)

if __name__ == '__main__':
    abc()
