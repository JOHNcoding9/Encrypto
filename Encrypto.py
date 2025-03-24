


def Cesar():
    #  Cifra de César
    # Simples de implementar.
    # Boa para aprendizado, mas não segura para uso real.
    # Recomendado para iniciantes.'

    alfabeto= ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

    deslocamento = int(input("Defina a quantidade de deslocamentos: "))

    posicao = 0
    for letra in alfabeto:
          
        armazena_letra = letra[posicao + deslocamento]
        
        letra[posicao + deslocamento] = letra[posicao] 

        letra[posicao] = armazena_letra

        posicao +=1
    
    print(alfabeto)



    #with open('mensagem.txt','r',encoding="utf-8") as arquivo:





#def Monoalfabetica():
    #Cifra de Substituição (Cifra Monoalfabética)
    #Uma variação da Cifra de César, onde as letras são substituídas por outras aleatoriamente (não apenas com um deslocamento fixo).
   #Embora mais difícil de decifrar do que a Cifra de César, ainda é vulnerável a ataques como análise de frequência.


#def AES():
   #É um algoritmo de criptografia simétrica, o que significa que a mesma chave é usada tanto para criptografar quanto para descriptografar os dados.
   #A segurança do AES depende da chave secreta compartilhada entre as partes envolvidas.

Cesar()