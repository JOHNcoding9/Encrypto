Este projeto criptografa mensagens automaticamente para você com a chave de sua escolha.

COMO FUNCIONA? 
 Insira a mensagem a ser criptografada  (ou descriptografada) no bloco de notas "mensagem.txt", execute o código Encrypto.py e selecione o método de criptografia utilizado. O resultado da sua mensagem criptografada (ou descriptografada) estará presente no bloco de notas 
 "mensagem_resultado"

 Antes de realizar as substituições de alfabeto para a criptografia, o programa trata todas as letras acentuadas ( e o Ç), substituindo suas ocorrências na mensagem por uma versão não acentuada.
     # Dicionário com as substituições de caracteres acentuados
     acentuados = {
    'Ç': 'C', 'À': 'A', 'Â': 'A', 'Ä': 'A', 'Ã': 'A', 'Å': 'A', 'Æ': 'AE',
    'É': 'E', 'È': 'E', 'Ê': 'E', 'Ë': 'E', 'Í': 'I', 'Ì': 'I', 'Î': 'I', 'Ï': 'I',
    'Ñ': 'N', 'Ó': 'O', 'Ò': 'O', 'Ô': 'O', 'Õ': 'O', 'Ö': 'O', 'Ø': 'O', 'Ú': 'U',
    'Ù': 'U', 'Û': 'U', 'Ü': 'U', 'Ý': 'Y', 'À': 'A', 'Á': 'A', 'Ã': 'A', 'Â': 'A',
    'Ä': 'A', 'Ç': 'C', 'È': 'E', 'É': 'E', 'Ê': 'E', 'Í': 'I', 'Ï': 'I', 'Ì': 'I',
    'Î': 'I', 'Ó': 'O', 'Ò': 'O', 'Ô': 'O', 'Õ': 'O', 'Ö': 'O', 'Ú': 'U', 'Ù': 'U',
    'Û': 'U', 'Ü': 'U', 'Ÿ': 'Y', 'Œ': 'OE', 'Æ': 'AE'
  }
 A primeira letra corresponde á original e a segunda é a sua substituta.
    

EXPLICANDO A CIFRA DE CÉSAR
Como esta criptografia funciona?
O princípio básico da cifra de César é o deslocamento. Para criptografar uma mensagem, basta deslocar cada letra da mensagem original por um número fixo de posições. Vamos explicar como isso acontece em dois processos: criptografar e descriptografar.

1. Criptografando com a Cifra de César
Imaginemos que você tenha o texto "HELLO" e queira criptografá-lo com um deslocamento de 3. Isso significa que cada letra da palavra será substituída pela letra que está 3 posições à frente dela no alfabeto:

H → K (H + 3)

E → H (E + 3)

L → O (L + 3)

L → O (L + 3)

O → R (O + 3)

Assim, a palavra "HELLO" se torna "KHOOR" após a criptografia com um deslocamento de 3.

2. Descriptografando com a Cifra de César
Para descriptografar a mensagem, o processo é invertido. Ou seja, para cada letra criptografada, você deve deslocá-la no sentido oposto. Então, para a palavra "KHOOR", com um deslocamento de 3:

K → H (K - 3)

H → E (H - 3)

O → L (O - 3)

O → L (O - 3)

R → O (R - 3)

Assim, a palavra "KHOOR" volta a ser "HELLO".
A cifra de César é muito simples e fácil de ser quebrada, o que a torna insegura para uso real. A principal fraqueza da cifra é o fato de ela ter apenas 25 possibilidades de deslocamento (no caso de um alfabeto de 26 letras). Ou seja, para quebrar uma cifra de César, um atacante só precisaria tentar 25 diferentes deslocamentos, o que é muito rápido.

Além disso, a cifra de César não leva em consideração a frequência das letras na língua. Por exemplo, em uma língua como o português, a letra "A" é muito mais comum do que a letra "X". Isso significa que um atacante poderia facilmente analisar o texto criptografado e deduzir qual letra corresponde a outra, usando técnicas como a análise de frequência. Em termos modernos de criptografia, a cifra de César não é segura. Embora tenha sido útil em tempos antigos, sua simplicidade faz com que seja facilmente quebrada com ferramentas computacionais
