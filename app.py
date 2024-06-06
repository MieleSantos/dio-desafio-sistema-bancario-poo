from abc import ABC, abstractclassmethod, abstractproperty
from datetime import date


class Cliente:
    def __init__(self, endereco: str) -> None:
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(
        self, endereco: str, cpf: str, nome: str, data_nascimento: date
    ) -> None:
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento


class Conta:

    def __init__(self, numero: int, cliente: Cliente) -> None:
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        # self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente: Cliente, numero: int):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor: float):
        saldo = self.saldo

        if valor > saldo:
            print("\n Você não tem saldo suficiente")
        elif valor > 0:
            self._saldo -= valor
            print("f\nSaque no valor {} reais realizado com sucesso")
        else:
            print("\n O valor informado é invalido")


class ContaCorrente:
    def __init__(self, limite: float, limite_saques: int) -> None:
        self.limite = limite
        self.limite_saques = limite_saques
