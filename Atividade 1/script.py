import re

# texto = "Aúçana, Olú, blåbær é uma palavra com acento."
# palavras = re.findall(r'\b[\wáéíóúâêîôûãõç]+\b', texto)
# palavras1 = re.findall(r'[áéíóúâêîôûãõç]', texto)
# print(palavras)  # ['yogenfrüz']
# print(palavras1)



# forbiddenChar = re.compile(r'/\b[a-záéíóúâêîôûãõç]+\b/gi')

linesQt = int(input('Digite o número de linhas desejado: '))
inputLines = ''
wordsArr = []
caractersArr = []
operations = 'Operações: \n 1. lista palavras por tamanho (número de letras) \n 2. lista palavras que começam com uma determinada letra \n 3. lista todas as palavras \n 4. número de vezes em que uma palavra ocorre \n 5. número de caracteres que não são letras nem espaços  \n 6. listagem de caracteres que não são letras nem espaços \n 7. término da seqüência de comandos'
# print(linesQt)

# def listappend(arr, item):
#     arr.append(item)




# /\b[a-záéíóúâêîôûãõç]+\b/gi

def arrSort(arr):
    for j in range(len(arr)):
        for i in range(j+1,len(arr)):
            if arr[i] < arr[j]:
                arr[j],arr[i] = arr[i],arr[j]
    return arr

def removeRepeatedItems(arr):
    for i in range(len(arr)):
        indexArr = []
        for j in range(i+1,len(arr)):
            if arr[i] == arr[j]:
                indexArr.insert(0,j)
        for b in indexArr:
            arr.pop(b)       
    return arr



# def treatAndReturn(arr,a,b):
#     matchingWords = []
#     for item in arr:
#         if a == b:
#             matchingWords.append(item)
#     if matchingWords:
#         matchingWords = arrSort(matchingWords)
#         matchingWords = removeRepeatedItems(matchingWords)
#         for word in matchingWords:
#             print(word)
#     else:
#         return
        


# def getWordsArray(arr):
#     bigString = ''
#     for item in arr:
#         bigString += f'{item} '
#     return re.findall(r'\b[\w0-9]+\b', bigString) #remover os caracters com acento da ReGex

def firstOp(arr):
    size = int(input('Digite o tamanho(número de letras): '))
    # treatAndReturn(arr,len(item),size)
    matchingWords = []
    for item in arr:
        if len(item) == size:
            matchingWords.append(item)
    if matchingWords:
        # matchingWords = arrSort(matchingWords)
        # matchingWords = removeRepeatedItems(matchingWords) 
        for word in removeRepeatedItems(arrSort(matchingWords)):
            print(word)
    else:
        return

def seconrOp(arr):
    letter = input('Digite uma letra: ')
    matchingWords = []
    for item in arr:
        if item[0] == letter:
            matchingWords.append(item)
    if matchingWords:
        # matchingWords = arrSort(matchingWords)
        # matchingWords = removeRepeatedItems(matchingWords) 
        for word in removeRepeatedItems(arrSort(matchingWords)):
            print(word)
    else:
        return

def thirdOp(arr):
    for word in removeRepeatedItems(arrSort(arr)):
        print(word)

def fourthOp(arr):
    word = input('Digite uma palavra: ')
    i = 0
    for item in arr:
        if item == word:
            i+=1
    print(f'{word} {i}')

def fifthOp(arr):
    print(len(arr))

def sixthOp(arr):
    for symbol in removeRepeatedItems(arr):
        print(symbol)

    





while linesQt > 0:
    newLine = input('Digite uma frase: ')

    if len(newLine) > 50 or not newLine.islower():
        print('Não são permitidas letras maiúsculas ou textos com mais de 50 caracteres, tente novamente.')
    elif len(newLine) == 0:
        print('Por favor, digite algum texto.')
    elif re.findall(r'[áéíóúâêîôûãõç]', newLine):
        print('Não são permitidas letras com acento ou ç, tente novamente.')
    elif re.findall(r'[áéíóúâêîôûãõç]', newLine): #alowed special caracters: 0-9.,!?()
        print('Não são permitidas letras com acento ou ç, tente novamente.')
    else:
        inputLines += f'{newLine} '
        linesQt -= 1

# wordsArr = re.findall(r'\b[\w0-9]+\b', inputLines)  #r'\b[a-zA-Z]+\b' #r'\b\w+\d*\w+\b' #r'\b[a-zA-Z]+\d*[a-zA-Z]+\b' regex para palavras, mesmo que contenham um digito no meio 
# caractersArr = re.findall(r'[\\d,.?!()0-9]', inputLines)

wordsArr = re.findall(r'\b[\w0-9]+\b', inputLines)
caractersArr = re.findall(r'[\\d,.?!()0-9]', inputLines)
# caractersArr = 

print(wordsArr)
print(caractersArr)
fifthOp(caractersArr)
sixthOp(caractersArr)
# print(operations)
# firstOp(wordsArr)
# seconrOp(wordsArr)
# thirdOp(wordsArr)
# fourthOp(wordsArr)

# # print(wordsArr)
# print(operations)