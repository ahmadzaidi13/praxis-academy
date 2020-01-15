#Method Resolution Order (MRO)
#diamond problem

class A:
    num = 4

class B(A):
    pass

class C(A):
    num = 6

class D(B, C):
    pass

X = D()
#dengan kode ini maka X akan mengambil nilai dari kelas
#terdekat sesuai dengan urutan eksekusi kelas
print (D.num)
#urutan kelas yang dieksekusi dapat di lihat dengan
help (X)
    