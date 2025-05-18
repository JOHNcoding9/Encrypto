import random
 # Lê o conteúdo de um arquivo de texto
try:
    with open('mensagem.txt', 'r', encoding='utf-8') as file:
     texto = file.read().upper()  # Lê o arquivo e prepara a mensagem
except FileNotFoundError:
     print("O arquivo 'mensagem.txt' não foi encontrado.")

# tratamento da mensagem
def Remover_acentos(texto):
    
    try:

    # Dicionário com as substituições de caracteres acentuados
     acentuados = {
    'Ç': 'C', 'À': 'A', 'Â': 'A', 'Ä': 'A', 'Ã': 'A', 'Æ': 'AE',
    'É': 'E', 'È': 'E', 'Ê': 'E', 'Ë': 'E', 'Í': 'I', 'Ì': 'I', 'Î': 'I', 'Ï': 'I',
    'Ñ': 'N', 'Ó': 'O', 'Ò': 'O', 'Ô': 'O', 'Õ': 'O', 'Ö': 'O', 'Ø': 'O', 'Ú': 'U',
    'Ù': 'U', 'Û': 'U', 'Ü': 'U', 'Ý': 'Y', 'Á': 'A','Ÿ': 'Y', 'Œ': 'OE'
  }
    # Substitui os caracteres acentuados com base no dicionário
     for caractere_acentuado, caractere_sem_acentos in acentuados.items():
        texto = texto.replace(caractere_acentuado, caractere_sem_acentos)
    
     return texto
    
    except Exception as e:
       print(f'Erro: {e}')

mensagem = Remover_acentos(texto)
while True:
 try:
  espaco = str(input("Deseja manter o espaçamento entre as letras na mensagem? [S/N] ")).upper()  
  if espaco == "N" :
   mensagem = mensagem.replace(' ','')
   break

  if espaco == "S" :
   break

 except Exception as e:
   print(f'Erro: {e}') 

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
       crip_ou_descript = int(input(' [0]: criptografar [1]:descriptografar mensagem: '))
       if crip_ou_descript == 1 or crip_ou_descript == 0:
         break
       
      except Exception as e:
         print(f'Erro: {e}')

     deslocamento = int(input("Defina a quantidade de deslocamentos: "))  

     for letra in mensagem:

        if letra.isdigit() or letra in '.,!?=+-%@$;:&()':

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

def Monoalfabetica():
 
 
#Cifra de Substituição (Cifra Monoalfabética)
#Uma variação da Cifra de César, onde as letras são substituídas por outras aleatoriamente (não apenas com um deslocamento fixo).
#Embora mais difícil de decifrar do que a Cifra de César, ainda é vulnerável a ataques como análise de frequência.

 alfabeto= ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
 letra_usada = []
 alfabeto_copia = alfabeto.copy()
 resultado = ''

 while True:
   try:
    crip_ou_descript = int(input(' [0]: criptografar [1]: descriptografar mensagem: '))
    if crip_ou_descript == 1 or crip_ou_descript == 0:
      break
      
   except Exception as e:
      print(f'Erro: {e}')


 if not crip_ou_descript: # cript_descript = False (criptografar)
  
  
   while True:
    try:
     pergunta = int(input("[0]: alfabeto de substituição aleatória  [1]: alfabeto de substituição manual: "))
     if pergunta == 1:
        
      # alfabeto de substiuiçao manual
      for i, letra in enumerate(alfabeto):
        nova_letra = str(input(f'Escreva o substituto da letra "{letra}" : ')).strip().upper()
        while nova_letra == '' or len(nova_letra) != 1 or nova_letra in letra_usada:
           print('><'*60)
           print("Inválido! a nova letra deve ser apenas UM caractere e este não pode se repetir! ")
           print('><'*60)
           nova_letra = str(input(f'Escreva o substituto da letra "{letra}" : ')).strip().upper()
          
        letra_usada.append(nova_letra)
        alfabeto[i] = nova_letra

      break
    
      # alfabeto de substiuição aleatória
     if pergunta == 0:
       # a letra nova não pode se repetir de novo no alfabeto
       for i,letra in enumerate(alfabeto):
        nova_letra = random.choice(alfabeto_copia)

        while nova_letra == letra or nova_letra in letra_usada:
          nova_letra = random.choice(alfabeto_copia)  
    
        letra_usada.append(nova_letra)
        alfabeto[i] = nova_letra
       
       break

    except Exception as e:
      print(f'Erro: {e}')
 
   print('=' *74)
   print(f'este é o seu novo alfabeto de A-Z, guarde-o para conseguir desciptografá-lo depois :)')
   print(f'Antes:  {alfabeto_copia}')
   print(f'depois: {alfabeto}')
   print("string:", ''.join(alfabeto))
   print('=' *74) 
  
   # criptografia Monoalfabética
   try:  
    for letra in mensagem:

     if letra.isdigit() or letra in '.,!?=+-%@$;:&()':
         
         resultado += letra
         continue # skipa a iteração se for número ou símbolo
   
     if letra in alfabeto_copia:
     
      posicao_alfabeto = alfabeto_copia.index(letra)

      letra = alfabeto[posicao_alfabeto]

      resultado += letra
   
     else:
       if letra == ' ':
        resultado += letra

   except Exception as e:
    print(f'Erro: {e}')


 else: # cript_descript = True (descriptografar)
   
   # Descriptografia
   try:
    while True:
     print('=' * 60)
     alfabeto = str(input('Informe o alfabeto que foi utilizado para criptografar a mensagem: ')).replace(' ','').upper()
    
     if len(alfabeto) == 26:
       alfabeto = list(alfabeto)
       break
     
     print('><' * 60)
     print(f'Erro! o alfabeto brasileiro possui 26 letras! Você forneceu {len(alfabeto)} letras!')
     print('><' * 60)
    
    for letra in mensagem:

      if letra.isdigit() or letra in '.,!?=+-%@$;:&()':
         
         resultado += letra
         continue # skipa a iteração se for número ou símbolo
   
      if letra in alfabeto:
     
       posicao_alfabeto = alfabeto.index(letra)

       letra = alfabeto_copia[posicao_alfabeto]

       resultado += letra

      else:
       if letra == ' ':
        resultado += letra

   except Exception as e:
    print(f'Erro: {e}')

 # Salvando o resultado em um arquivo de texto
 with open("mensagem_resultado.txt", "w") as file:
   file.write(resultado)  # Escreve a criptografia no arquivo de texto

 print("O resultado foi salvo no arquivo 'mensagem_resultado.txt'.")

       
     
Monoalfabetica()

# gerar letra aleatoria, conferir se a letra gerada é diferente da letra original, adicionar cada letra aleaotria para a lista novo alfabeto
# substituir cada letra da mensagem pelo novo alfabeto

#def AES():
   #É um algoritmo de criptografia simétrica, o que significa que a mesma chave é usada tanto para criptografar quanto para descriptografar os dados.
   #A segurança do AES depende da chave secreta compartilhada entre as partes envolvidas.
