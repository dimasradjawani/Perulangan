import random
n = input("Masukkan Jumlah N = ")

for i in range(n):

    while 1:
        a=random.random()
        if a < 0.5 :
            break

    print (a)
