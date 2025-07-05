# CÓDIGO EM PYTHON LOGO ABAIXO DA PROPOSTA DE DESAFIO

# Desafio
Faça um programa que vai ler um numero do usuario, esse numero será o numero de linhas da saida

A saida será uma sequencia em zig zag de caracteres, onde ele vai pra direita 5 vezes, depois pra esquerda até o começo, e repetir. Por exemplo, suponha entrada 10, a saida seria

```
#
 #
  #
   #
    #
   #
  #
 #
#
```

Isso se repetirá infinitamente (teoricamente), pode usar o caracter que quiser e a linguagem que quiser

# Como participar
Basta criar um fork desse repositório e modificar seu proprio repositório. Dessa forma poderemos acompanhar vocês


numero = int(input('Quantidade de caracteres: '))

espaco = ' '

caractere = '*'
contagem = 0
contagem2 = 3

for i in range(1, numero):
  
  if contagem < 5:

    posicao = espaco*contagem + str(contagem)
    print(posicao)
    contagem += 1
  
  elif contagem == 5 and contagem2 > -1:

    posicao2 = espaco*contagem2 + str(contagem2)
    print(posicao2)
    contagem2 -= 1

  else:
 
    contagem = 1
    contagem2 = 3  
    
