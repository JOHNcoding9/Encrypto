 # Lê o conteúdo de um arquivo de texto
try:
    with open('mensagem.txt', 'r', encoding='utf-8') as file:
     mensagem = file.read().upper()  # Lê o arquivo e prepara a mensagem
except FileNotFoundError:
     print("O arquivo 'mensagem.txt' não foi encontrado.")

def Remover_acentos(texto):
    try:

    # Dicionário com as substituições de caracteres acentuados
     acentuados = {
    'Ç': 'C', 'À': 'A', 'Â': 'A', 'Ä': 'A', 'Ã': 'A', 'Å': 'A', 'Æ': 'AE', 'Ç': 'C',
    'É': 'E', 'È': 'E', 'Ê': 'E', 'Ë': 'E', 'Í': 'I', 'Ì': 'I', 'Î': 'I', 'Ï': 'I',
    'Ñ': 'N', 'Ó': 'O', 'Ò': 'O', 'Ô': 'O', 'Õ': 'O', 'Ö': 'O', 'Ø': 'O', 'Ú': 'U',
    'Ù': 'U', 'Û': 'U', 'Ü': 'U', 'Ý': 'Y', 'À': 'A', 'Á': 'A', 'Ã': 'A', 'Â': 'A',
    'Ä': 'A', 'Ç': 'C', 'È': 'E', 'É': 'E', 'Ê': 'E', 'Í': 'I', 'Ï': 'I', 'Ì': 'I',
    'Î': 'I', 'Ó': 'O', 'Ò': 'O', 'Ô': 'O', 'Õ': 'O', 'Ö': 'O', 'Ú': 'U', 'Ù': 'U',
    'Û': 'U', 'Ü': 'U', 'Ÿ': 'Y', 'Œ': 'OE', 'Æ': 'AE'
  }
    # Substitui os caracteres acentuados com base no dicionário
     for caractere_acentuado, caractere_sem_acentos in acentuados.items():
        texto = texto.replace(caractere_acentuado, caractere_sem_acentos)
    
     return texto
    
    except Exception as e:
       print(f'Erro: {e}')

mensagem = Remover_acentos(mensagem)

espaco = str(input("Deseja manter o espaçamento entre as letras? [S/N] ")).upper()   
if espaco == "N" :
    mensagem = mensagem.replace(' ','')

def Cesar():
    #  Cifra de César
    # Simples de implementar.
    # Boa para aprendizado, mas não segura para uso real.
    # Recomendado para iniciantes.'

    try:

     resultado = ""
     alfabeto= ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
     
     while True:
      try:
       crip_ou_descript = int(input('Digite 0 para criptografar e 1 se você quer descriptografar a mensagem: '))
       if crip_ou_descript == 1 or crip_ou_descript == 0:
         break
       
      except Exception as e:
         print(f'Erro: {e}')

     deslocamento = int(input("Defina a quantidade de deslocamentos: "))  

     for letra in mensagem:

        if letra.isdigit() or letra in '.,!?=+-%@$':

            resultado += letra
            continue # skipa a iteração se for número

        if letra in alfabeto:
            posicao_alfabeto = alfabeto.index(letra)
            
            if crip_ou_descript:
             # Aplicando o deslocamento de forma circular com o operador de módulo (resto da divisão)
             nova_posicao = (posicao_alfabeto - deslocamento) % len(alfabeto)

            else:
             # Aplicando o deslocamento de forma circular com o operador de módulo (resto da divisão)
             nova_posicao = (posicao_alfabeto + deslocamento) % len(alfabeto)

            letra = alfabeto[nova_posicao]

            resultado += letra

            


        else:
            if letra == ' ':
               resultado += letra
            else:   
             print(f"invalido: {letra} (não incluido)")

     # Salvando o resultado em um arquivo de texto
     with open("mensagem_resultado.txt", "w") as file:
        file.write(resultado)  # Escreve a criptografia no arquivo de texto

     print("O resultado foi salvo no arquivo 'mensagem_resultado.txt'.")

    except Exception as e:
       print(f'Erro: {e}')



# fazer um deslocamento "circular"
# fazer as primeiras validações

Cesar()


#def Monoalfabetica():
    #Cifra de Substituição (Cifra Monoalfabética)
    #Uma variação da Cifra de César, onde as letras são substituídas por outras aleatoriamente (não apenas com um deslocamento fixo).
   #Embora mais difícil de decifrar do que a Cifra de César, ainda é vulnerável a ataques como análise de frequência.


#def AES():
   #É um algoritmo de criptografia simétrica, o que significa que a mesma chave é usada tanto para criptografar quanto para descriptografar os dados.
   #A segurança do AES depende da chave secreta compartilhada entre as partes envolvidas.
