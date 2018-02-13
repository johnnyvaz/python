import os
import glob
import shutil
from xml.etree.ElementTree import Element, ElementTree

# current_directory = os.path.dirname(os.path.abspath(__file__))

# os.chdir('teste2')

# files = glob.glob('*.txt')
# for file in files:
#     print(file)
#     os.unlink(file)

# shutil.rmtree(current_directory + '\\teste2')
    
# root = Element('Agenda')
# pessoa = Element('Pessoa') 
# cliente = Element('Cliente', nome='Guilherme', idade='19', peso='71', altura='1.63') 
# root.append(pessoa)
# root.append(cliente)
# ElementTree(root).write('agenda.xml');

tree = ElementTree(file='arquivos\\agenda.xml')
r = tree.getroot()
pessoa = r.find('Pessoa') 
cliente = r.find('Cliente') 
print(cliente.tag, cliente.attrib) 

andesConfig = ElementTree(file='arquivos\\AndesConfiguracao.xml')
a = andesConfig.getroot()
bancos = a.find('bancos')
banco = a.banco.find('dataBase')
#db = bancos.find('caminhoAplicativos')
print(banco.tag, banco.attrib)




# 1 - No banco original de produção precisa ficar assim:
# Sweep interval = 0
# Forced Writes are ON

# 2 - No banco _log deve ficar assim:
# Sweep interval = 0
# Forced Writes are OFF

# Os comandos para alterar esses parâmetros são:
# Para alterar forçar escrita
# %AndesFBXX%\gfix -write async BANCO.fdb -user andpro3dthkmdka -password "y2b%dm/ni|"   (para deixar off o forçar escrita)

# %AndesFBXX%\gfix -write sync BANCO.fdb -user andpro3dthkmdka -password "y2b%dm/ni|"   (para deixar on o forçar escrita)

# Para setar o sweep para zero o comando é:

# %AndesFBXX%\gfix -h 0 BANCO.fdb -user andpro3dthkmdka -password "y2b%dm/ni|"   (para deixar sweep = 0)
# (importante essa alteração porque no score foi detectado que quando chegava a executar o sweep o sistema travava tudo e só reiniciando o servidor para voltar a funcionar.)