# -*- coding: utf-8 -*-
"""prak 5 algo.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1PwJL4FB4Z16hjOmwfPB8PcQ1-cB0UfOQ
"""

skor = 0
nilaimurid = list()
ulang = 0
nomor = 0

while ulang == 0:
    nomor += 1
    x = str(input('"selesai" untuk mengakhiri!\nmasukan nilai : '))

    if x == 'selesai':
        ulang = 1

    else:

        if x == 'A':
            skor = float(4.00)

        elif x == 'A-':
            skor = float(3.75)

        elif x == 'B+':
            skor = float(3.50)

        elif x == 'B':
            skor = float(3.00)

        elif x == 'B-':
            skor = float(2.75)

        elif x == 'C+':
            skor = float(2.50)

        elif x == 'C':
            skor = float(2.00)

        elif x == 'C-':
            skor = float(1.75)

        elif x == 'D':
            skor = float(1.50)

        elif x == 'E':
            skor = float(1.25)

        else:
            print('Saya tidak mengerti...')
            skor = 0
        print(('\nNilai ke-{0} = {1}').format(nomor,skor))
        nilaimurid.append(skor)

rata2 = sum(nilaimurid) / len(nilaimurid)
print('rata rata nilai murid tersebut:', rata2)

"""
@materi : algoritma dan pemograman
@judul : menghitung kembalian
@hari/tanggal : minggu,24,10,2021
@nim : 065002100023
@author : Tri Bintang Pamungkas
"""
print("Selamat Datang")
print("umur 1 : gratis ")
print("umur 12 kebawah : $ 14.00")
print("umur 13 sampai 34 : $ 18.00")
print("umur 35 sampai 66 : $ 23.00")

ulang = 0
nomor = 0
jumlah= 0


while ulang == 0:
    nomor += 1
    x = int(input("masukan umur: "))

    if x == int("-1"):
        break

    else:

        if x == 1:
            jumlah += 0
            print("ini gratis")
            print("jumlah",jumlah)

        elif x <= 12:
            jumlah += 14.00
            print("$ 14.00")
            print("jumlah",jumlah)


        elif(x >= 13 and x <= 34) :
            jumlah += 18.00
            print("$ 18.00")
            print("jumlah: ",jumlah)

        elif(x >= 35 and x <= 66) :
            jumlah += 23.00
            print("$ 23.00")
            print("jumlah: ",jumlah)

        else :
            print("saya tidak mengerti")
            jumlah = 0



uang = int(input("Masukkan uang nya: "))

if uang == jumlah:
            print("uang anda pas")

elif uang < jumlah:
            print("uang anda kurang")

elif uang > jumlah:
            uang -= jumlah
            print("kembalian nya",uang)