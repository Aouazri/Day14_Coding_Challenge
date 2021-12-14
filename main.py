from game_data import data 
import random 
from art import logo, vs
from replit import clear
#print(len(data))
# so we have 50 dictionaries stored in our list
#I need a function that compares who has more followers 
#I need a function that updates score when the user is right 
# the loser between the two choices become option A 
#while the user is right, we keep playing
#I need a function to randomly chooses someone from the list
def random_choice(data):
  choice= random.choice(data)
  return choice
# ******************************* #
#function that compares who has more followers and updates the score accordingly:# 
def compare(dict1,dict2,user_answer):
  #user_answer= input("Who has more instagram followers? choose 'A' or 'B': ")
  if user_answer =='a' and dict1['follower_count']>= dict2['follower_count']:
    return score+1
  elif user_answer =='b' and dict2['follower_count']>= dict1['follower_count']:
    return score+1
  else:
    return score
# ******************************* ******************************* **********#
def answer(dict1,dict2,user_answer):
  if user_answer =='a' and dict1['follower_count']>= dict2['follower_count']:
    return True
  elif user_answer =='b' and dict2['follower_count']>= dict1['follower_count']:
    return True
  else:
    return False
# ******************************* ******************************* **********#

print(logo)
first_choice= random_choice(data)
second_choice= random_choice(data)
score= 0
should_continue=True
#while will be here
while should_continue==True:
  print(f"Compare A: {first_choice['name']}, {first_choice['description']}, from {first_choice['country']}")
  #VS
  print(vs)
  print(f"Against B: {second_choice['name']}, {second_choice['description']}, from {second_choice['country']}")

  user_answer= input("Who has more instagram followers? choose 'A' or 'B': ").lower()
  score= compare(first_choice,second_choice,user_answer)
  should_continue=answer(first_choice,second_choice,user_answer)
  if should_continue==True:
    clear()
    print(logo)
    print(f"You're right! Current score: {score} ")
    
    #switchero magic
    first_choice= second_choice
    second_choice= random_choice(data)
    
  else:
    clear()
    print(logo)
    if score== 0:
      print(f"Final score: {score}. Are you even trying? ")
    elif score<3:
      print(f"Final score: {score}. Come on you can do better! ")
    elif score<9:
      print(f"Final score: {score}. Congrats you're better than the majority of players ")
    else:
      print(f"Final score: {score}. You're too good at this game, maybe you should spend less time in instagram ")
