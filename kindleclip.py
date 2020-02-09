# parsing Kindle clippings
# lendo o arquivo das anotações do Kindle

import csv

def saving_csv_lists_as_columns(somelist1,somelist2,somelist3):
    # concatenates horizontally each element in each list
    # concatena horizontalmente cada elemento em cada uma das três listas
    filename= "kindle_clippings_organizado.csv"
    with open(filename, "w", newline='', encoding='latin_1') as somefile:
        for i in range(len(somelist1)):
            somefile.write(somelist1[i])
            somefile.write("|")
            somefile.write(somelist2[i])
            somefile.write("|")
            somefile.write(somelist3[i])
            somefile.write("\n")
        
with open("My Clippings.txt", "r", encoding='latin_1') as file1:
    # reading all lines from My Clippings
    # lendo todas as linhas do My Clippings
    allLines_temp=file1.readlines()  

    # removing last character from each line, which is always a \n line break
    # removendo o último caractere de cada linha, que sempre é uma quebra de linha \n
    allLines = [x[:-1] for x in allLines_temp]

    # creating empty lists for each of the columns to-be-created
    # criando listas vazias para o que virão a ser as três colunas
    titleList=[]
    typelocList=[]
    textList=[]

    # adding the first 2 lines, a step which is necessary because the txt doesn't begin with a separator
    # adicionando as 2 primeiras linhas, etapa necessária pois o txt não começa com um separador
    titleList.append(allLines[0])
    typelocList.append(allLines[1])

    # adding each corresponding line to each of the three lists, using the separator as a guide
    # adicionando cada linha correspondente a cada uma das três listas, usando o separador como guia
    for line in range(len(allLines)):
        if '==========' in allLines[line-1]:
            titleList.append( allLines[line])

    for line in range(len(allLines)):
        if '==========' in allLines[line-2]:
            typelocList.append( allLines[line] )

    for line in range(len(allLines)):
        if '==========' in allLines[line]:
            textList.append( allLines[line-1] )

    # a fix, adding the second to last line which gets left behind because of the line-1
    # adicionando a penúltima linha que acaba não lendo lida por causa do line-1
    textList.append(allLines[-2])

    # applying the function to all the three sub-lists (to-be columns) created
    # aplicando a função para as três sub-listas (proto-colunas) criadas
    saving_csv_lists_as_columns(titleList, typelocList, textList)