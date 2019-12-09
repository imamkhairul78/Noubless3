def jumlah(a, b):
   return a + b

def kurang(a, b):
   return a - b

def kali(a, b):
   return a * b

def bagi(a, b):
   return a / b

print("Pilih Operasi.")
print("1.Jumlah")
print("2.Kurang")
print("3.Kali")
print("4.Bagi")


masukkan = input("Masukkan pilihan: ")
angka1   = int(input("Masukkan bilangan pertama: "))
angka2   = int(input("Masukkan bilangan kedua  : "))

if masukkan == '1':
   print(angka1,"+",angka2,"=", jumlah(angka1,angka2))
elif masukkan == '2':
   print(angka1,"-",angka2,"=", kurang(angka1,angka2))
elif masukkan == '3':
   print(angka1,"*",angka2,"=", kali(angka1,angka2))
elif masukkan == '4':
   print(angka1,"/",angka2,"=", bagi(angka1,angka2))
else:
   print("Input salah")
