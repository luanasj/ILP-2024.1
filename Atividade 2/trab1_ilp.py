import re # importa a biblioteca python para RegEx


linesQt = int(input()) #recebe o número de linhas
inputLines = '' #inicia a string que receberá todas as linhas inseridas

#Função para ordenação de arrays
def arrSort(arr):
    for j in range(len(arr)):
        for i in range(j+1,len(arr)):
            if arr[i] < arr[j]:
                arr[j],arr[i] = arr[i],arr[j]
    return arr

#Função para remover repetições de itens nos arrays
def removeRepeatedItems(arr):
    for i in range(len(arr)):
        indexArr = []
        for j in range(i+1,len(arr)):
            if arr[i] == arr[j]:
                indexArr.insert(0,j)
        for b in indexArr:
            arr.pop(b)       
    return arr

#Função correspondente à operação: 1. lista palavras por tamanho (número de letras) 
def firstOp(arr):
    size = int(input())
    matchingWords = []
    for item in arr:
        if len(item) == size:
            matchingWords.append(item)
    if matchingWords:
        for word in removeRepeatedItems(arrSort(matchingWords)):
            print(word)
    else:
        return

#Função correspondente à operação: 2. lista palavras que começam com uma determinada letra 
def seconrOp(arr):
    letter = input()
    matchingWords = []
    for item in arr:
        if item[0] == letter:
            matchingWords.append(item)
    if matchingWords: 
        for word in removeRepeatedItems(arrSort(matchingWords)):
            print(word)
    else:
        return

#Função correspondente à operação: 3. lista todas as palavras
def thirdOp(arr):
    for word in removeRepeatedItems(arrSort(arr)):
        print(word)

#Função correspondente à operação: 4. número de vezes em que uma palavra ocorre
def fourthOp(arr):
    word = input()
    i = 0
    for item in arr:
        if item == word:
            i+=1
    print(f'{word} {i}')

#Função correspondente à operação: 5. número de caracteres que não são letras nem espaços
def fifthOp(arr):
    print(len(arr))

#Função correspondente à operação: 6. listagem de caracteres que não são letras nem espaços
def sixthOp(arr):
    for symbol in removeRepeatedItems(arr):
        print(symbol)

#Função responsável pela chamada das operaçõee
def opSelection(words,caracters): #recebe como parâmetros um array de palavras e um array de caracteres e digitos 
    opId = input()

    while opId != 'e':
        if opId == 'x':
            firstOp(words)
        elif opId == 'l':
            seconrOp(words)
        elif opId == 'a':
            thirdOp(words)
        elif opId == 'n':
            fourthOp(words)
        elif opId == 's':
            fifthOp(caracters)
        elif opId == 'z':
            sixthOp(caracters)
        opId = input()

    return



#Solicita e revebe as linhas de texto na entrada
for i in range(linesQt):
    inputLines += f'{input()} '


#Chamada da função de seleção das operações
opSelection(re.findall(r'\b\w+\b', inputLines),re.findall(r'[\\,.?!()0-9]', inputLines))

#re.findall(r'\b\w+\b', inputLines): método python que retorna array de palavras através da RegEx r'\b\w+\b'
#re.findall(r'[\\,.?!()0-9]', inputLines): método python que retorna array de caracreres especiais permitidos e digitos através da RegEx r'[\\,.?!()0-9]'
