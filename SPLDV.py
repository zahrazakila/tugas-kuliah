def prog():
    print("===PROGRAM SPLDV MANUAL===")
    print('')
    print("persamaan 1 : ax + by = c")
    print("masukkan nilai a,b dan c")
    print('')
    a = float(input("masukkan nilai a: "))
    b = float(input("masukkan nilai b: "))
    c = float(input("masukkan nilai c: "))
    print('')
    print("persamaan 2 : px + qy + r")
    print("masukkan nilai p,q dan r")
    print('')
    p = float(input("masukkan nilai p: "))
    q = float(input("masukkan nilai q: "))
    r = float(input("masukkan nilai r: "))
    print('')

    # output
    x = (c*q - r*b)/(a*q - p*b)
    y = (1/b)*(c - a*x)

    print("==Solusi SPLDV==")
    print('')
    print('x :', x)
    print('y :', y)


while True:
    print("===Program SPLDV MANUAL===")
    print('')
    print('1. Ke Program')
    print('2. Keluar')
    pilihan = int(input("Masukkan pilihan anda : "))
    if pilihan == 1:
        prog()
    elif pilihan == 2:
        exit()
