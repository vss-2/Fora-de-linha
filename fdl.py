import os
import sys

arquivoinput = sys.argv[1]

try:
	print('Vou ler o arquivo chamado: ')
	print(arquivoinput, end='\n\n\n')
	arquivo = open(arquivoinput)
	linha = arquivo.readline()
	contador = 1
	while linha:
		if(linha[0:3] == '<p>' or linha[0:7] == '<title>'):
			linha = arquivo.readline()
			print(linha, end='')
			contador = contador + 1
		else:
			linha = arquivo.readline()
			
finally:
	arquivo.close()
