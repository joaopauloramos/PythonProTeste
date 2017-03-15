#!/usr/bin/python3

def calcular_iterativamente():
    p1 = input('Digite o primeiro numero: ')
    p1 = float(p1)
    sinal = input('Digite o sinal de operação: ( + ou - )')
    p2 = input('Digite o primeiro numero: ')
    p2 = float(p2)
    if sinal == '+':
        return p1 + p2

    elif sinal == '-':
        return p1 - p2
    raise Exception('Operacao nao suportada')