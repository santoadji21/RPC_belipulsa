import zerorpc

c = zerorpc.Client()
c.connect("tcp://127.0.0.1:4242")

class Provider(object):
    @staticmethod
    def provider_pulsa(nominal, nomorhp, saldo):
        print(c.beli_pulsa(nominal, saldo))
        resi = c.beli_pulsa(nominal, saldo)
        return "Anda Akan Membeli Pulsa Sebesar: Rp."  +  str(nominal) + '\n' + "Dengan Nomorhp: " + str(nomorhp) + '\n \n' + str(resi)

s = zerorpc.Server(Provider())
s.bind("tcp://0.0.0.0:4243")
s.run()