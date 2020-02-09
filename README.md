# Organizador dos grifos e anotações do Kindle
## O quê
 - Organizador dos grifos e anotações feitos no Kindle
 - Esses dados estão escritos no MyClippings.txt, arquivo localizado na pasta documents dentro da memória do Amazon Kindle.

## Por quê
 - A ideia era adicionar as anotações que fiz em cada livro de não-ficção que li pelo Kindle ao Zotero, e aí me deparei com um arquivo todo esquisito que não tinha regularidade entre os separadores, o que me impediu de resolver pelo Excel
 - Por isso, resolvi usar Python para organizar esses dados, usando o separador como guia

## Método
 - Ler cada linha do txt
 - Remover o último caractere, \n, de quebra de linha de cada linha
 - Criar listas com os títulos, os tipo + localização e com os textos do grifo ou anotação
 - Cada item das listas é preenchido usando o separador como guia
    - título = 1 depois do separador
    - tipo e localização = 2 depois do separador
    - texto = 1 antes do separador
 - Consertada final pra adicionar os dados que se perderam por conta dessa lógica de achar título, tipo/localização e texto
 - Escreve cada linha do csv justapondo cada elemento de cada uma das três listas, usando o caractere | como separador
 
