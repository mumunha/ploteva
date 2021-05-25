#!/bin/bash

vdate=`date +'%d%m%Y'_'%H%M%S'`
clear
echo 'Iniciando Ploteva...'
echo -e

echo "Verificando se existem arquivos antigos..."
sleep 1

vfiles=`ls *.csv | wc | awk '{print $1}'`
echo "${vfiles} arquivos encontrados."

if [ $vfiles -ge 1 ]
then 
	vpath="data_bkp_${vdate}"
	echo "Movendo arquivos existentes para a pasta ${vpath}/"
	`mkdir "${vpath}"`
	`mv *.csv "${vpath}/"`
fi


echo -e
echo "Executando processo ploteva_R1.py para gerar arquivos: PlotsNumbers.csv e PlotsProgress.csv"
echo "Logs encontrados: "
echo -e
python3 ploteva_R1.py

echo -e
echo "Executando processo files_R1.py para gerar arquivos: PlotsFile.csv, DrivesFile.csv e TabelaGrafico.csv"
python3 files_R1.py

echo -e
echo "Fim"
echo -e
