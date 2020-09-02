hargaApel = 2000
uang = 10000
jumlah = input('Mau berapa apel ?: ')
jumlah_apel = int(jumlah)
total_harga = hargaApel * jumlah_apel

print('Anda akan membeli ' + str(jumlah_apel) + ' apel')
print('Harga total adalah ' + str(total_harga) + ' rupiah')

if uang > total_harga:
    print('uang anda tinggal ' + str(uang - total_harga) + ' Rupiah')
elif uang == total_harga:
    print('Dompet kosong')
else:
    print('Uang anda tidak mencukupi')
    print('Anda tidak dapat membeli apel sebanyak itu')