#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Tue Sep 10 18:29:55 2019

@author: victor senoguchi borges
@numero usp: 9298580

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
        
    def reverse(self):
        reversa = pilha()
        while self.is_empty() == False:
            reversa.push(self.top())
            self.pop()
        return reversa
        
def prioridade(ex, Tabvar = []): #Devolve a prioridade dos operadores.
    
    if ex == "=": return 1
    elif ex == "-": return 2
    elif ex == "+": return 2
    elif ex == "*": return 3
    elif ex == "/": return 3
    elif ex == "^": return 4 
    elif ex == "~": return 5
    elif ex == "(": return 6
    elif ex == ")": return 7
    elif ex in Tabvar: return 0
    elif ex is None: return 0
    else: return 0  
       
def traduzposfixa(a): #Recebe uma expressão aritmética e devolve ela na notação pós-fixa.
    
   operadores = pilha()
   polonesa = pilha()
   for k in range(len(a)):
      if prioridade(a[k]) < 1:
           polonesa.push(a[k])
      elif prioridade(a[k]) == 7: 
           for j in range(len(operadores),0,-1):
                while prioridade(operadores.top()) != 6:
                    polonesa.push(operadores.top())
                    operadores.pop()
           operadores.pop()
      elif prioridade(a[k]) < 7:
           if prioridade(a[k]) <= prioridade(operadores.top()) and prioridade(operadores.top()) != 6:
                polonesa.push(operadores.top())
                operadores.pop()
                operadores.push(a[k])                    
           else:
                operadores.push(a[k])      
   while operadores.top() is not None:
       polonesa.push(operadores.top())
       operadores.pop()
   return polonesa

def calcposfixa(polonesa, Tabvar, Tabval): #Calcula o valor da expressão aritmética.
    b = pilha()
    polonesa = polonesa.reverse()
    if polonesa.is_empty():
        return None
    else:
        while not polonesa.is_empty():
            if prioridade(polonesa.top()) == 0: #Caso em que o topo da pilha é um operando.
                c = val(polonesa.top(), Tabvar, Tabval)
                if c is None:
                    return None
                b.push(c)
                polonesa.pop()
            elif prioridade(polonesa.top()) == 2: #Caso em que topo da pilha é um operador binario + ou -.
                c = b.top()
                b.pop()
                d = b.top()
                b.pop()
                c = val(c, Tabvar,Tabval)
                d = val(d, Tabvar,Tabval)
                if (c is None) or (d is None):
                    return None
                if polonesa.top() == "-":
                    b.push(d-c)
                    polonesa.pop()
                else:
                    b.push(d + c)
                    polonesa.pop()
            elif prioridade(polonesa.top()) == 3: #Caso em que topo da pilha é um operador binario * ou /
                c = b.top()
                b.pop()
                d = b.top()
                b.pop()
                c = val(c, Tabvar,Tabval)
                d = val(d, Tabvar,Tabval)
                if (c is None) or (d is None):
                    return None
                if polonesa.top() == "*":
                    b.push(d * c)
                    polonesa.pop()
                else:
                    b.push(d / c)
                    polonesa.pop()
            elif prioridade(polonesa.top()) == 4: #Caso em que topo da pilha é um operador unário **.
                c = b.top()
                b.pop()
                d = b.top()
                b.pop()
                c = val(c, Tabvar,Tabval)
                d = val(d, Tabvar,Tabval)
                if (c is None) or (d is None):
                    return None
                b.push(d ** c)
                polonesa.pop()
            elif prioridade(polonesa.top()) == 5: #Caso em que topo da pilha é um operador unário -.
                c = b.top()
                b.pop()
                c = val(c, Tabvar,Tabval)
                if c is None:
                    return None
                b.push(-1 * c)
                polonesa.pop()
        return b.top()
 
def atribuicao(ex,Tabvar,Tabval): #Verifica se a expressão lida é uma atribuição e caso seja inclui ela na lista de variaveis e valores.
    igual = "="    
    var, value = ex.split(igual)
    var = var.rstrip().lstrip()
    value = corrigestr(value).split()
    value = traduzposfixa(value)
    value = str(calcposfixa(value, Tabvar, Tabval))
    if var in Tabvar:
       Tabval[Tabvar.index(var)] = value
    else:
       Tabvar += [var]
       Tabval += [value]
    return Tabvar, Tabval

def val(ex, Tabvar, Tabval): #Verifica se uma string é um número.
    if ex in Tabvar:
        ex = Tabval[Tabvar.index(ex)]
    try:
        ex = float(ex)
        return ex
    except:
        return None
    
def corrigestr(ex): #Lê uma expressão aritmética e devolve ela de uma forma que dê para usar a função split.
    
    a = " "
    b = pilha()
    for k in range(len(ex)):
        if ex[k] == " ":
            continue
        elif ex[k] == "-": #Caso em que o - é um operador unário.
            if b.is_empty():
                a+= " ~ "
                b.push("~")
            else:
                if prioridade(b.top()) > 0:
                    a+= " ~ "
                    b.push("~")
                else:
                    a+= " " + ex[k] + " "
                    b.push("~")
        elif ex[k] == "*": #Caso em que * faz parte do operador **.
            if b.top() == "^":
                continue
            j = k+1
            try:
                while ex[j] == " ":
                    j += 1
                if ex[j] == "*":
                    k = j+1
                    a+= " ^ "
                    b.push("^")
                else:
                    a += " " + ex[k] + " "
                    b.push("*")
            except:
                a += " " + ex[k] + " "
                b.push("*")
        elif prioridade(ex[k]) == 0:
            b.push(ex[k])
            a += ex[k]
        else: 
            a += " " + ex[k] + " "
            b.push(ex[k])
    return a

def reverse(polonesa): #Reverte uma pilha.
    reversa = pilha()
    while polonesa.is_empty() == False:
        reversa.push(polonesa.top())
        polonesa.pop()
    return reversa


Tabvar = [] #Tabela de variáveis.
Tabval = [] #Tabela de valores das veriáveis.
while True:
    igual = "="
    ex = input()
    if ex == 'fim': break
    elif igual in ex: # Caso em que a expressão aritimética lida é uma atribuição.
        print(end = "")
        Tabvar, Tabval = atribuicao(ex, Tabvar,Tabval)
    else:
        value = corrigestr(ex).split()
        value = traduzposfixa(value) 
        print(calcposfixa(value ,Tabvar,Tabval)) # Valor da expressão aritimética lida.
