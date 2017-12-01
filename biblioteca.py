def gera_nome_convite(nome):
	parte1 = nome[0:4]
	tamanho_nome = len(nome)
	parte2 = nome[tamanho_nome-4:tamanho_nome]
	return parte1 + ' ' + parte2

def envia_convite(nome_formatado):
	print 'Enviando convite para %s' % nome_formatado

def processa_convite(nome):
	envia_convite(gera_nome_convite(nome))