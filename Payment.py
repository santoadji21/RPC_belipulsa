import zerorpc

class Payment(object):
    @staticmethod
    def beli_pulsa(nominal, saldo):
        if saldo >= nominal:
            saldo -= nominal
            return "Anda Berhasil Membeli Pulsa Rp." + str(nominal) + ' \n' +"Sisa Saldo Anda Adalah Rp." + str(saldo)
        else:
            return "\nMaaf Saldo Anda Tidak Cukup Untuk Membeli Pulsa Sebesar Rp." + str(nominal) + '\n' + "Transaksi Dibatalkan ...."

s = zerorpc.Server(Payment())
s.bind("tcp://0.0.0.0:4242")
s.run()