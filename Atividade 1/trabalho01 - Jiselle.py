# Univerdade Federal da Bahia
     # Aluna Jiselle Marques dos Santos
     # Matricula:224119999
     # MATA37            #Turma 04 
     # Primeira atividade pratica avaliativa


import re

def validar_texto(texto):
    
    # Aqui o texto do usuario vai ser validado em tres criterios; comprimento do texto e formatacao maiuculas das letras e caracteres invalidos 
    
    def contem_invalidacoes(t):
        
        return bool(re.search(r'[áéíóúÁÉÍÓÚç]', t))
        
    #Funcao para definir caracteres invalidos.
    # A funcao vai definir um padrão para caracteres invalidos que nesse caso sao os acentos e a cedilha.
    
    # while True:
        
        
    if len(texto) > 50:
        print("O texto excede o limite de 50 caracteres. Por favor, digite novamente:")
        texto = input()
        # continue : não precisa do continue

        #Limita o texto a cinquenta 50 caracteres por linha.

    if any(char.isupper() for char in texto):
        print("O texto não pode conter letras maiúsculas. Por favor, tente digitar novamente:")
        texto = input()
        # continue
        
    #Limita o text9, invalindando caracteres maiuculos.
    #Analisa o texto e verifica se ha alguma letra maiuscula, caso havendo pede para o usuario digitar novamente.

    if contem_invalidacoes(texto):
        print("O texto contém caracteres invalidos (acentos e cedilha). Por favor, digite novamente:")
        texto = input()
        # continue

    #Limita o texto, invalidando cedilha e pontuacoes.
    # Verifica mais uma vez o texto do usuario mas dessa vez tendo em foco a cedilha e as acentuacoes, fazendo com que o usurio digite novamente caso haja alguma 


    # Se todas as condições forem atendidas dai do loop e retorna ao texto do usuario
    # break

    return texto





def listar_tamanho(texto, tamanho):
    
    #Funcao para listar palavras no texto que tem o comprimento especificado.
    
    texto_sem_pontuacao = re.sub(r'[^\w\s]', '', texto)
    palavras = texto_sem_pontuacao.split()
    palavras_tamanho = {p for p in palavras if len(p) == tamanho}
    
    #Eu usei a expressao regular re.sub para poder retirar todas as pontuacoes do texto mantendo aoenas letras, numeros e espacos.
    
    return sorted(palavras_tamanho)


def palavras_comecando(texto, letra):
    
    #Funcao para listar palavras que iniciem com a letra especificada.
    
    palavras = texto.split()
    palavras_com_letra = {p for p in palavras if p.lower().startswith(letra.lower())}
    
    return sorted(palavras_com_letra)

def listar_todas_palavras(texto):
    
    #Funcao para listar todas as palavras do texto.
    # E caso haja duplicadas imprimir apenas uma delas.
    
    texto_sem_pontuacao = re.sub(r'[^\w\s]', '', texto)
    palavras = texto_sem_pontuacao.split()
    palavras_unicas = sorted(set(palavras))
    
    #utilizei o "sorted(set())" sabendo que a funcao set nao aceita elementos duplicados, nessa funcao assim os removendo e ordenando seu valor com sorted.
    
    return "\n".join(palavras_unicas)


def contar_ocorrencias(texto, palavra):
    
    #Funcao para contar o numero de ocorrencias, quantas vezes se repete de cada palavra no texto.
    
    texto_sem_pontuacao = re.sub(r'[^\w\s]', '', texto).lower()
    palavra = palavra.lower()
    ocorrencias = texto_sem_pontuacao.split().count(palavra)
    
    return f"{palavra} {ocorrencias}"

def contar_caracteres_especiais(texto):
    #Funcao para contar o numero de caracteres especial em todo o texto.
    
    caracteres_especiais = ",.()?!"
    
    return sum(1 for char in texto if char in caracteres_especiais)

def listar_caracteres_especiais(texto):
    
    #Funcao para listar todos os caracteres especiai presente no texto. 
    
    caracteres_especiais = {char for char in texto if not char.isalpha() and not char.isspace()}
    
    return sorted(caracteres_especiais, key=texto.index)
    
    #Utilizei o sorted ordenar a lista em criterio sobre a ordem em que foi digitados.

     # Solicita o texto do usuário
# num_linhas = int(input("Digite o número de linhas de texto: "))
num_linhas = int(input())
texto = [input() for _ in range(num_linhas)]
texto = ' '.join(texto)

     # Valida o texto
# texto_valido = validar_texto(texto) #não precisa validar

texto_valido = texto

comando = None #iniciando a variável antes para usar na condição do while

     #Chamada das funcoes 
while comando != 'e':
    
    comando = input().strip().lower()
    
    if comando == 'e':
        break
   
    #Encerra o loop se o comando for 'e'
    
    elif comando == 'x':
        tamanho = int(input())
        resultado = listar_tamanho(texto_valido, tamanho)
        if resultado:
            print("\n".join(resultado))
    elif comando == 'l':
        letra = input().strip()
        resultado = palavras_comecando(texto_valido, letra)
        if resultado:
            print("\n".join(resultado))
    elif comando == 'a':
        resultado = listar_todas_palavras(texto_valido)
        if resultado:
            print(resultado)
    elif comando == 'n':
        palavra = input().strip()
        print(contar_ocorrencias(texto_valido, palavra))
    elif comando == 's':
        print(contar_caracteres_especiais(texto_valido))
    elif comando == 'z':
        resultado = listar_caracteres_especiais(texto_valido)
        if resultado:
            print("\n".join(resultado))
            
        # if name == "main": main() # acredito que não se enquadra ao trabalho