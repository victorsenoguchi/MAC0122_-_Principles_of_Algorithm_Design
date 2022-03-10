#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 18:29:55 2019

@author: victor senoguchi borges
@numero usp: 9298580
"""

def ler(arquivo): # Função para ler a matriz de um arquivo txt.
    try: 
        arq = open(arquivo,"r")
    except: 
        return []
    matriz = [9 * [0] for k in range(9)]
    i = 0
    for linha in arq:
        l = linha.split()
        if len(l) != 9:
            return [] 
        for j in range(len(l)):
            try:
                matriz[i][j] = int(l[j])
            except:
                return []
            if int(l[j]) not in range(10):
                return []               
        i = i + 1
    arq.close()
    return matriz 

def ImprimeMatriz(matriz): # Imprime a matriz.
    for i in range(len(matriz)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - - - ")
        for j in range(len(matriz[i])):
            if j % 3 == 0 and j != 0:
                print("| ", end="")
            if j == 8:
                print(matriz[i][j])
            else:
                print(str(matriz[i][j]) + " ", end = " ")
    print(" ")
        
        
   
def TestaMatrizLida(matriz): # Testa se as linhas, as colunas e os quadrados da matriz. estão corretos.
    for k in range(1, 10):
            for i in range(9): 
                d1, d2 = 0, 0
                for j in range(9):
                    if matriz[i][j] == k:
                        d1 = d1 + 1
                    if matriz[j][i] == k:
                        d2 = d2 + 1
                    if ((d1 > 1) or (d2 > 1)):
                        return -1
    for a in range(0,9,3):
        for b in range(0,9,3):
            for k in range(1, 10):
                d = 0
                for i in range(3):
                    for j in range(3):
                        if matriz[a+i][b+j] == k:
                            d = d + 1
                        if  d > 1:
                            return -1
    return 1

def TestaMatrizPreenchida(matriz): # Testa se a matriz está preenchida e se está correta.
    for k in range(9):
            for i in range(9): 
                d1, d2 = 0, 0
                for j in range(9):
                    if matriz[i][j] == k+1:
                        d1 = d1 + 1
                    if matriz[j][i] == k+1:
                        d2 = d2 + 1
                    if ((d1 > 1) or (d2 > 1) or (matriz[i][j]) == 0 or (matriz[j][i]) ==0):
                            return -1
    for a in range(0,9,3):
        for b in range(0,9,3):
            for k in range(9):
                d = 0
                for i in range(3):
                    for j in range(3):
                        if matriz[a+i][b+j] == k+1:
                            d = d + 1 
                        if  d > 1:
                            return -1
    return 1 

def ProcuraElementoLinha(matriz, lin, k): # Procura o elemento k na linha L.    
    for j in range(9):
        if matriz[lin][j] == k:
            return -1
    return 1 

def ProcuraElementoColuna(matriz, col, k): # Procura o elemento k na linha L.    
    for i in range(9):
        if matriz[i][col] == k:
            return -1
    return 1 
    
def ProcuraElementoQuadrado(matriz, lin, col, k): # Procura o elemento k no quadrado interno onde esta o elemento mat[L][C]
    if lin > 2:
        a = 3
    if lin < 3:
        a = 0
    if lin > 5:
        a = 6
    if col > 2:
        b = 3
    if col < 3:
        b = 0
    if col > 5:
        b = 6
    for i in range(3):
        for j in range(3):
            if matriz[a+i][b+j] == k:
                return -1
    return 1

def Sudoku(matriz, lin, col): # Devolve todas as soluções possíveis para a matriz do Sudoku que foi lida.
    global s
    for i in range (lin, 9):
        d = 0
        for j in range (9):
            if i == lin and d == 0:
                j,d = col,1
            if matriz[i][j] == 0:
                vp = []
                for k in range(1, 10): # Cria uma lista dos possiveis valores na casa i,j.
                    if ProcuraElementoLinha(matriz, i, k) == 1:
                        if ProcuraElementoColuna(matriz, j, k) == 1:
                            if ProcuraElementoQuadrado(matriz,i,j,k) == 1:
                                vp = vp + [k]
                for valor in vp: # Percorre a lista dos possiveis valores para casa i,j.
                    matriz_auxiliar = [9 * [0] for k in range(9)] # Cria matriz auxiliar para usar o backtracking.
                    for x in range(9):
                        for y in range(9):
                            matriz_auxiliar[x][y] = matriz[x][y] 
                    matriz_auxiliar[i][j] = valor
                    if TestaMatrizPreenchida(matriz_auxiliar) == 1: # Verifica se a matriz do Sudoku está completa e correta.
                        ImprimeMatriz(matriz_auxiliar)
                        print("Essa é uma solução para a matriz lida.")
                        print(" ")
                        s = s + 1
                    Sudoku(matriz_auxiliar,i,j) # Chama a função novamente iniciando a recursão.
                return 

import time
arquivo = str(" ")
while arquivo != "fim": # While para rodar o programa até o usuario digitar com "fim".
    arquivo = input("Entre com o arquivo que contem a matriz do Sudoku: ")
    if arquivo == "fim": # Sair do while se o usuario digitar "fim".
        break
    print(" ")
    matriz = ler(arquivo)
    if matriz == []:
        print("A matriz lida está incorreta")
        continue
    else:
        ImprimeMatriz(matriz)
        print("Essa é a matriz lida.")
        print(" ")
    if TestaMatrizLida(matriz) == 1: # Verifica se a matriz do Sudoku está completa e correta.
        tempo1 = time.process_time()
        s = 0
        Sudoku(matriz, 0, 0) # Devolve todas as soluções possiveis.
        tempo2 = time.process_time()
        tempo_decorrido = tempo2 - tempo1 # Indica o tempo gasto para o programa achar todas as soluções para a matriz lida.
        print("a matriz lida tem", s, "soluções")
        print("tempo decorrido =", tempo_decorrido, "segundos")
    else:
        print("A matriz lida não está correta.")
