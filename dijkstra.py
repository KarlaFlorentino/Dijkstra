#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def matriz(arquivo):
	#Transformando arquivo em uma matriz
	conteudo = open(arquivo, 'r').readlines()
	matriz = []
	linha = []

	for i in range(len(conteudo)):
		for j in range(len(conteudo)):
			linha.append((conteudo[i].split(" ")[j]).replace('\n', ''))
			
		matriz.append(linha)
		linha = []
	return matriz

def nosAdjacentes(matriz):
	#Transformando matriz em "lista de adjacência"
	nosAdjacentes = []
	linha = []
	for i in range(len(matriz)):
		for j in range(len(matriz)):
			if(matriz[i][j] != "1024"):
				linha.append(str(j) + " "+ matriz[i][j])
		nosAdjacentes.append(linha)
		linha = []
	return nosAdjacentes

def dijkstra(nosAdjacentes, inicio, fim):
	visitouNos = [0] * len(nosAdjacentes) #Vetor que marca os nós já visitados ou "coloridos"
	solucao = [] #Vetor que guarda os passos para a solução
	linha = [] #Vetor auxiliar para adicionar no vetor solucao
	local = [0] * len(nosAdjacentes) #Vetor auxiliar para guardar o local do noAnterior dentro do vetor solucao

	#iniciando as variáveis...
	linha.append ('- ' + inicio + ' 0') #Adicionando inicio no vetor solucao
	solucao.append(linha)
	visitouNos[int(inicio)] = 1 #Colorindo inicio
	noAtual = int(inicio)
	distanciaNoAtual = 0 #Variável auxiliar que guarda a distâncio do nó atual
	noAnterior = "" #Variável auxiliar que guarda o nó anterior
	distanciaNoAnterior = 0 #Variável auxiliar que guarda a distância do nó anterior	
	menorAdj = "" #Variável auxiliar que guarda o menor adjacente
        distanciaAdj = "" #Variável auxiliar que guarda a distância do menor adjacente
	
	while visitouNos[int(fim)] != 1:
		menorAdj = (nosAdjacentes[noAtual][0]).split(" ")[0]
		distanciaAdj = int((nosAdjacentes[noAtual][0]).split(" ")[1]) + int(distanciaNoAtual)
		#Comparando os adjacentes do no Atual
		for i in range(1,len(nosAdjacentes[noAtual])):
			if(visitouNos[int(menorAdj)] != 1):
				if(int(menorAdj) == int(fim) ):
					noAnterior = noAtual
				else:
					adj2 = 	(nosAdjacentes[noAtual][i]).split(" ")[0]
					if(visitouNos[int(adj2)] != 1):	
						distanciaAdj2 = int((nosAdjacentes[noAtual][i]).split(" ")[1]) + int(distanciaNoAtual)
						if(distanciaAdj2 < distanciaAdj) :				
							menorAdj = adj2
				                	distanciaAdj = distanciaAdj2
							noAnterior = noAtual

			elif(noAnterior == int(inicio) or visitouNos[int(menorAdj )] == 1):
				menorAdj = (nosAdjacentes[noAtual][i]).split(" ")[0]
				distanciaAdj = int((nosAdjacentes[noAtual][i]).split(" ")[1]) + int(distanciaNoAtual)
			
		if(noAnterior == ""):
			noAnterior = noAtual
		#Comparando os adjacentes não visitados ou "coloridos" do nó anterior com o menor adjcante do nó atual		
		distanciaNoAnterior = (solucao[local[int(noAnterior)]][0]).split(" ")[2]		
		
		if(len(solucao) > 2 and noAnterior != int(inicio) and int(menorAdj) != int(fim)):
			for i in range(len(nosAdjacentes[int(noAnterior)])):
				adj2 = 	(nosAdjacentes[noAnterior][i]).split(" ")[0]				
				if(visitouNos[int(adj2)] != 1):	
					distanciaAdj2 = int((nosAdjacentes[noAnterior][i]).split(" ")[1]) + int(distanciaNoAnterior)
					if(distanciaAdj2 < distanciaAdj):				
						menorAdj = (nosAdjacentes[noAnterior][i]).split(" ")[0]
				                distanciaAdj = distanciaAdj2
						
				
		linha = []
		linha.append(str(noAnterior) + ' ' + str(menorAdj) + ' ' + str(distanciaAdj))
		#Adicionando menor nó adjacente no vetor solucao 				
		solucao.append(linha)
		visitouNos[int(menorAdj)] = 1 #Atualizando visita ou "cor"
		local[int(menorAdj)] = len(solucao) -1	#Atualizando local dentro do vetor solucao	
		noAtual = int(menorAdj)  #Atualizando no Atual
		distanciaNoAtual = int(distanciaAdj) #Atualizando distancia do no Atual
		
	return solucao

def exibirSolucao(solucao,inicio, fim):
	#Exibindo solucao o terminal
	if(inicio == fim):
		print(inicio)
	else:
		sol=""
		sol += (solucao[(len(solucao)-1)][0]).split(" ")[1]
		sol += " "
		depois = (solucao[(len(solucao)-1)][0]).split(" ")[0]

		while int(depois) != int(inicio):
			for i in range(1,len(solucao)-1):			
				if((solucao[i][0]).split(" ")[1] == depois):
					sol += (solucao[i][0]).split(" ")[1]
					sol += " "
					depois = (solucao[i][0]).split(" ")[0]
		sol += (solucao[0][0]).split(" ")[1]
		print(sol[::-1])

param = sys.argv[1:]
arquivo = param[0]
inicio = param[1]
fim = param[2]

nosAdjacentes = nosAdjacentes(matriz(arquivo))
exibirSolucao(dijkstra(nosAdjacentes,inicio,fim),inicio,fim)

