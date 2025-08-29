import random
Rock = 'Rock'
Paper = 'Paper'
Scissors = 'Scissors'
Lizard = 'Lizard'
Spock = 'Spock'
computer = random.randint(1,5)
print('=====================================')
print('Rock, Paper, Scissors, Lizard, Spock!')
print('=====================================')

print('1 = Rock!')
print('2 = Paper!')
print('3 = Scissors!')
print('4 = Lizard!')
print('5 = Spock!')
print('===================================================')
player = int(input('Rock Paper Scissors Lizard or Spock?: '))
if player == 1:
    print('You Chose!' , Rock)
elif player == 2:
    print('You Chose!' , Paper)
elif player == 3:
    print('You Chose!' , Scissors)
elif player == 4:
    print('You Chose!' , Lizard)
elif player == 5:
    print('You Chose!' , Spock)
else:
    print('Please Enter a Valid Number.')

if computer == 1:
    print('CPU Chose!' , Rock)
elif computer == 2:
    print('CPU Chose!' , Paper)
elif computer == 3:
    print('CPU Chose!' , Scissors)
elif computer == 4:
    print('CPU Chose' , Lizard)
elif computer == 5:
    print('CPU Chose' , Spock)
else:
    print('Error')

print('===================================================')
if player == 1 and computer == 2:
    print('CPU Wins!')
elif player == 1 and computer == 3:
    print('Player Wins!')
elif player == 1 and computer == 4:
    print('Player Wins!')
elif player == 1 and computer == 5:
    print('CPU Wins!')
elif player == 3 and computer == 2:
    print('Player Wins!')
elif player == 3 and computer == 1:
    print('CPU Wins!')
elif player == 3 and computer == 4:
    print('Player Wins!')
elif player == 3 and computer == 5:
    print('CPU Wins!')
elif player == 2 and computer == 1:
    print('Player Wins!')
elif player == 2 and computer == 3:
    print('CPU Wins!')
elif player == 2 and computer == 4:
    print('CPU Wins!')
elif player == 2 and computer == 5:
    print('Player Wins!')
elif player == 4 and computer == 1:
    print('CPU Wins!')
elif player == 4 and computer == 2:
    print('Player Wins!')
elif player == 4 and computer == 3:
    print('CPU Wins!')
elif player == 4 and computer == 5:
    print('Player Wins!')
elif player == 5 and computer == 1:
    print('Player Wins!')
elif player == 5 and computer == 2: 
    print('CPU Wins!')
elif player == 5 and computer == 3:
    print('Player Wins!')
elif player == 5 and computer == 4:
    print('CPU Wins!')
else:
    print('Draw!')
print('====================================================')