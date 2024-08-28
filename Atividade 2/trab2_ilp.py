#Author: Luana da Silva de Jesus

import re 
import random 

linesQt = int(input()) 
#recebe o número de linhas
inputLines = '' 
#inicia a string que receberá todas as linhas inseridas

def arrSort(arr):
    array = arr[:]
#Função para ordenação de arrays
    for j in range(len(array)):
        for i in range(j+1,len(array)):
            if array[i] < array[j]:
                array[j],array[i] = array[i],array[j]
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

def customSearch(array,word,operator):
#Algoritmo para busca binaria e com meio aleatório
    i=0
    f=len(array)-1
    exists = False
    j = 0
    def m(a,b) : return ((a+b)//2 if operator == "b" else random.randint(a,b)) #possible to use math.floor(m)
    #retorna o valor para o meio
    while((i <= f) and (not exists)):
        mid = m(i,f)
        print(f'i: {i} f:{f} m:{mid}')
        if word < array[mid]:
            f = mid-1
        elif word > array[mid]:
            i = mid+1
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


#Solicita e recebe as linhas de texto na entrada
for i in range(linesQt):
    inputLines += f'{input()} '

words = re.findall(r'\b\w+\b', inputLines)
#Transformação das linhas inseridas em um array de palavras 
#re.findall(r'\b\w+\b', inputLines): método python que retorna array de palavras através da RegEx r'\b\w+\b'

opSelection(words,arrSort(words))
#Chamada da função de seleção das operações



