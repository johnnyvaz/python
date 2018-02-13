# -*- coding: utf-8 -*-
# '''
# 	Sintese:
# 		Objetivo : Demonstrar manipulacao de arquivos XML em Python
# 		Entrada : Uma URL com XML - WebService do INMET
# 		Saída : Uma tag do arquivo
# 		Autor : f_Candido	<fagner7777777@gmail.com>	@fagner_candido
# '''

# Importacoes
import urllib2
from xml.dom import minidom

class Previsao():
    # URL do INMET - WebService
    url = 'http://www.inmet.gov.br/webservice/previsao/?geraXml=&TP=CP&CP=BRAS%CDLIA& '
    fonte = ''
    xmlDoc = ''
    listaEstado = []

    def __init__(self):
	# '''
	# 	Construtor onde e recebido a URL
	# 	Alem de ser convertido para objeto XML
	# '''
        try:
            self.fonte = urllib2.urlopen(self.url).read()
        except:
            self.fonte = 'URL Inválida'
	self.xmlDoc = minidom.parseString(self.fonte)
        

    def getTag(self, tag):
	# '''
	# 	Obtem a tag pegando por valor
	# '''
        self.listaEstado = self.xmlDoc.getElementsByTagName(tag)

    def listElement(self):
	# '''
	# 	Percorre os elementos
	# '''
        for x in self.listaEstado:
            print x.toxml()


objPrevisao = Previsao()
listaEstado = objPrevisao.getTag('estado')
objPrevisao.listElement()
