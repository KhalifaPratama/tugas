def tambah(angka1,angka2):
    hasil=angka1+angka2
    print(f'{angka1}+{angka2}={hasil}')

def kurang(angka1,angka2):
    hasil=angka1+angka2
    print(f'{angka1}-{angka2}={hasil}')

angka1=int(input('silahkan masukkan Saldo: '))
pin=int(input('silahkan masukkan pin: '))
while True:
    
    if pin==999:
     pilihan=int(input('''
Menu ATM
1. Tarik
2. Setor
3. Cek Saldo
4. Keluar
pilihan anda: '''))
    
     if pilihan==1:
        tarik = int(input('Masukkan saldo yang ingin ditarik: '))

        if tarik % 50000 == 0:
            if tarik > angka1:
                print('Tarik lebih besar dari saldo')
            else:
                angka1 = angka1 - tarik
        else:
            print('Tarik bukan kelipatan 50rb')
        
     elif pilihan==2:
        angka2=int(input('silahkan masukkan saldo yang ingin ditambahakan: '))
        angka1 = angka1 + angka2
        
     elif pilihan==3:
        print('Saldo anda :','Rp.',angka1)
     elif pilihan==4:
        break
     else:
        print('Pilihan salah, Silahkan coba lagi!')
    else:
        print('Pin salah, Coba lagi')
        
    
               
    
