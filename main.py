import random
#import time
 
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
 
s = input("size: ")
#s=21
s=int(s)
 
while (s < 9):
  print ("Size must be 9 or more")
  s=input("size: ")
  s=int(s)
 
seed=input("seed (zero for random seed): ")
seed=int(seed)
 
if (seed == 0):
  seed=random.randint(1,1000)
 
i=0
g=int(s/3)
lst1=[]
ch=""
 
def nwln (l,g):
  l=int(l)
  list.clear (lst1)
  ch="|"
  k=0
  j=0
  while (k < 2*g-1):
    r1=random.randint (1,l-2)
  
    while (r1 in lst1):
      r1=random.randint (1,l-2)
  
    list.append (lst1,r1)
    k=k+1
  lst1.sort ()
  k=1
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

print ("seed:",seed)

