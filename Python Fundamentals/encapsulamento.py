class Conta:
    def __init__(self, nro_agencia, saldo=0):
        # Atributo privado:
        self._saldo = saldo
        # Atributo público:
        self.nro_agencia = nro_agencia

    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        self._saldo -= valor

    def mostrar_saldo(self):
        return self._saldo

conta = Conta("260", 100)
conta.depositar(100)
print(conta.nro_agencia)
print(conta.mostrar_saldo())