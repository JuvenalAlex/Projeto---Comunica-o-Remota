import Pyro4

@Pyro4.expose
class MeuServicoRemoto(object):
    def saudacao(self):
        return "Olá,unisjdoaisjdouashduahsdouhsaduohsaudhasofuhfuihado!"

    def calcular_bhaskara(self, a, b, c):
        delta = b**2 - 4*a*c
        if delta < 0:
            return "A equação não possui raízes reais."
        elif delta == 0:
            raiz = -b / (2*a)
            return "A equação possui uma raiz real: x = {:.2f}".format(raiz)
        else:
            raiz1 = (-b + delta**0.5) / (2*a)
            raiz2 = (-b - delta**0.5) / (2*a)
            return "A equação possui duas raízes reais: x' = {:.2f} e x'' = {:.2f}".format(raiz1, raiz2)

daemon = Pyro4.Daemon(host='127.0.0.1', port=9090)
uri = daemon.register(MeuServicoRemoto)

print("URI do objeto remoto:", uri)

daemon.requestLoop()
