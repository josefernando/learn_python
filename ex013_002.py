class ContaBancaria():
    def __init__(self, valor_inicial):
        self.saldo =  valor_inicial

    def depositar(self, valor):
        self.saldo += valor

    def verificar_saldo(self):
        print(f"Saldo: {self.saldo}")

    def sacar(self, valor):
        if valor > self.saldo:
            print(f"Saldo insuficiente: {self.saldo}")
        else:
             self.saldo -= valor

        print(f"Valor: {valor}sacado com sucesso.")

conta001 = ContaBancaria(100)

conta001.depositar(200)

conta001.sacar(100)

conta001.verificar_saldo()