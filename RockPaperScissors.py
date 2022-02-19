# coded by loh1na
from random import *



def game ():
  
      print ("wellcome to RockPaperScissors made by loh1na")
      print ("type a rock Or paper Or scissors")
        #game logic
      while True:
        player1 = input("player1:")
        player2 = randint(1, 3)
        #lose
        if player1 == 'rock' and player2 == 2:
            print ("player2 is choosing paper\nplayer2 wins")
        elif player1 == 'paper' and player2 == 3:
            print ("player2 is choosing scissors\nplayer2 wins")
        elif player1 == 'scissors' and player2 == 1:
            print ("player2 is choosing rock\nplayer2 wins")
        #win
        elif player1 == 'rock' and player2 == 3:
            print ("player2 is choosing scissors\nplayer1 wins")
        elif player1 == 'paper' and player2 == 1:
            print ("player2 is choosing rock\nplayer1 wins")
        elif player1 == 'scissors' and player2 == 2:
            print ("player2 is choosing paper\nplayer1 wins")
        else:
            print ("tie")


if __name__ == '__main__':
    game()