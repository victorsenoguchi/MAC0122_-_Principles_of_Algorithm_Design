#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 16:33:08 2019

@author: victor borges
"""

class pilha:
    
    def __init__(self): #Inicia uma pilha.
        self.pilha = []
        
    def __len__(self): #Devolve o tamanho da pilha.
        return len(self.pilha)
    
    def is_empty(self): #Verifica se a pilha está vazia.
        return len(self.pilha) == 0
    
    def push(self,e): #Insere um elemento no topo da pilha.
        self.pilha.append(e)

    def top(self): #Devolve o topo da pilha.
        if self.is_empty():
            return None
        return self.pilha[-1]
    
    def pop(self): #Remove o topo da pilha.
        if self.is_empty():
            return None
        return self.pilha.pop()
    
def ler(arquivo): #Função para ler o arquivo de texto a ser classificado.
    
    try: 
        arq = open(arquivo,"r")
    except: 
        return None
    registros = []
    for linha in arq:
        A = ""
        l = linha.split()
        for k in range(len(l)-1):
            A += l[k] + " "
        A += l[k+1]
        registros += [A]
    arq.close()
    return registros

def criar(arquivo,destino): #Cria arquivo texto classificado.
    
    file = open(destino, "w+")
    for k in range(len(arquivo)):
        for l in range(len(arquivo[k])):
            file.write(arquivo[k][l])
        file.write("\n")
                                         
def reverse(registros):
    
    name =  [1*"" for k in range(len(registros))]
    nasc = [1*"" for k in range(len(registros))]
    dia = [1*"" for k in range(len(registros))]
    mes = [1*"" for k in range(len(registros))]
    ano = [1*"" for k in range(len(registros))]
    ident = [1*"" for k in range(len(registros))]
    for k in range(len(registros)):
        l = 0 
        while registros[k][l] != ",":
            name[k] += registros[k][l]
            l += 1
            if len(name[k]) > 40:
                print("O nome do registro", k+1, "do arquivo ultrapassou o número máximo de caracteres.")
                return None
            if l >= len(registros[k]):
                print("O registro", k+1, "do arquivo lido não estão no formato correto.")
                return None
        name[k] += ","
        l += 1
        while registros[k][l] != "/":
            dia[k] += registros[k][l]
            l += 1
            if l >= len(registros[k]):
                print("O registro", k+1, "do arquivo lido não estão no formato correto.")
                return None
        if len(dia[k]) != 2:
            print("O dia de nascimento do", k+1, "registro do arquivo lido está incorreto.")
            return None
        l += 1
        if l >= len(registros[k]):
            print("O registro", k+1, "do arquivo lido não estão no formato correto.")
            return None
        while registros[k][l] != "/":
            mes[k] += registros[k][l]
            l += 1
            if l >= len(registros[k]):
                print("O registro", k+1, "do arquivo lido não estão no formato correto.")
                break
        if len(mes[k]) != 2:
            print("O mês de nascimento do registro", k+1, "do arquivo lido está incorreto.")
            return None
        l += 1
        if l >= len(registros[k]):
            print("O registro", k+1, " do arquivo lido não estão no formato correto.")
            return None
        while registros[k][l] != ",":
            ano[k] += registros[k][l]   
            l += 1
            if l >= len(registros[k]):
                print("O registro", k+1, "do arquivo lido não estão no formato correto.")
                return None
        if len(ano[k]) != 4:
            print("O ano de nascimento do registro", k, "do arquivo lido está incorreto.")
            return None
        nasc[k] = ano[k] + "/" + mes[k] + "/" + dia[k] + ","
        l += 1
        if l >= len(registros[k]):
            print("O registro", k+1, "do arquivo lido não estão no formato correto.")
            break
        while l in range(len(registros[k])):
            ident[k] += registros[k][l]
            l += 1
            if l > len(registros[k]):
                print("O registro", k+1, "do arquivo lido não estão no formato correto.")
                break
        registros[k] = name[k] + nasc[k] + ident[k]
    return registros

def back(registros):
    
    name = [1*"" for k in range(len(registros))]
    nasc = [1*"" for k in range(len(registros))]
    dia = [1*"" for k in range(len(registros))]
    mes = [1*"" for k in range(len(registros))]
    ano = [1*"" for k in range(len(registros))]
    ident = [1*"" for k in range(len(registros))]
    for k in range(len(registros)):
        l = 0 
        while registros[k][l] != ",":
            name[k] += registros[k][l]
            l += 1
        name[k] += ","
        l += 1
        while registros[k][l] != "/":
            ano[k] += registros[k][l]
            l += 1
        l += 1
        while registros[k][l] != "/":
            mes[k] += registros[k][l]
            l += 1
        l += 1
        while registros[k][l] != ",":
            dia[k] += registros[k][l]   
            l += 1
        l += 1
        nasc[k] = dia[k] + "/" + mes[k] + "/" + ano[k] + ","
        while l in range(len(registros[k])):
            ident[k] += registros[k][l]
            l += 1
        registros[k] = name[k] + nasc[k] + ident[k]
    return registros

def particiona(lista, inicio, fim):
    
    i,j = inicio, fim
    pivo = lista[fim]
    while True:
        while i<j and lista[i] <= pivo:
            i += 1
        if i < j:
            lista[i], lista[j] = pivo, lista[i]
        else:
            break
        while i < j and lista[j] >= pivo:
            j -= 1
        if i < j:
            lista[i], lista[j] = lista[j], pivo
        else:
            break
    return i
    
def ClassQuickRecursivo(registros, inicio, fim): #Método Quick Recursivo.
    
    if inicio < fim:
        k = particiona(registros, inicio, fim)
        ClassQuickRecursivo(registros, inicio, k - 1)
        ClassQuickRecursivo(registros, k + 1, fim)
    return registros

def ClassQuickNaoRecursivo(registros): #Método Quick Não Recursivo.
    
    p = pilha()
    p.push((0, len(registros) - 1))
    while not p.is_empty():
        inicio, fim = p.pop()
        if fim - inicio > 0:
            k = particiona(registros, inicio, fim)
            p.push((inicio, k - 1))
            p.push((k + 1, fim))
    return registros
    
def VerifClass(registros):
    
    reverse(registros)
    for k in range(len(registros)-1):
        if registros[k+1] < registros[k]:
            return False
        else:
            back(TAB)
            return True
    
import time
while True:
    origem = input("Entre com o nome do arquivo origem:")
    TAB = ler(origem)
    if origem == "fim":
        break
    elif TAB is not None:
        destino = input("Entre com o nome do arquivo destino:")
        print("Quantidade de registros a classificar:", len(TAB), "registros")
        if reverse(TAB) is None:
            continue
        else:
            print("Tempo para classificar a tabela:")
            t1 = time.process_time()
            ClassQuickRecursivo(TAB, 0, len(TAB)-1)
            t2 = time.process_time()
            back(TAB)
            print("Método Quick Recursivo: ", t2 - t1, "segundos")
            if VerifClass(TAB) is True:
                criar(TAB, destino)
                print("A tabela foi classificada com sucesso pelo Método do Quick Recursivo.")
            TAB = ler(origem)
            reverse(TAB)
            t3 = time.process_time()
            ClassQuickNaoRecursivo(TAB)
            t4 = time.process_time()
            back(TAB)
            print("Método Quick Não Recursivo: ", t4 - t3, "segundos")
            if VerifClass(TAB) is True:
                criar(TAB, destino)
                print("A tabela foi classificada com sucesso pelo Método do Quick Não Recursivo.")
            TAB = ler(origem)
            TAB = reverse(TAB)
            t5 = time.process_time()
            TAB.sort()
            t6 = time.process_time()
            TAB = back(TAB)
            print("Método sort() do python: ", t6 - t5, "segundos")
            if VerifClass(TAB) is True:
                criar(TAB, destino)
                print("A tabela foi classificada com sucesso pelo Método Sort.")
    else:
        print("O arquivo lido está vazio.")
