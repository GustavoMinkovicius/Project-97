import random

chances = 0
numero = random.randint(0,9)
print('advinhe o numero de 0 a 9')
while chances < 5:
  guess = input('Qual é o numero? ')
  guess = int(guess)
  if guess == numero:
    print('Parabens você ganhou')
    break
  elif guess != numero:
    print('tente novamente')
    chances = chances +1
    
if not chances < 5:
  print('VOCÊ PERDEU. O numero é', numero) 
  