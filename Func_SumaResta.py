"""
Module: Calculadora.py
Purpose: Este módulo es el modulo principal para el uso de funciones como calculadora
Date: 21JUL26
Author: I. Oliva
"""


def sum(a, b):
    return(a+b)
def rest(a, b): 
    return (a-b)
def run():
    print(sum(5, 3))
    print(rest(5, 3))
if __name__ == "__main__":
    run()