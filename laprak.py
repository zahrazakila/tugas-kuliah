print("Nama : Zahra Zakila Aninda Rahmanti")
print("NIM  : 23106050019")
print("Prodi: Informatika")
print("========================================")


def f(x):
    return x**2 - 5*x+6


error = 0.0001
a = 1
b = 2.4


def bisection(a, b):
    iteration = True
    i = 0
    max_iter = 50
    while iteration and i < max_iter:
        if f(a)*f(b) < 0:
            x = (a+b)/2
            if f(a)*f(x) < 0:
                b = x
                print("jika f(a)*f(x) < 0 maka b = x, b= ", x)
            if f(b)*f(x) < 0:
                a = x
                print("jika f(b)*f(x) < 0 maka a = x, b= ", x)
            if abs(a-b) < error:
                iteration = False
            else:
                i += 1
        else:
            print('tidak ditemukan akar')

    print('x=', x)


bisection(a, b)
