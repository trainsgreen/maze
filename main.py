import random
#import time

#  ___ _   _ ___ _____ 
# |_ _| \ | |_ _|_   _|
#  | ||  \| || |  | |  
#  | || |\  || |  | |  
# |___|_| \_|___| |_|  
                     
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
 
s = input("size: ")
#s=21
s=int(s)
 
while (s < 9): # Input size must be greater than 9
  print ("Size must be 9 or more")
  s=input("Size: ")
  s=int(s)
 
seed=input("Seed (\"enter\" for random seed): ")
# seed=int(seed)
 
# if (seed == 0):
#   seed=random.randint(1,1000)
if (seed == ""): # Determine seed generation present
  seed=random.randint(1,1000)

#   ____                           _   _             
#  / ___| ___ _ __   ___ _ __ __ _| |_(_) ___  _ __  
# | |  _ / _ \ '_ \ / _ \ '__/ _` | __| |/ _ \| '_ \ 
# | |_| |  __/ | | |  __/ | | (_| | |_| | (_) | | | |
#  \____|\___|_| |_|\___|_|  \__,_|\__|_|\___/|_| |_|
                                                   
# Properties
i=0 # Loop counter
g=int(s/3) # Number of gaps
lst1=[] # Wall and Gap positioning within a line
ch="" # Current line staging to be dumped to bash

def nwln (l,g):
  l=int(l) # Length of line to be generated
  list.clear (lst1)
  ch="|" # Init line (Edge of map)
  k=0 # Loop counter
  j=0 # Loop counter
  while (k < 2*g-1): # While kounter is less than the number of walls plus gaps
    r1=random.randint (1,l-2) # Generate a random x-coordinate
  
    while (r1 in lst1): # Checks if random x-coordinate is already in list
      r1=random.randint (1,l-2) # Generate a random x-coordinate
      # ^WARNING 1: Gets stuck on maze under 9 because all spaces are walls or gaps.
    list.append (lst1,r1) # Adds coordinate to the list
    k=k+1 
  lst1.sort () # Sorts the coordinates to ascending order
  k=1 
  # Debugging:
  # print (lst1)
  # print (len(lst1))
  # print ("l: ",l)
  # print ("g: ",g)

  while (j < len(lst1)): 
  
    while (k != lst1[j]):
      ch=ch+"_"
      k+=1
  
    if (j/2 == round(j/2,0)):
      ch=ch+" "
    else:
      ch=ch+"႔"
#˩
    j+=1
    k+=1
  while (k <= l-2):
    ch=ch+"_"
    k+=1
  ch=ch+"|"
# print (len(ch))
  print (ch)
 
ch="_v"
while (len(ch) < s-2):
  ch=ch+"_"
ch=ch+"^_"
print (ch)
 
while (i < s/6):
# print ("i: ",i)
  nwln (s,i+3)
  i+=1
 
i-=1
 
while (i > -1):
# print ("i: ",i)
  nwln (s,i+3)
  i-=1
 
ch="|"
while (len(ch) < s-1):
  ch=ch+"_"
ch=ch+"|"
print (ch)

#  _____      _ _     _                      
# | ____|_  _(_) |_  | |    ___   ___  _ __  
# |  _| \ \/ / | __| | |   / _ \ / _ \| '_ \ 
# | |___ >  <| | |_  | |__| (_) | (_) | |_) |
# |_____/_/\_\_|\__| |_____\___/ \___/| .__/ 
#                                     |_|   
print ("seed:",seed)

