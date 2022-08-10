def regra(strings): 
# Inicializando uma váriavel booleana,
# e identicando o tamanho das strings de entrada.
    check = True  
    tamanho = len(strings) 

    for j in range(0, tamanho):
# Variavel x sendo utilizada para armazenar letra por letra 
# da string de entrada.
        x = strings[j]
# Condição criada para a checagem acontecer apenas
# no caso de letra 'a'
        if x == 'a':
# Condição criada para evitar o erro de alcance.
            if j == tamanho -1 or j == tamanho -2:
                check = False
                return False
# Condição criada para checar se após a letra 'a', temos
# os dois b's em seguida.
            if strings[j + 1] == 'b' and strings[j + 2] == 'b':
                check = True
            else:
                check = False
                return False
    return check
# Abrir o arquivo de texto.
with open("entrada3.txt", "r") as arquivo:
# Ler o arquivo e retirar a informação do número inteiro
# que representa a quantidade de strings de entrada.
    infos = arquivo.readlines()
    inteiro = int(infos[0])
# Contador feito para limitar a quantidade de strings de entrada,
# ao número inteiro informada na primeira linha.
    contador = 1
    while inteiro >= contador:
# Extrair as strings de entrada e chamar a função onde está o algoritmo
        strings = infos[contador].strip('\n')
        funcao = regra(strings)
        contador += 1
        
        if funcao:
            print(strings,': pertence')
        else:
            print(strings, ': não pertence')
             
arquivo.close()