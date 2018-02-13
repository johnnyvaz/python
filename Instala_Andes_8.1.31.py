import os
import glob
import shutil

current_directory = os.path.dirname(os.path.abspath(__file__))

arquivos = [arq for arq in current_directory if os.path.isfile(arq)]
pasta = "c:\\andeserp"

caminhos = [os.path.join(pasta, nome) for nome in os.listdir(pasta)]
#print caminhos

arquivos = [arq for arq in caminhos if os.path.isfile(arq)]
# print arquivos

bpls = [arq for arq in arquivos if arq.lower().endswith(".bat")]
print bpls

# files = glob.glob(current_directory + 'app' + '*.log')
# for file in files:
#     print(file)
#     os.unlink(file)

        
# REM - PARA SERVIÇO
# net stop AndesLogTransfer
# REM DESINSTALA SERVIÇOS
# c:\andesERP\AndesLogTransfer.exe /uninstall /s
# cd\
# cd andeserp
# del AndesLogTransfer.exe AndesUpdateConfig.exe AndesUpdateGUI.exe
# del AndesLogTransfer.zip AndesUpdateConfig.zip AndesUpdateGUI.zip
# del AndesLogTransfer.log
# cd app
# del AndesLogTransfer.exe
# del AndesLogTransfer.zip
# del AndesUpdateConfig.exe
# del AndesUpdateConfig.zip
# del AndesUpdateGUI.exe
# del AndesUpdateGUI.zip
# cd ..
# cd log
# del *.log
# pause

# remover diretório inteiro
#shutil.rmtree(current_directory + '\\teste2')

# tree = ET.parse('arquivos\AndesConfiguracao.xml')



    

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