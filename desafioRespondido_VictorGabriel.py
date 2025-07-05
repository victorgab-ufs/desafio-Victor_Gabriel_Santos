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
