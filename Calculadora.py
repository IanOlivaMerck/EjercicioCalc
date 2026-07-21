"""
Module: Calculadora.py
Purpose: Este módulo es el modulo principal para el uso de funciones como calculadora
Date: 21JUL26
Author: I. Oliva
"""
import string
import Func_SumaResta as SR


def run():
  a=float(input("dame un numero"))
  b=float(input("dame otro numero"))
  operacion=(input("que quieres hacer?"))
  operacion=operacion.lower()
  if operacion=="suma":
    result=SR.sum(a, b)
  elif operacion=="resta":
    result=SR.rest(a, b)
  print("el resultado es", result)

if __name__=="__main__":
  run()