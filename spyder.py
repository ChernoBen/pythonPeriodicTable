# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 19:53:39 2020

@author: benja
"""
import pandas as pd

'''load csv'''
table = pd.read_csv("C:/Users/benja/Desktop/projetinApi/fontes/c2dd862cd38f21b0ad36b8f96b4bf1ee-1d92663004489a5b6926e944c1b3d9ec5c40900e/Periodic Table of Elements.csv")

'''Filtering table by index'''
firstfill = table.loc[:,['Element','Symbol','AtomicMass','AtomicNumber','NumberofNeutrons','NumberofProtons',
                     'NumberofElectrons','Phase','Radioactive','Type']]
'''replacing nan values'''
firstfill['Radioactive'] = firstfill['Radioactive'].fillna("no")

'''filtering by values'''
secondfill = firstfill.iloc[:].values

''' Creating a list of dictionaries'''
i,j,matrix = 0,0,[] 
while i<118:
    primeiroElemento = secondfill[i][:]
    dict = {'Element':primeiroElemento[j],'Symbol':primeiroElemento[j+1],'AtomicMass':primeiroElemento[j+2],
            'AtomicNumber':primeiroElemento[j+3],'NumberofNeutrons':primeiroElemento[j+4],
            'NumberofProtons':primeiroElemento[j+5],'NumberofElectrons':primeiroElemento[j+6],
            'Phase':primeiroElemento[j+7],'Radioactive':primeiroElemento[j+8],'Type':primeiroElemento[j+9]}
    matrix.append(dict)
    i += 1

   
for valor in matrix:
    pr = valor['Element']
    print(pr)