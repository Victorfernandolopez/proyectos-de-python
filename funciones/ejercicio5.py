"""
Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un cilindro usando la primera función.
"""
import math

def area_circulo(radio):
    area = math.pi * radio**2
    return area

def volumen(radio,altura):
    volumen = area_circulo(radio) * altura
    return volumen

print(volumen(23,23))