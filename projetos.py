 # 53. Faça um algoritmo que calcule os 20 primeiros números primos, 
 # dados os tres primeiros 1,2 e 3. 

contador = 0  # o contador mostra quantos numeros
num = 1       # primos ja apareceram 

while contador < 20:

    divisor = 1
    quantidade_divisor = 0

    while divisor <= num: # laço que repete a té aparecer
                           # os 20 numero primos 
        if num % divisor == 0:
            quantidade_divisor += 1  # conta quantos divisores o 
                                     # numero possui
        divisor += 1

    if quantidade_divisor == 2 or num == 1: # verifica se a divisão deu
        print(num)                          # deu certo.
        contador += 1  # soma mais um numero

    num += 1  


print("\n trabalho de") # identificação do autor. 
print("\n Dairon Everson Barbosa")
print("\n turma 12131")
print("\n Laços de Repetição")

  

            

    




     
 













