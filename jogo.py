# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 17:52:47 2023

@author: vanessa.oliveira
"""
import forca
import adivinhacao

def escolher_jogo(): 
    print("*********************************")
    print("*******Escolha o seu jogo!*******")
    print("*********************************")
    
    print("(1) Forca (2) Adivinhação")
    jogo = int(input("Qual jogo? "))
    
    if (jogo == 1):
        forca.jogar()
    elif (jogo == 2):
        adivinhacao.jogar()
    
if (__name__ == "__main__"):
    escolher_jogo()