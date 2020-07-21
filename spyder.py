# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 19:53:39 2020

@author: benja
"""
import pandas as pd


table = pd.read_csv("C:/Users/benja/Desktop/projetinApi/fontes/c2dd862cd38f21b0ad36b8f96b4bf1ee-1d92663004489a5b6926e944c1b3d9ec5c40900e/Periodic Table of Elements.csv")
test1 = table.loc[:,['Element','Symbol','AtomicNumber','NumberofNeutrons','NumberofProtons',
                     'NumberofElectrons','Phase','Radioactive','Type']]
test2 = test1.iloc[:].values
i,j,matrix = 0,0,[[]] 
while i<118:
    primeiroElemento = test2[i][:]
    dict = {'Element':primeiroElemento[j],'Symbol':primeiroElemento[j+1],
            'AtomicNumber':primeiroElemento[j+2],'NumberofNeutrons':primeiroElemento[j+3],
            'NumberofProtons':primeiroElemento[j+4],'NumberofElectrons':primeiroElemento[j+5],
            'Phase':primeiroElemento[j+6],'Radioactive':primeiroElemento[j+7],'Type':primeiroElemento[j+8]}
    matrix.append(dict)
    i += 1