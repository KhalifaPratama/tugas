def nilai(n):
    if 100>=n>=90:
        print('Nilai A')
    elif 89>=n>=80:
        print('Nilai B')
    elif 79>=n>=75:
        print('Nilai C')
    elif 74>=n>=50:
        print('Nilai D')
    elif 49>=n>=0:
        print('Nilai E(jeblok)')
    else:
        print('Angka salah')

n=int(input('Masukkan Angka Nilai='))

nilai(n)
