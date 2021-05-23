import os
import csv
from datetime import datetime
import operator

## ALTERAR PARA LOCAL ONDE ESTAO SALVOS OS LOGS DO PLOTTER
## NORMALMENTE: C:\Users\YOUR_USER\.chia\mainnet\plotter <-- YOUR_USER: SEU USUARIO DO WINDOWS
## CHANGE TO THE PATH WHERE LOGS ARE SAVED
## USUALLY: C:\Users\YOUR_USER\.chia\mainnet\plotter <-- YOUR USER: WINDOWS USER NAME
yourpath = 'D:\logs_test2_apagar'

ideas = [
        [0, "DateTimeStart", "mid_date", 0, 62, 20, "Starting phase 1", "", "", ""]
        , [1, "TempDir", "rig_rel", 0, 48, 0, "Starting plotting progress into temporary dirs", "", "", ""]
        , [2, "Description", "",  0,  0, 0, "", "", "", ""] # calculated 
        , [3, "BufferSize", "bet_str",  0,  0, 0, "Buffer size is", "Buffer size is:", "MiB", ""]
        , [4, "PlotSize", "rig_str",  0,  0, 0, "Plot size is", "Plot size is:", "", ""]
        , [5, "Buckets", "bet_str",  0,  0, 0, "buckets", "Using", "buckets", ""]
        , [6, "Threads", "bet_str",  0,  0, 0, "threads", "Using", "threads", ""]
        , [7, "TimePh1Tbl1", "bet_str",  -1,  0, 0, "Computing table 2", "time:", "seconds", "Num"]
        , [8, "TimePh1Tbl2", "bet_str",  -1,  0, 0, "Computing table 3", "time:", "seconds", "Num"]
        , [9, "TimePh1Tbl3", "bet_str",  -1,  0, 0, "Computing table 4", "time:", "seconds", "Num"]
        , [10, "TimePh1Tbl4", "bet_str",  -1,  0, 0, "Computing table 5", "time:", "seconds", "Num"]
        , [11, "TimePh1Tbl5", "bet_str",  -1,  0, 0, "Computing table 6", "time:", "seconds", "Num"]
        , [12, "TimePh1Tbl6", "bet_str",  -1,  0, 0, "Computing table 7", "time:", "seconds", "Num"]
        , [13, "TimePh1Tbl7", "bet_str",  -1,  0, 0, "Time for phase 1", "time:", "seconds", "Num"]
        , [14, "TimePhase1", "bet_str",  0,  0, 0, "Time for phase 1", "phase 1 =", "seconds", "Num"]
        , [15, "TimePh2Tbl7", "bet_str",  -1,  0, 0, "sorting table 7", "time =", "seconds", "Num"]
        , [16, "TimePh2Tbl6a", "bet_str",  -1,  0, 0, "sorting table 6", "time =", "seconds", "Num"]
        , [17, "TimePh2Tbl6b", "bet_str",  -1,  0, 0, "Backpropagating on table 5", "time =", "seconds", "Num"]  
        , [18, "TimePh2Tbl5a", "bet_str",  -1,  0, 0, "sorting table 5", "time =", "seconds", "Num"]  
        , [19, "TimePh2Tbl5b", "bet_str",  -1,  0, 0, "Backpropagating on table 4", "time =", "seconds", "Num"]  
        , [20, "TimePh2Tbl4a", "bet_str",  -1,  0, 0, "sorting table 4", "time =", "seconds", "Num"]  
        , [21, "TimePh2Tbl4b", "bet_str",  -1,  0, 0, "Backpropagating on table 3", "time =", "seconds", "Num"]  
        , [22, "TimePh2Tbl3a", "bet_str",  -1,  0, 0, "sorting table 3", "time =", "seconds", "Num"]  
        , [23, "TimePh2Tbl3b", "bet_str",  -1,  0, 0, "Backpropagating on table 2", "time =", "seconds", "Num"]  
        , [24, "TimePh2Tbl2a", "bet_str",  -1,  0, 0, "sorting table 2", "time =", "seconds", "Num"]  
        , [25, "TimePh2Tbl2b", "bet_str",  -1,  0, 0, "table 1 new size", "time =", "seconds", "Num"] 
        , [26, "TimePh2Tbl1", "",  0,  0, 0, "", "", "", ""] # calculated 
        , [27, "TimePhase2", "bet_str",  0,  0, 0, "Time for phase 2", "phase 2 =", "seconds", "Num"] 
        , [28, "TimePh3Tbl1-2", "bet_str",  -1,  0, 0, "Compressing tables 2 and 3", "time:", "seconds", "Num"] 
        , [29, "TimePh3Tbl2-3", "bet_str",  -1,  0, 0, "Compressing tables 3 and 4", "time:", "seconds", "Num"] 
        , [30, "TimePh3Tbl3-4", "bet_str",  -1,  0, 0, "Compressing tables 4 and 5", "time:", "seconds", "Num"] 
        , [31, "TimePh3Tbl4-5", "bet_str",  -1,  0, 0, "Compressing tables 5 and 6", "time:", "seconds", "Num"] 
        , [32, "TimePh3Tbl5-6", "bet_str",  -1,  0, 0, "Compressing tables 6 and 7", "time:", "seconds", "Num"] 
        , [33, "TimePh3Tbl6-7", "bet_str",  -1,  0, 0, "Time for phase 3", "time:", "seconds", "Num"] 
        , [34, "TimePhase3", "bet_str",  0,  0, 0, "Time for phase 3", "phase 3 =", "seconds", "Num"] 
        , [35, "TimePhase4", "bet_str",  0,  0, 0, "Time for phase 4", "phase 4 =", "seconds", "Num"] 
        , [36, "CopyTime", "bet_str",  0,  0, 0, "Copy time", "time =", "seconds", "Num"] 
        , [37, "DateTimeEnd", "mid_date2", 0, 0, 19, "Created a total of", "", "", ""]
        , [38, "PlotName", "rig_minus_x", 0, 96, 1, "Renamed final file from", "", "", ""]
        , [39, "DateTimeStart_String", "",  0,  0, 0, "", "", "", ""] # calculated 
        , [40, "SpacingTime", "",  0,  0, 0, "", "", "", ""] # calculated 
        , [41, "PlotNumber", "",  0,  0, 0, "", "", "", ""] # calculated     
            ]

general = []

field_number = 0
number_description = 1
type_search = 2
location_search = 3
ref1 = 4
ref2 = 5
search_string = 6
string_between_left = 7
string_between_right = 8
type_variable = 9

linetext = ""

print (yourpath)
for root, dirs, files in os.walk(yourpath, topdown=False):
    file_count = 0
    for name in files:
        
        general = general + [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]    
        
        print(os.path.join(root, name))
        # Using readlines()
        file1 = open(os.path.join(root, name), 'r')
        Lines = file1.readlines()
 
        count = 0
        # Strips the newline character
        for line in Lines:
            count += 1
            priorlinetext = linetext
            linetext = line.strip()
            for variables in range (len(ideas)):
                if ideas[variables][type_search] == "mid_date":
                    if ideas[variables][search_string] in linetext: 
                        temp_datetime = datetime.strptime(linetext[ideas[variables][ref1]:ideas[variables][ref1]+ideas[variables][ref2]], '%b %d %H:%M:%S %Y')
                        general[file_count][ideas[variables][field_number]] = datetime.timestamp(temp_datetime)
                        
                elif ideas[variables][type_search] == "mid_date2":
                    if ideas[variables][search_string] in linetext: 
                        general[file_count][ideas[variables][field_number]] = datetime.strptime(linetext[ideas[variables][ref1]:ideas[variables][ref1]+ideas[variables][ref2]], '%Y-%m-%dT%H:%M:%S')
                        dt = general[file_count][ideas[variables][field_number]]
                        dtt =  dt.strftime("%m/%d/%Y, %H:%M:%S")
                
                elif ideas[variables][type_search] == "rig_rel": 
                    if ideas[variables][search_string] in linetext: 
                        general[file_count][ideas[variables][field_number]] = linetext[-len(linetext)+ideas[variables][ref1]:]

                elif ideas[variables][type_search] == "rig_minus_x": 
                    if ideas[variables][search_string] in linetext: 
                        general[file_count][ideas[variables][field_number]] = (linetext[-ideas[variables][ref1]:])[:ideas[variables][ref1]-ideas[variables][ref2]]
                
                elif ideas[variables][type_search] == "bet_str":      
                    if ideas[variables][location_search] == 0:
                        text_to_extract = linetext 
                    else :
                        text_to_extract = priorlinetext
                    if ideas[variables][search_string] in linetext:
                        temp_left = (text_to_extract.find(ideas[variables][string_between_left])+len(ideas[variables][string_between_left])+1)
                        temp_right = (text_to_extract.find(ideas[variables][string_between_right]))
                        if ideas[variables][type_variable] == "Num":
                            general[file_count][ideas[variables][field_number]] = float(text_to_extract[temp_left:temp_right])
                        else :
                            general[file_count][ideas[variables][field_number]] = text_to_extract[temp_left:temp_right]
                
                elif ideas[variables][type_search] == "rig_str":      
                    if ideas[variables][search_string] in linetext:
                        temp_left = (linetext.find(ideas[variables][string_between_left])+len(ideas[variables][string_between_left])+1)
                        general[file_count][ideas[variables][field_number]] = (linetext[temp_left:])
                
        # Find Table1 Phase 2 time subtracting all from total        
        
        general[file_count][ideas[26][0]] = general[file_count][ideas[27][0]]
        for i in range (15,26):
            general[file_count][ideas[26][0]] = general[file_count][ideas[26][0]] - general[file_count][ideas[i][0]]

        # cria campo com data inicio
        temp_aa = datetime.fromtimestamp(general[file_count][ideas[0][0]])
        general[file_count][ideas[39][0]] = temp_aa.strftime("%m/%d/%y %H:%M")


        file_count = file_count + 1

general = sorted(general, key=lambda x: x[0])


# cria campo com spacing de data
date_start= [row[0] for row in general]
menor_data = (min(date_start))
for i in range (0,len(general)):
    general[i][40] = general[i][0] - menor_data

# cria campo com numero do plot
for i in range (0,len(general)):
    general[i][41] = i+1

#cria campo com descricao
for i in range (0,len(general)):
    general[i][2] = str(int((general[i][14] + general[i][27] + general[i][34] + general[i][35] + general[i][36]) / 60))+" minutes"
    
# cria tabela com numero dos plots
general_plotsnumber = []

for i in range (0,len(general)):
    general_plotsnumber = general_plotsnumber + [[0]] 
    general_plotsnumber[i][0] = general[i][41]

fields = ['PlotNumber']    
with open('PlotsNumbers.csv', 'w', newline='') as g:
      
    write = csv.writer(g)
      
    write.writerow(fields)
    write.writerows(general_plotsnumber)

 
fields = [row[1] for row in ideas]

with open('PlotsProgress.csv', 'w', newline='') as f:
      
    write = csv.writer(f)
      
    write.writerow(fields)
    write.writerows(general)