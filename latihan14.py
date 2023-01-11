print("SITI NURVIATIKA_20220040281")
print("program sederhana sistem kasir(sesi14)")

totalHarga = 0

while(True):
    print("===== menu produk =====")
    print("1. buku      : RP 50.000 ")
    print("2. pena      : RP 20.000 ")
    print("3. kerayon   : RP 35.000 ")
    print("4. penggaris : RP 15.000 ")
    print("5. rak buku  : RP 55.000 ")
    print("6. headphone : RP 500.000 ")

    listMenu = input(" Masukan pilihan anda :")
    jumlahPesanan = int(input("masukan jumlah pesanan anda :"))

    if listMenu == "1" :
        print("\nMenu produk -> buku ")
        namaMenu = ("buku")
        hargaJual = (50.000 * jumlahPesanan)

    elif listMenu == "2" :
        print("\nMenu produk -> pena ")
        namaMenu = ("pena")
        hargaJual = (20.000 * jumlahPesanan)
    
    elif listMenu == "3" :
        print("\nMeu produk -> kerayon ")
        namaMenu = ("kerayon")
        hargaJual = (35.000 * jumlahPesanan)
    
    elif listMenu == "4" :
        print("\nMenu produk -> penggaris ")
        namaMenu = ("penggaris")
        hargaJual = (15.000 * jumlahPesanan)

    elif listMenu == "5" :
        print("\nMenu produk -> rak buku ")
        namaMenu = ("rak buku")
        hargaJual = (55.000 * jumlahPesanan)

    elif listMenu == "6" :
        print("\nMenu produk -> headphone ")
        namaMenu = ("headphone")
        hargaJual = (500.000 * jumlahPesanan)

    else :
        print("\n Maaf inputan salah silahkan coba kembali ")

    totalHarga = totalHarga + hargaJual

    print("\nMenu yang anda pilih : ", namaMenu)
    print("\njumlah pesanan : ", jumlahPesanan)
    print("\ntotal harga : ", hargaJual)
    
    apakahLanjut = input("\nIngin membeli barang lain? Y or N : ")
    if (apakahLanjut != "y") :
        print("\nLihat note pembayaran anda :")
        print(" thanks")
        break

headerNota = ("\n-- STRUK PEMBELIAN -- ")

totalHarga_str = format(totalHarga)

footerNota = ("\nThanks")


# nota dalam bentuk txt
fileNota_txt = open ("Nota_pembayaran.txt ", "w")

fileNota_txt.write(headerNota)
fileNota_txt.write("\nTotal pembayaran, Rp")
fileNota_txt.write(totalHarga_str)
fileNota_txt.write(footerNota)

fileNota_txt.close()

# nota dalam bentuk Pdf
#fileNota_pdf = open ("Nota_pembayaran.pdf ", "wb")

#fileNota_pdf.write(headerNota)
#fileNota_pdf.write("\nTotal pembataran, Rp")
#fileNota_pdf.write(totalHarga-str)
#fileNota_pdf.write(footerNota)

