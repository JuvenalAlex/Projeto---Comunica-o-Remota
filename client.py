import Pyro4

uri = "PYRO:obj_63f1d16e2ec843028788b36b85e322d9@127.0.0.1:9090"
servico_remoto = Pyro4.Proxy(uri)

saudacao = servico_remoto.saudacao()

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

resultado = servico_remoto.calcular_bhaskara(a, b, c)

print("Resposta do servidor:", saudacao)
print("Resultado da fórmula de Bhaskara:", resultado)
