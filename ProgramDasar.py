saldo = 200000
user = {"username": "test", "nomor": "0853956123"}
beli_lagi = "y"
nomor = "tidakterdaftar"


def beli_pulsa(nominal):
    global saldo
    if saldo >= nominal:
        saldo -= nominal
        print("Anda Berhasil Membeli Pulsa Rp.", nominal)
        print("Sisa Saldo Anda Adalah Rp.", saldo)
    else:
        print("Maaf Saldo Anda Tidak Cukup Untuk Membeli Pulsa Sebanyak", nominal)


while nomor == "tidakterdaftar":
    print("==================== ADJI CELL ==================== ")
    print("Mau Beli Pulsa ? Silakan Masukan Data Anda!")
    username = input("Masukan Username : ")
    nomorhp = input("Masukan NomorHp : ")
    if username == user['username'] and nomorhp == user['nomor']:
        print("Nomor Anda Terdaftar " + user['username'] + "\n")
        nomor = "terdaftar"
    else:
        print("Maaf Nomor Anda Tidak Terdaftar")

while beli_lagi == "y" and nomor == "terdaftar":
    print("Silahkan Pilih Nominal :")
    print("1. Beli Pulsa Rp. 5000")
    print("2. Beli Pulsa Rp. 10000")
    print("3. Beli Pulsa Rp. 20000")
    print("4. Beli Pulsa Rp. 25000")
    print("5. Keluar Aplikasi \n ")

    pilihan = int(input("Silahkan Pilih Nominal Pulsa Yang Akan Dibeli : "))

    if pilihan == 1:
        beli_pulsa(5000)
    elif pilihan == 2:
        beli_pulsa(10000)
    elif pilihan == 3:
        beli_pulsa(20000)
    elif pilihan == 4:
        beli_pulsa(25000)
    elif pilihan == 5:
        beli_lagi = "n"
    else:
        print("Pilihan Tidak Tersedia")
    beli_lagi = input("Mau Isi Pulsa Lagi? (y/n): ")
