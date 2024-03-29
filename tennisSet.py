'''
In tennis, the winner of a set is based on how many
games each player wins. The first player to win 6 games
is declared the winner unless their opponent had 
already won 5 games, in which case the set continues
until one of the players has won 7 games.
Given two integers score1 and score2, your task
is to determine if it is possible for a tennis set
to be finished with a final score of score1 : score2.
'''
def tennisSet(score1, score2):
    if (score1 ==6 or score2==6)and (score1 <5 or score2 <5 ):
            return True
    if (score1 ==7 or score2==7)and (score1 in range(5,7) or score2 in range(5,7)):
            return True
    if (score1 >7 or score2>7) :
            return False
    if (score1 <6 or score2<6)and (score1 <6 or score2 <6):
        return False
    if (score1 ==7 and score2==7) :
        return False
    if (score1 ==6 and score2==6) :
        return False
