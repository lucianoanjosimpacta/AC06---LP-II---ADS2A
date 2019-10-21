# Linguagem de Programação II
# AC06 ADS2A - Banco
#
# Alunos: luciano.gomes@aluno.faculdadeimpacta.com.br
#         gabriel.ogoncalves@aluno.faculdadeimpacta.com.br

from typing import Union, List, Dict
import re

Number = Union[int, float]


class Cliente():
    """
    Classe Cliente do Banco.

    possui os atributos: nome, telefone e email, todos privados
    caso o email não seja um email válido gera um ValueError,
    caso o telefone não seja um número gera um TypeError
    """
    # VERIFICA SE O TELEFONE É VÁLIDO NA CRIAÇÃO DO OBJETO
    def __init__(self, nome: str, telefone: int, email: str):
        if type(telefone) != int:
            raise TypeError("Número de telefone inválido!")
    # VERIFICA SE O EMAIL É VÁLIDO NA CRIAÇÃO DO OBJETO
        email_valid = re.compile(
            r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$"
            )
        if not email_valid.match(email):
            raise ValueError("E-mail inválido!")
        else:
            self.__email = email
        self.__nome = nome
        self.__telefone = telefone

    def get_nome(self) -> str:
        """Acessor do atributo Nome."""
        nome_cliente = self.__nome
        return nome_cliente

    def get_telefone(self) -> int:
        """Acessor do atributo Telefone."""
        tel_cliente = self.__telefone
        return tel_cliente

    def set_telefone(self, novo_telefone: int) -> None:
        """
        Mutador do atributo telefone, caso não receba um número,
        gera um TypeError
        """
        if type(novo_telefone) == int:
            self.__telefone = novo_telefone
        else:
            raise TypeError("O telefone deve ser um número válido")
        return None

    def get_email(self) -> str:
        """Acessor do atributo Email."""
        email_cliente = self.__email
        return email_cliente

    def set_email(self, novo_email: str) -> None:
        """
        Mutador do atributo Email, caso não receba um email válido
        gera um ValueError.
        """
        email_valido = re.compile(
            r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$"
            )

        if not email_valido.match(novo_email):
            raise ValueError("E-mail inválido!")
        else:
            self.__email = novo_email
        return None


class Banco():
    """
    A classe Banco deverá receber um nome em sua construção e deverá
    implementar os métodos:
    * abre_contas: abre uma nova conta, atribuindo o numero da conta em ordem
    crescente.
    * lista_contas(): apresenta um resumo de todas as contas do banco
    DICA: mantenha uma variável interna que armazene todas as contas do banco
    DICA2: utilze a variável acima para gerar automaticamente o número das
    contas do banco
    """
    def __init__(self, nome: str):
        self.__nome = nome
        self.__num_conta = 0
        self.__lista_conta = []

    def get_nome(self) -> str:
        """Acessor do Atributo Nome."""
        nome_banco = self.__nome
        return nome_banco

    def abre_conta(self, clientes: List[Cliente], saldo_ini: Number) -> None:
        """
        Método para abertura de nova conta, recebe os clientes
        e o saldo inicial.
        Caso o saldo inicial seja menor que 0 devolve um ValueError
        """
        # NECESSÁRIO CORRIGIR ESTE MÉTODO
        if len(self.__lista_conta) >= 0:
            self.__num_conta += 1
        if saldo_ini < 0:
            raise ValueError("Saldo inválido!")
        nova_conta = Conta(clientes, self.__num_conta, saldo_ini)
        self.__lista_conta.append(nova_conta)
        return None

    def lista_contas(self) -> List['Conta']:
        """Retorna a lista com todas as contas do banco."""
        listas_contas = self.__lista_conta
        return listas_contas


class Conta():
    """
    Classe Conta.
    * Todas as operações (saque e deposito, e saldo inicial) devem aparecer
    no extrato como tuplas, exemplo ('saque', 100), ('deposito', 200) etc.
    * Caso o saldo inicial seja menor que zero deve lançar um ValueError
    * A criação da conta deve aparecer no extrato com o valor
    do saldo_inicial, exemplo: ('saldo_inicial', 1000)
    DICA: Crie uma variável interna privada para guardar as
    operaões feitas na conta
    """

    def __init__(self, clientes: List[Cliente], numero_conta: int,
                 saldo_inicial: Number):
        if saldo_inicial < 0:
            raise ValueError("Saldo inicial inválido!")
        self.__clientes = list(clientes)
        self.__numero_conta = numero_conta
        self.__saldo_inicial = saldo_inicial
        self.__operacoes = [
            ('saldo_inicial', saldo_inicial)
        ]

    def get_clientes(self) -> List[Cliente]:
        '''
        Acessor para o atributo Clientes
        '''
        clientes = self.__clientes
        return clientes

    def get_saldo(self) -> Number:
        '''
        Acessor para o Atributo Saldo
        '''
        saldo = self.__saldo_inicial
        return saldo

    def get_numero(self) -> int:
        '''
        Acessor para o atributo Numero
        '''
        num_conta = self.__numero_conta
        return num_conta

    def saque(self, valor: Number) -> None:
        '''
        Método de saque da classe Conta, operação deve aparecer no extrato
        Caso o valor do saque seja maior que o saldo da conta,
        deve retornar um ValueError, e não efetuar o saque
        '''
        if valor > self.__saldo_inicial:
            raise ValueError("Saldo insuficiente!")
        else:
            result_saque = self.__saldo_inicial - valor
            self.__saldo_inicial -= result_saque
        op_saque = ('saque', valor)
        self.__operacoes.append(op_saque)
        return None

    def deposito(self, valor: Number):
        '''
        Método depósito da classe Conta, operação deve aparecer no extrato
        '''
        self.__saldo_inicial += valor
        op_deposito = ('deposito', valor)
        self.__operacoes.append(op_deposito)
        return None

    def extrato(self) -> List[Dict[str, Number]]:
        '''
        Retorna uma lista com as operações (Tuplas) executadas na Conta
        '''
        op_extrato = self.__operacoes
        return op_extrato
