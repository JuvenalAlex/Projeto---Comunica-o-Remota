import Pyro4

@Pyro4.expose
class MeuServicoRemoto(object):
    def saudacao(self):
        return "Olá, mundo!"

    def somar(self, a, b):
        return a + b

daemon = Pyro4.Daemon(host = '192.168.1.114', port= 9090)
uri = daemon.register(MeuServicoRemoto)

print("URI do objeto remoto:", uri)

daemon.requestLoop()