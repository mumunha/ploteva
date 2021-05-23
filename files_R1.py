import glob
from datetime import datetime
import os
import shutil
import math
import csv

#
# AQUI E NECESSARIO ALTERAR SEUS DRIVES AONDE ESTAO OS PLOTS
# IMPORTANTE: APOS O ULTIMO DRIVE, NAO HA VIRGULA DEPOIS DO COLCHETE
#
# HERE YOU INSERT DRIVES WHERE YOUR PLOTS ARE LOCATED
# IMPORTANT: AFTER LAST DRIVE, THER IS NO COMMA AFTER THE BRACKET

yourdrives = [ 
                ['//MSF-SERVER/Easy/ChiaFinal', 'Easy'],
                ['Z:/ChiaFinal', 'NAS'],
                ['//MSF-SERVER/Alpha/ChiaFinalFarm', 'Alpha'],
                ['//MSF-SERVER/Beta', 'Beta'],
                ['//MUMUS_WKH/Delta/ChiaFinalFarm', 'Delta'],
                ['//MUMUS_WKH/Epsilon/ChiaFinalFarm', 'Epsilon'],
                ['//MUMUS_WKH/Gama/', 'Gama'],
                ['//MUMUS_WKH/Eta/', 'Eta'],
                ['//MUMUS_WKH/Zeta/', 'Zeta'] # NAO INCLUIR VIRGULA - DO NOT INSERT COMMA HERE
            ]

yourpaths = [row[0] for row in yourdrives]
yourpaths_names = [row[1] for row in yourdrives]

fields = ['caminho','nome_arquivo','plot_size','data_inicio','data_inicio_valor','data_inicio_curta', 'data_final', 'data_final_valor', 'data_final_curta', 'nome_drive' ]

plots_livres =[]

for cam_espaco in yourpaths:
    total, used, free = shutil.disk_usage(cam_espaco)
    drive_espaco = yourpaths_names[yourpaths.index(cam_espaco)]
    plots_livres = plots_livres + [[drive_espaco, (math.trunc((free // (2**30))/101.4))]]

print(plots_livres)
a=0
for yourpath in yourpaths:
    a = a +1
    if a==1:
        datafiles = (glob.glob(yourpath+"/*.plot"))
    else:
        datafiles =  datafiles + (glob.glob(yourpath+"/*.plot"))

dados = []
tabela_grafico = []
tabela_grafico_drives = []

for name in datafiles:
        
    inicio = name.find("plot-k")
    caminho = (name[:inicio-1])


    for name_path in yourpaths_names:
        if yourpaths[yourpaths_names.index(name_path)] == caminho:
            nome_caminho = name_path
    nome_arquivo = (name[-len(name)+inicio:])
    #nome_arquivo = 'PLOTname.plot'
    data_string = (name[inicio+9:inicio+9+16])
    data_valor = (datetime.strptime(name[inicio+9:inicio+9+16], "%Y-%m-%d-%H-%M"))
    data_string_resumida = data_valor.strftime("%Y.%m.%d")
    data_end_valor = (datetime.fromtimestamp(os.path.getmtime(name)))
    data_end_string = data_end_valor.strftime("%Y-%m-%d-%H-%M")
    data_end_string_resumido = data_end_valor.strftime("%Y.%m.%d")
    dados = dados + [[caminho, nome_arquivo, name[inicio+5:inicio+8], data_string, data_valor, data_string_resumida, data_end_string, data_end_valor, data_end_string_resumido, nome_caminho ]]

# Monta tabela dos dias

dias = [row[8] for row in dados]
dias_unicos = list(set(dias))
dias_unicos.sort()

repeticoes_acumuladas = 0
for dia_calculo in dias_unicos:
    repeticoes_dia = 0
    for linha_dados in dados:
        if dia_calculo==linha_dados[8]:
            repeticoes_dia += 1
            repeticoes_acumuladas +=1
    tabela_grafico = tabela_grafico + [[dia_calculo,repeticoes_dia,repeticoes_acumuladas]]

# Monta tabela dos drives
plots_livres_drive=1
for drive_calculo in yourpaths_names:
    plots_por_drive = 0
    for linha_dados in dados:
        if drive_calculo==linha_dados[9]:
            plots_por_drive +=1
    for pl in plots_livres:
        if drive_calculo==pl[0]:
            plots_livres_drive = (plots_livres[(plots_livres.index(pl))][1])

    tabela_grafico_drives = tabela_grafico_drives + [[drive_calculo,plots_por_drive,plots_livres_drive]]

with open('PlotsFile.csv', 'w', newline='') as f:
      
    write = csv.writer(f)
      
    write.writerow(fields)
    write.writerows(dados)


fields = ["NomeDrive", "PlotsAtuais", "PlotsLivres"]
with open('DrivesFile.csv', 'w', newline='') as g:
      
    write = csv.writer(g)
      
    write.writerow(fields)
    write.writerows(tabela_grafico_drives)

fields = ["Data", "PlotsDia", "PlotsAcum"]
with open('TabelaGrafico.csv', 'w', newline='') as h:
      
    write = csv.writer(h)
      
    write.writerow(fields)
    write.writerows(tabela_grafico)

