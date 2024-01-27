import random
def check(comp,user):
    if(comp == user):
     return 0
    if(comp == 1 and user == 0):
       return -1
    if(comp == 2 and user == 1):
       return -1
    if(comp == 0 and user == 2):
     return -1
    
    return 1
comp= random.randint(0,2)
user=int(input("0 is for Rock,1 is for Paper, 2 is for Scissor: "))

score= check(comp,user)

print("User: ",user)
print("Comp: ",comp)
if(score== user):
  print("It is a draw")
elif (score == -1):
  print("You loose")
elif(user > 2) :
  print("Invalid Input") 
else:
  print("You won")    