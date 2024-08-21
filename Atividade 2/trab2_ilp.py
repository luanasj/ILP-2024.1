import re #importa a biblioteca python para RegEx
import random #importa biblioteca python para gerar números aleatórios

linesQt = int(input()) #recebe o número de linhas
inputLines = '' #inicia a string que receberá todas as linhas inseridas

#Função para ordenação de arrays
def arrSort(arr):
    for j in range(len(arr)):
        for i in range(j+1,len(arr)):
            if arr[i] < arr[j]:
                arr[j],arr[i] = arr[i],arr[j]
    return arr

#Imprime todos os itens da lista(ordenada ou não ordenada).
def firstOp(Array):
    if len(Array) == 0:
        return print('lista vazia')
    for word in Array:
        print(word)

#Faz busca sequencial em listas
def secondOp(array):
    word = input()
    exists = False
    i = 0
    while ((not exists) and i<len(array)):
        if array[i] == word:
            exists = True
        i+=1
    if exists:
        print("palavra existente")
    else:
        print("palavra nao existente")
    print(i)

#Algoritmo para busca binaria
def thirdOp(array,word,exp):
    i=0
    f=len(array)-1
    exists = False
    j = 0
    #retorna o velor para o meio
    #caso exp = "b", retorna o meio para busca binaria comum
    #caso exp != "b", retorna o meio aleatorio no intervalo
    def m(a,b) : return ((a+b)//2 if exp == "b" else random.randint(a,b)) #possible to use math.floor(m)
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
    

#Função responsável pela chamada das operações
#recebe como parâmetros um array de palavras ordenadas e um array de palavras não ordenadas
def opSelection(unorderedWords,orderedWords): 
    opId = input()

    while opId != 'e':
        if opId == 'n':
            firstOp(unorderedWords)
        elif opId == 'o':
            firstOp(orderedWords)
        elif opId == 's':
            match input():
                case 'n':
                    secondOp(unorderedWords)
                case 'o':
                    secondOp(orderedWords)    
        elif opId == 'b':
            thirdOp(orderedWords,input(),"b")
        elif opId == 'r':
            thirdOp(orderedWords,input(),"r")
        opId = input()

    return



#Solicita e revebe as linhas de texto na entrada
for i in range(linesQt):
    inputLines += f'{input()} '

#Chamada da função de seleção das operações
opSelection(re.findall(r'\b\w+\b', inputLines),arrSort(re.findall(r'\b\w+\b', inputLines)))

#re.findall(r'\b\w+\b', inputLines): método python que retorna array de palavras através da RegEx r'\b\w+\b'

