'''
You are playing an RPG game.
Currently your experience points
(XP) totalis equal to experience. 
To reach the next level your XP 
should be at least at threshold. 
If you kill the monster in front of you,
you will gain more experience points
in the amount of the reward.
'''
def reachNextLevel(experience, threshold, reward):
    amount=experience+reward
    if(amount>=threshold):
        return True
    else:
        return False
