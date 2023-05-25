import Pyro4

uri = "PYRO:obj_81ee0fcf8f5d4d158a3cd3279fec6496@192.168.1.114:9090"
servico_remoto = Pyro4.Proxy(uri)

saudacao = servico_remoto.saudacao()
resultado = servico_remoto.somar(2, 3)

print("Resposta do servidor:", saudacao)
print("Resultado da soma:", resultado)