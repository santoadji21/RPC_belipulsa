import zerorpc

# nominal= int(input("Masukan Nominal \t: "))
# nomorhp = input("Masukan Nomorhp \t: ")
# saldo = int(input("Masukan Saldo \t\t: "))

nominal= 500
nomorhp = 8059642
saldo = 20000

c = zerorpc.Client()
c.connect("tcp://127.0.0.1:4243")
print(c.provider_pulsa( nominal, nomorhp , saldo))