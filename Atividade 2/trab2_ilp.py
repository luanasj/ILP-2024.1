import re 
#importa a biblioteca padrão para RegEx
import random 
#importa biblioteca padrão para gerar números aleatórios

linesQt = int(input()) #recebe o número de linhas
inputLines = '' #inicia a string que receberá todas as linhas inseridas

def arrSort(arr):
    array = arr[:]
#Função para ordenação de arrays
    for j in range(len(array)):
        for i in range(j+1,len(array)):
            if array[i] < array[j]:
                array[j],array[i] = array[i],array[j]
    return array

def removeRepeatedItems(arr):
#Função para remover repetições de itens nos arrays
    array = arr[:]
    for i in range(len(array)):
        indexArr = []
        for j in range(i+1,len(array)):
            if array[i] == array[j]:
                indexArr.insert(0,j)
        for b in indexArr:
            array.pop(b)       
    return array

def printListItems(Array):
#Imprime todos os itens de uma lista.
    if not Array:
        return print('lista vazia')
    for word in Array:
        print(word)

def sequentialSearch(array,word):
#Faz busca sequencial em listas
    for i in range(len(array)):
        if array[i] == word:
            return print('palavra existente',i+1)
    print(f"palavra não existente {len(array)}")
    # word = input()
    # exists = False
    # i = 0
    # while ((not exists) and i<len(array)):
    #     if array[i] == word:
    #         exists = True
    #     i+=1
    # if exists:
    #     print(f"palavra existente {i}")
    # else:
    #     print("palavra nao existente")

def customSearch(array,word,operator):
#Algoritmo para busca binaria e com meio aleatório
    i=0
    f=len(array)-1
    exists = False
    j = 0
    def m(a,b) : return ((a+b)//2 if operator == "b" else random.randint(a,b)) #possible to use math.floor(m)
    #retorna o valor para o meio
    #caso operator = "b", retorna o meio para busca binaria comum
    #caso operator != "b", retorna o meio aleatorio no intervalo
    while((i <= f) and (not exists)):
        print(f'i: {i} f:{f} m:{m(i,f)}')
        if word < array[m(i,f)]:
            f = m(i,f)-1
        elif word > array[m(i,f)]:
            i = m(i,f)+1
        else:
            exists = True
        j+=1
    if(exists):
        print(f'palavra existente {j}')
    else:
        print(f'palavra nao existente {j}')
    

def opSelection(unorderedWordsArray,orderedWordsArray): 
#Função responsável pela chamada das operações
    opId = input()

    while opId != 'e':
        match opId:
            case 'n':
                printListItems(unorderedWordsArray)
            case 'o':
                printListItems(orderedWordsArray)
            case 's':
                match input():
                    case 'n':
                        sequentialSearch(unorderedWordsArray,input())
                    case 'o':
                        sequentialSearch(orderedWordsArray,input())    
            case 'b':
                customSearch(orderedWordsArray,input(),"b")
            case 'r':
                customSearch(orderedWordsArray,input(),"r")
        opId = input()
        # if opId == 'n':
        #     printListItems(unorderedWordsArray)
        # elif opId == 'o':
        #     printListItems(orderedWordsArray)
        # elif opId == 's':
        #     match input():
        #         case 'n':
        #             sequentialSearch(unorderedWordsArray,input())
        #         case 'o':
        #             sequentialSearch(orderedWordsArray,input())    
        # elif opId == 'b':
        #     customSearch(orderedWordsArray,input(),"b")
        # elif opId == 'r':
        #     customSearch(orderedWordsArray,input(),"r")
        # opId = input()
    return



#Solicita e recebe as linhas de texto na entrada
for i in range(linesQt):
    inputLines += f'{input()} '

words = removeRepeatedItems(re.findall(r'\b\w+\b', inputLines))
#Transformação das linhas inseridas em um array de palavras 
#re.findall(r'\b\w+\b', inputLines): método python que retorna array de palavras através da RegEx r'\b\w+\b'

opSelection(words,arrSort(words))
#Chamada da função de seleção das operações



