bilangan = int(input('masukan bilangan: '))
count = 0
x1 = 0
x2 = 1
 
fibonacci = []
while count < bilangan:
   fibonacci.append(x1)
   bilangan_terakhir = x1 + x2
   x1 = x2
   x2 = bilangan_terakhir
   count += 1
   
print(fibonacci)
 
daftar_string = [str(angka) for angka in fibonacci]
deret_string = ', '.join(daftar_string)
print('Deret fibonacci dengan banyak bilangan {} adalah:\n{}'. format(bilangan, ', '.join(daftar_string)))
