import matplotlib.pyplot as plt
from datetime import date
import csv
import os
import sys
from os import listdir
from tkinter import *
import webbrowser


def main():
    verificador_diretorio()
    gerar_graficos()
    gerar_html()

def alerta(msg):
    class Aplication:
        def __init__(self, master=None):
            self.widget1 = Frame(master)
            self.widget1.pack(side='bottom')
            self.msg = Label(self.widget1,text=msg)
            self.msg['width'] = 75
            self.msg['height'] = 10
            self.msg["font"] = ("Verdana", "12", "italic", "bold")
            self.msg.pack()
    root = Tk()
    Aplication(root)
    root.mainloop()
    

def verificador_diretorio():
    end = 'C:\Gerador_de_Graficos'
    if not os.path.isdir(end):
        os.mkdir(end)
        os.mkdir(end+'\\base')
        os.mkdir(end+'\\graficos')
        os.mkdir(end+'\\graficos\\img')
        alerta('Diretório do programa criado, insira a base de dados em \n C:\Gerador_de_Graficos\\base, e execute o programa novamente')
        sys.exit(10)


def listar_arq():
    end = 'C:\Gerador_de_Graficos\\base\\'
    lista_dir = listdir(end)
    try:
        arq = str(lista_dir[0])
        arq = end + arq
        return arq
    except IndexError:
        alerta('Arquivo de base de dados não encontrado,\n insira-o em C:\Gerador_de_Graficos\\base')
        sys.exit(10)

def obter_idade(dtn):
    dtn = dtn.split('/')
    dtn = [int(dtn[2]),int(dtn[1]), int(dtn[0])]

    data = str(date.today()).split('-')
    hoje = [int(data[0]),int(data[1]), int(data[2])]

    idade = hoje[0] - dtn[0] - 1

    if hoje[1] > dtn[1]:
        idade += 1
    elif hoje[1] == dtn[1]:
        if hoje[2] >= dtn[2]:
            idade += 1
    return idade



def abrir_csv():
    end = listar_arq()
    try:
        arq = csv.reader(open(end,'r',encoding = 'utf8'))
    except FileNotFoundError:
        alerta('Arquivo de base de dados não encontrado, insira-o em C:\Gerador_de_Graficos\base')
        sys.exit(10)

        
    registros = []
    
    for linha in arq:
        linha.append('V')
        registros.append(linha)

    for linha in registros[1:]:
        if obter_idade(linha[4])< 17:
            linha[-1] = 'F'
            
        i = 0
        for l in registros[2:]:
            if linha[2].lower().replace(' ','') == l[2].lower().replace(' ','') and linha[3] == l[3] and not l[-1] == 'F': 
                i += 1
                if i == 2:
                    linha[-1] = 'F'
            
                    
    return registros


def gerar_graficos():
    lista = abrir_csv()

    idade = {'20':0,'21-30':0,'31-40':0,'40+':0}     
    est_civil = {'solteiro':0,'casado':0,'outro':0}
    filhos = {'nao':0,'sim':0}
    escolaridade = {'integral_EPU':0,'maior_EPU':0,'integral_EPA':0,'maior_EPA':0}
    cd_origem = {'franca':0,'regiao':0}
    moradia = {'proprio':0,'financiado':0,'alugado':0}
    locomocao = {'moto':0,'onibus':0,'carro':0,'andando':0,'bicicleta':0}
    renda = {'1':0,'2':0,'3':0,'4ou+':0}
    trabalha = {'nao':0,'nao_na_area':0,'nao_ja_area':0,'sim_area':0,'sim_fora':0}
    periodo_trab = {'manha':0,'tarde':0,'noite':0,'manha_tarde':0,'tarde_noite':0}
    mora = {'sozinho':0,'familia':0,'republica':0}
    compFamiliar = {'1':0,'2':0,'3':0,'4+':0}
    ativRemunerada = {'1':0,'2':0,'3':0,'4+':0}
    info = {'basico':0,'medio':0,'avancado':0}
    idioma = {'ingles':0,'espanhol':0,'outros':0,'nao':0,'ing-esp':0}
    deficiencia = {'sim':0,'nao':0}
    invalido = 0
    
    
    for linha in lista[1:]:
        if linha[-1] == 'F':
            invalido += 1
        else:
            if obter_idade(linha[4]) >= 17 and  obter_idade(linha[4]) <= 20:
                idade['20']+= 1
            elif obter_idade(linha[4]) >= 21 and obter_idade(linha[4]) <= 30:
                idade['21-30']+= 1    
            elif obter_idade(linha[4]) >= 31 and obter_idade(linha[4]) <= 40:
                idade['31-40']+= 1
            elif obter_idade(linha[4]) >= 41:
                idade['40+']+= 1
            

            if linha[6] == 'Solteiro(a)':
                est_civil['solteiro']+=1
            elif linha[6] == 'Casado(a)':
                est_civil['casado']+=1
            elif linha[6] == 'Outro':
                est_civil['outro']+=1

            if linha[7] == 'Não tem filhos':
                filhos['nao']+= 1
            elif int(linha[7]) >= 1:
                filhos['sim']+= 1
            

            if linha[-8] == 'Integralmente em Escola Pública':
                escolaridade['integral_EPU']+= 1
            elif linha[-8] == 'Maior parte em Escola Pública':
                escolaridade['maior_EPU']+= 1
            elif linha[-8] == 'Integralmente em Escola Particular':
                escolaridade['integral_EPA']+= 1
            elif linha[-8] == 'Maior parte em Escola Particular':
                escolaridade['maior_EPA']+= 1    
                
            if linha[8] == 'Franca':
                cd_origem['franca']+= 1
            elif linha[8] == 'Região de Franca':
                cd_origem['regiao']+= 1
            
            if linha[11] == 'Próprio':
                moradia['proprio']+= 1
            elif linha[11] == 'Alugado':
                moradia['alugado']+= 1
            elif linha[11] == 'Financiado':
                moradia['financiado']+= 1

            if linha[9] == 'Moto':
                locomocao['moto']+= 1
            elif linha[9] == 'Ônibus':
                locomocao['onibus']+= 1
            elif linha[9] == 'Carro':
                locomocao['carro']+= 1
            elif linha[9] == 'Andando':
                locomocao['andando']+= 1
            elif linha[9] == 'Bicicleta':
                locomocao['bicicleta']+= 1
            elif linha[10] == 'Moto':
                locomocao['moto']+= 1
            elif linha[10] == 'Ônibus':
                locomocao['onibus']+= 1
            elif linha[10] == 'Carro':
                locomocao['carro']+= 1
            elif linha[10] == 'Andando':
                locomocao['andando']+= 1
            elif linha[10] == 'Bicicleta':
                locomocao['bicicleta']+= 1

            if linha[20] == '1':
                renda['1']+= 1
            elif linha[20] == '2':
                renda['2']+= 1
            elif linha[20] == '3':
                renda['3']+= 1
            elif linha[20] == '4 ou mais':
                renda['4ou+']+= 1

            if linha[18] == 'Nunca trabalhei':
                trabalha['nao']+= 1
            elif linha[18] == 'Não. Nunca trabalhei na área do curso.':
                trabalha['nao_na_area']+= 1
            elif linha[18] == 'Sim. Trabalho na área do curso':
                trabalha['sim_area']+= 1
            elif linha[18] == 'Sim. Trabalho fora da área do curso':
                trabalha['sim_fora']+= 1
            elif linha[18] == 'Não. Já trabalhei na área do curso.':
                trabalha['nao_ja_area']+= 1

            if linha[22] == 'Tarde':
                periodo_trab['tarde']+= 1
            elif linha[22] == 'Noite':
                periodo_trab['noite']+= 1
            elif linha[22] == 'Tarde, Noite':
                periodo_trab['tarde_noite']+= 1    
            if linha[23] == 'Manhã':
                periodo_trab['manha']+= 1
            elif linha[23] == 'Tarde':
                periodo_trab['tarde']+= 1
            elif linha[23] == 'Manhã, Tarde':
                periodo_trab['manha_tarde']+= 1

            if linha[13] == 'Sozinho':
                mora['sozinho']+=1
            elif linha[13] == 'Família':
                mora['familia']+=1
            elif linha[13] == 'Republica':
                mora['republica']+=1

            if linha[17] == '1':
                compFamiliar['1']+=1
            elif linha[17] == '2':
                compFamiliar['2']+=1
            elif linha[17] == '3':
                compFamiliar['3']+=1
            elif linha[17] == '4 ou mais':
                compFamiliar['4+']+=1

            if linha[19] == '1':
                ativRemunerada['1']+=1
            elif linha[19] == '2':
                ativRemunerada['2']+=1
            elif linha[19] == '3':
                ativRemunerada['3']+=1
            elif linha[19] == '4 ou mais':
                ativRemunerada['4+']+=1

            if linha[25] == 'Básico':
                info['basico']+= 1
            elif linha[25] == 'Intermediario':
                info['medio']+= 1
            elif linha[25] == 'Avançado':
                info['avancado']+= 1

            if linha[5] == 'Sim':
                deficiencia['sim']+=1
            elif linha[5] == 'Não':
                deficiencia['nao']+=1

            if linha[28] == '':
                idioma['nao']+=1
            elif linha[28] == 'Inglês':
                idioma['ingles']+=1
            elif linha[28] == 'Espanhol':
                idioma['espanhol']+=1
            elif not linha[28].find('Outros') == -1:
                idioma['outros']+=1
            elif linha[28].replace(' ','') == 'Inglês,Espanhol':
                idioma['ing-esp']+=1
                    
                
    cont = [idade['20'],idade['21-30'],idade['31-40'],idade['40+'],invalido]
    lb = ['até 20 anos','21 a 30 anos','31 a 40 anos','acima de 40 anos','Registros inválidos']
    fig = plt.figure(1,figsize=(9,9))
    leg = plt.subplot(111)
    i = 0
    for l in lb:
        leg.plot(i,label=l)
        i+=1
    plt.pie(cont,autopct = '%1.f%%')
    leg.legend(loc='lower left',bbox_to_anchor=(-0.1, -0.1),fancybox=True, shadow=True)
    plt.title('Faixa Etária')
    plt.savefig('C:\Gerador_de_Graficos\graficos\img\gIdade.png')
    plt.close(fig)
    
    cont = [est_civil['solteiro'],est_civil['casado'],est_civil['outro'],invalido]
    lb = ['Solteiro','Casado','Outro','Registros inválidos']
    fig = plt.figure(1,figsize=(9,9))
    leg = plt.subplot(111)
    i = 0
    for l in lb:
        leg.plot(i,label=l)
        i+=1
    plt.pie(cont,autopct = '%1.f%%')
    leg.legend(loc='lower left',bbox_to_anchor=(-0.1, -0.1),fancybox=True, shadow=True)
    plt.title('Estado Civil')
    plt.savefig('C:\Gerador_de_Graficos\graficos\img\gEstCivil.png')
    plt.close(fig)

    cont = [filhos['nao'],filhos['sim'],invalido]
    lb = ['Não','Sim','Registros inválidos']
    fig = plt.figure(1,figsize=(9,9))
    leg = plt.subplot(111)
    i = 0
    for l in lb:
        leg.plot(i,label=l)
        i+=1
    plt.pie(cont,autopct = '%1.f%%')
    leg.legend(loc='lower left',bbox_to_anchor=(-0.1, -0.1),fancybox=True, shadow=True)
    plt.title('Filhos')
    plt.savefig('C:\Gerador_de_Graficos\graficos\img\gFilhos.png')
    plt.close(fig)
    
    cont = [escolaridade['integral_EPU'],escolaridade['maior_EPU'],escolaridade['integral_EPA'],escolaridade['maior_EPA'],invalido]
    lb = ['Integralmente em Escola Pública','Maior parte em Escola Pública','Integralmente em Escola Particular','Maior parte em Escola Particular','Registros inválidos']
    fig = plt.figure(1,figsize=(9,9))
    leg = plt.subplot(111)
    i = 0
    for l in lb:
        leg.plot(i,label=l)
        i+=1
    plt.pie(cont,autopct = '%1.f%%')
    leg.legend(loc='lower left',bbox_to_anchor=(-0.1, -0.1),fancybox=True, shadow=True)
    plt.title('Escolaridade')
    plt.savefig('C:\Gerador_de_Graficos\graficos\img\gEscolaridade.png')
    plt.close(fig)

    cont = [cd_origem['franca'],cd_origem['regiao'],invalido]
    lb = ['Franca','Região de Franca','Registros inválidos']
    fig = plt.figure(1,figsize=(9,9))
    leg = plt.subplot(111)
    i = 0
    for l in lb:
        leg.plot(i,label=l)
        i+=1
    plt.pie(cont,autopct = '%1.f%%')
    leg.legend(loc='lower left',bbox_to_anchor=(-0.1, -0.1),fancybox=True, shadow=True)
    plt.title('Cidade de origem')
    plt.savefig('C:\Gerador_de_Graficos\graficos\img\gCidorigem.png')
    plt.close(fig)

    cont = [moradia['proprio'],moradia['financiado'],moradia['alugado'],invalido]
    lb = ['Próprio','Financiado','Alugado','Registros inválidos']
    fig = plt.figure(1,figsize=(9,9))
    leg = plt.subplot(111)
    i = 0
    for l in lb:
        leg.plot(i,label=l)
        i+=1
    plt.pie(cont,autopct = '%1.f%%')
    leg.legend(loc='lower left',bbox_to_anchor=(-0.1, -0.1),fancybox=True, shadow=True)
    plt.title('Situação Domiciliar')
    plt.savefig('C:\Gerador_de_Graficos\graficos\img\gMoradia.png')
    plt.close(fig)

    cont = [locomocao['moto'],locomocao['onibus'],locomocao['carro'],locomocao['bicicleta'],locomocao['andando'],invalido]
    lb = ['Moto','Ônibus','Carro','Bicicleta','Andando','Registros inválidos']
    fig = plt.figure(1,figsize=(9,9))
    leg = plt.subplot(111)
    i = 0
    for l in lb:
        leg.plot(i,label=l)
        i+=1
    plt.pie(cont,autopct = '%1.f%%')
    leg.legend(loc='lower left',bbox_to_anchor=(-0.1, -0.1),fancybox=True, shadow=True)
    plt.title('Locomoção')
    plt.savefig('C:\Gerador_de_Graficos\graficos\img\gLocomocao.png')
    plt.close(fig)

    cont = [renda['1'],renda['2'],renda['3'],renda['4ou+'],invalido]
    lb = ['1 Renda','2 Rendas','3 Rendas','4 Rendas ou mais','Registros inválidos']
    fig = plt.figure(1,figsize=(9,9))
    leg = plt.subplot(111)
    i = 0
    for l in lb:
        leg.plot(i,label=l)
        i+=1
    plt.pie(cont,autopct = '%1.f%%')
    leg.legend(loc='lower left',bbox_to_anchor=(-0.1, -0.1),fancybox=True, shadow=True)
    plt.title('Renda Familiar')
    plt.savefig('C:\Gerador_de_Graficos\graficos\img\gRenda.png')
    plt.close(fig)

    cont = [trabalha['nao'],trabalha['nao_na_area'],trabalha['sim_area'],trabalha['sim_fora'],trabalha['nao_ja_area'],invalido]
    lb = ['Nunca trabalhou','Não Trabalha e nunca trabalhou na área do curso.','Trabalha na área do curso','Trabalha fora da área do curso','Não trabalha, mas já trabalhou na área do curso.','Registros inválidos']
    fig = plt.figure(1,figsize=(9,9))
    leg = plt.subplot(111)
    i = 0
    for l in lb:
        leg.plot(i,label=l)
        i+=1
    plt.pie(cont,autopct = '%1.f%%')
    leg.legend(loc='lower left',bbox_to_anchor=(-0.1, -0.1),fancybox=True, shadow=True)
    plt.title('Condições de Trabalho')
    plt.savefig('C:\Gerador_de_Graficos\graficos\img\gCondTrab.png')
    plt.close(fig)
    
    cont = [periodo_trab['tarde'],periodo_trab['noite'],periodo_trab['tarde_noite'],periodo_trab['manha'],periodo_trab['manha_tarde'],invalido]
    lb = ['Tarde','Noite','Tarde e Noite','Manhã','Manhã e Tarde','Registros inválidos']
    fig = plt.figure(1,figsize=(9,9))
    leg = plt.subplot(111)
    i = 0
    for l in lb:
        leg.plot(i,label=l)
        i+=1
    plt.pie(cont,autopct = '%1.f%%')
    leg.legend(loc='lower left',bbox_to_anchor=(-0.1, -0.1),fancybox=True, shadow=True)
    plt.title('Horário de Trabalho')
    plt.savefig('C:\Gerador_de_Graficos\graficos\img\gHorarioTrab.png')
    plt.close(fig)

    cont = [mora['familia'],mora['sozinho'],mora['republica'],invalido]
    lb = ['Família','Sozinho','República','Registros inválidos']
    fig = plt.figure(1,figsize=(9,9))
    leg = plt.subplot(111)
    i = 0
    for l in lb:
        leg.plot(i,label=l)
        i+=1
    plt.pie(cont,autopct = '%1.f%%')
    leg.legend(loc='lower left',bbox_to_anchor=(-0.1, -0.1),fancybox=True, shadow=True)
    plt.title('Com quem mora')
    plt.savefig('C:\Gerador_de_Graficos\graficos\img\gComQuemMora.png')
    plt.close(fig)

    cont = [compFamiliar['1'],compFamiliar['2'],compFamiliar['3'],compFamiliar['4+'],invalido]
    lb = ['1','2','3','4 ou mais','Registros inválidos']
    fig = plt.figure(1,figsize=(9,9))
    leg = plt.subplot(111)
    i = 0
    for l in lb:
        leg.plot(i,label=l)
        i+=1
    plt.pie(cont,autopct = '%1.f%%')
    leg.legend(loc='lower left',bbox_to_anchor=(-0.1, -0.1),fancybox=True, shadow=True)
    plt.title('Composição familiar')
    plt.savefig('C:\Gerador_de_Graficos\graficos\img\gCompFamiliar.png')
    plt.close(fig)

    cont = [ativRemunerada['1'],ativRemunerada['2'],ativRemunerada['3'],ativRemunerada['4+'],invalido]
    lb = ['1','2','3','4 ou mais','Registros inválidos']
    fig = plt.figure(1,figsize=(9,9))
    leg = plt.subplot(111)
    i = 0
    for l in lb:
        leg.plot(i,label=l)
        i+=1
    plt.pie(cont,autopct = '%1.f%%')
    leg.legend(loc='lower left',bbox_to_anchor=(-0.1, -0.1),fancybox=True, shadow=True)
    plt.title('Atividade remunerada familiar')
    plt.savefig('C:\Gerador_de_Graficos\graficos\img\gAtivRemunerada.png')
    plt.close(fig)

    cont = [info['basico'],info['medio'],info['avancado'],invalido]
    lb = ['Básico','Intermediário','Avançado','Registros inválidos']
    fig = plt.figure(1,figsize=(9,9))
    leg = plt.subplot(111)
    i = 0
    for l in lb:
        leg.plot(i,label=l)
        i+=1
    plt.pie(cont,autopct = '%1.f%%')
    leg.legend(loc='lower left',bbox_to_anchor=(-0.1, -0.1),fancybox=True, shadow=True)
    plt.title('Conhecimento em Informática')
    plt.savefig('C:\Gerador_de_Graficos\graficos\img\gInfo.png')
    plt.close(fig)

    cont = [idioma['nao'],idioma['ingles'],idioma['espanhol'],idioma['outros'],idioma['ing-esp'],invalido]
    lb = ['Não tem conhecimento','Inglês','Espanhol','Outros','Inglês e Espanhol','Registros inválidos']
    fig = plt.figure(1,figsize=(9,9))
    leg = plt.subplot(111)
    i = 0
    for l in lb:
        leg.plot(i,label=l)
        i+=1
    plt.pie(cont,autopct = '%1.f%%')
    leg.legend(loc='lower left',bbox_to_anchor=(-0.1, -0.1),fancybox=True, shadow=True)
    plt.title('Lingua Estrageira')
    plt.savefig('C:\Gerador_de_Graficos\graficos\img\gIdioma.png')
    plt.close(fig)

    cont = [deficiencia['sim'],deficiencia['nao'],invalido]
    lb = ['Sim','Não','Registros inválidos']
    fig = plt.figure(1,figsize=(9,9))
    leg = plt.subplot(111)
    i = 0
    for l in lb:
        leg.plot(i,label=l)
        i+=1
    plt.pie(cont,autopct = '%1.f%%')
    leg.legend(loc='lower left',bbox_to_anchor=(-0.1, -0.1),fancybox=True, shadow=True)
    plt.title('Deficiência')
    plt.savefig('C:\Gerador_de_Graficos\graficos\img\gDefi.png')
    plt.close(fig)


def gerar_html():
    html= '''
<!DOCTYPE html> 
<head> 
    <meta charset="utf-8" />
    <title>Gráficos da Pesquisa Socioeconômica </title>

    <script>
        var slideIndex = 0;
        showDivs(slideIndex);

        function plusDivs(n) {
            showDivs(slideIndex += n);
        }

        function currentDiv(n) {
            showDivs(slideIndex = n);
        }

        function showDivs(n) {
            var i;
            var x = document.getElementsByClassName("mySlides");
            var dots = document.getElementsByClassName("demo");
            if (n > x.length) {
                slideIndex = 1
            }
            if (n < 1) {
                slideIndex = x.length
            }
            for (i = 0; i < x.length; i++) {
                x[i].style.display = "none";  
            }
            for (i = 0; i < dots.length; i++) {
                dots[i].className = dots[i].className.replace(" w3-white", "");
            }
            x[slideIndex-1].style.display = "block";  
            dots[slideIndex-1].className += " w3-white";
        }
    </script>

</head>
<body>
    
    <header id="cabecalho" >
            <br />
            <h1> Gráficos da Pesquisa Socioeconômica</h1>
            <br />
    </header> 
    <section>
        <article>
            <table align="center">     
                <tr> 
                    <td>
                        <div class="anterior" onclick="plusDivs(-1)" > <h4>&#10094; Anterior</h4>  
                        </div>
                    </td>
                    <td height="750px" width="750px">
                        <img class="mySlides" src="img\gIdade.png" >
                        <img class="mySlides" src="img\gEstCivil.png" >
                        <img class="mySlides" src="img\gFilhos.png" >
                        <img class="mySlides" src="img\gCidOrigem.png" >
                        <img class="mySlides" src="img\gLocomocao.png" >
                        <img class="mySlides" src="img\gMoradia.png" >
                        <img class="mySlides" src="img\gComQuemMora.png" >
                        <img class="mySlides" src="img\gCompFamiliar.png" >
                        <img class="mySlides" src="img\gAtivRemunerada.png" >
                        <img class="mySlides" src="img\gRenda.png" >
                        <img class="mySlides" src="img\gCondTrab.png" >
                        <img class="mySlides" src="img\gHorarioTrab.png" >
                        <img class="mySlides" src="img\gEscolaridade.png" >
                        <img class="mySlides" src="img\gInfo.png" >
                        <img class="mySlides" src="img\gIdioma.png" >
                        <img class="mySlides" src="img\gDefi.png" >
                    </td>
                    <td>
                        <div class="proximo" onclick="plusDivs(1)"> <h4>Próximo &#10095;</h4> 
                        </div>
                    </td>
                </tr>
            </table> 
        </article>
    </section>
    
    <footer id="rodape" >
        <br />
            <h3>
                Análise e Desenvolvimento de Sistemas <br />
                2º Ciclo Noturno - Sistemas de Informação <br /><br />
                Professor:  <br />
                Carlos Eduardo de França Roland <br /><br />
                Alunos:<br />
                Bruno Oliveira e Oliveira <br />
                Douglas Rodrigues Trevizoni <br />              
                Evaldo Sebastião Lucas <br />
                Fúlvio Belato de Freitas Barichello <br />
                Gabriel Antônio Ribeiro <br />
            </h3>
        <br />
    </footer>

    <style>
        h1 {
            color: #FFFFFF;
            font-family: Tahoma;
            font-weight: 100;
        }
        h2 {
            color: #FFFFFF;
            font-family: Tahoma; 
        }
        h3 {
            color: #FFFFFF;
            font-family: Tahoma;
            font-weight: 100;
            text-align: center;
            font-size: 15px;
        }
        h4 {
            font-family: Tahoma;
            font-weight: 700;
            color: #000;
        }
        #cabecalho {
            background-color: #2E8B57;
            text-align: center;
        }
        #rodape {
            background-color: #2E8B57;
        }
        .mySlides {
            display: none;
            width: 750px;
        } 
        .anterior, .proximo {
            cursor: pointer;
        }
    </style>
</body>
'''
    end = 'C:\Gerador_de_Graficos\graficos\Gráficos.html'
    with open(end,'w', encoding='utf8') as ht:
        ht.write(html)
        webbrowser.open_new_tab(end)
        
main()

