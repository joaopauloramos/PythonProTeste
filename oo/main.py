#!/usr/bin/python3

from framework import Calculadora, CalculadoraInfixa

class CalculadoraPrefixa(Calculadora):
     def obter_inputs(self):
         
        sinal = input('Digite o sinal da operacao: ')
        p1= input('Digite o primeiro o numero ')
        p1 = float(p1)
        p2= input('Digite o primeiro o numero ')
        p2 = float(p2)
        return sinal, p1, p2

calculadora = CalculadoraInfixa()

print(calculadora.efetuar_operacao())

