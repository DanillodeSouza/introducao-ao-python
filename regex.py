import re

def procurar_match():
	print re.match('B', 'Barreto').group()


def procurar_ocorrencias():
	print re.findall('B\w+', 'Barreto Bonito')