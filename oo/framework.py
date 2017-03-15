#!/usr/bin/python3

class Operacao:
    """ Classe responsavel por definir como calculo deve ser feito"""
    def calcular(self,p1,p2):
        raise NotImplementedError("Precisa ser implementado")

class Calculadora:
    """ Classe Responsavel por obter inputs e efetuar a operacao de acordo com o solicitado"""
    def __init__(self):
        self._operacoes = {}

    def obter_inputs(self):
        """Deve obter sinal, p1 e p2 retornando os valores nessa ordem"""

        raise NotImplementedError('Precisa ser implementado')

    def efetuar_operacao(self):
        sinal, p1,p2 = self.obter_inputs()
        try:
            operacao_escolhida = self._operacoes[sinal]
        except KeyError:
           raise Exception("Operacao nao suportada")
        else:
            return operacao_escolhida.calcular(p1,p2)

    def adicionar_operacao(self, operacao):
        self.operacoes[sinal]=operacao


class CalculadoraInfixa(Calculadora):
    def obter_inputs(self):
        

    
