print("""
    <===<<< TOYOTA KC EXPRESS >>>===>
     RENTAL MOBIL :
    ______________________________________________________________ 
    | KODE |  Nama Mobil  |          Harga Sewa                  |
    |______|______________|  1 Jam Pertama   | 1 Jam Berikutnya  |
    |------| ------------ |------------------|-------------------|
    |  AL  | -> Alphard   | Rp. 550.000,00   | Rp. 300.000,00    |       
    |  FO  | -> Fortuner  | Rp. 430.000,00   | Rp. 250.000,00    |
    |  IN  | -> Innova    | Rp. 400.000,00   | Rp. 220.000,00    |
    |  AV  | -> Avanza    | Rp. 350.000,00   | Rp. 200.000,00    |
    |  CA  | -> Calya     | Rp. 320.000,00   | Rp. 200.000,00    |
    |______|______________|__________________|___________________|
        
    """)

nama  = input("Masukkan Nama : ")
alamat = input("Masukkan Alamat : ")
umur = input("Masukkan Usia Anda : ")
kontak = input("Nomor Handphone  : ")

kode = input("Masukkan Kode Mobil : ")
jam  = int(input("Mau Sewa Berapa Jam? : "))

if kode == "AL":
    mobil = "Alphard"
    harga1 = 550_000
    harga2 = 300_000
    
    if jam == 1:
        hargaSewa = harga1
    
    elif jam >=2:
        hargaSewa = (jam - 1) * harga2 + harga1
    
elif kode == "FO":
    mobil = "Fortuner"
    harga1 = 430_000
    harga2 = 250_000
    
    if jam == 1:
        hargaSewa = harga1
    
    elif jam >=2:
        hargaSewa = (jam - 1) * harga2 + harga1
        
elif kode == "IN":
    mobil = "Innova"
    harga1 = 400_000
    harga2 = 220_000
    
    if jam == 1:
        hargaSewa = harga1
    
    elif jam >=2:
        hargaSewa = (jam - 1) * harga2 + harga1
    
elif kode == "AV":
    mobil = "Avanza"
    harga1 = 350_000
    harga2 = 200_000
    
    if jam == 1:
        hargaSewa = harga1
    
    elif jam >=2:
        hargaSewa = (jam - 1) * harga2 + harga1
    
elif kode == "CA":
    mobil = "Calya"
    harga1 = 320_000
    harga2 = 200_000
    
    if jam == 1:
        hargaSewa = harga1
    
    elif jam >=2:
        hargaSewa = (jam - 1) * harga2 + harga1
    
else:
    print("Masukkan Kode Dengan Benar ")
    
print(f"""
      <===<<< TOYOTA KC EXPRESS >>>===>
      Nama               : {nama}
      Alamat             : {alamat}
      Umur               : {umur} Tahun
      No Handphone       : {kontak}
      Nama Mobil         : {mobil}
      Banyak Jam Sewa    : {jam} Jam
      Harga Sewa Sebesar : Rp.{hargaSewa},00
            
      """)
