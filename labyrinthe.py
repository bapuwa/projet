# -*- coding: utf-8 -*-
#!/usr/bin/env python
import sys 

per_line=0
per_rows=5
perso=[per_line,per_rows]

laby=["**   8*********","*    ***   ****","***     *******","*****       ***","*             *","*****       ***","******         " ]
print(laby[per_line][per_rows-1])

print("toto")
def affiche(labyrinth):
    for i in range(len(laby)):
        print(laby[i])

def change(chaine,i,car):
   print(chaine[:i])
   s=chaine[:i]+car+chaine[i+1:]
  
   return s

quit_party='n'

try:
    while (per_line!=len(laby) or (per_rows!=15) or quit_party=='n' ):
   
    
        n=input("ou voulez vous aller:(Left = l, right = r, top = t, down = d)")
        n=n.lower()
    
    
        if (n=="l"):
        
            if laby[per_line][per_rows-1] =="*":
                print("can't move left")
            elif laby[per_line][per_rows-1] ==" ":
                laby[per_line]=change(laby[per_line],per_rows-1,"8")
                laby[per_line]=change(laby[per_line],per_rows," ")
                per_rows=per_rows-1
                affiche(laby)
                
        if n=='r':
            if laby[per_line][per_rows+1] =="*":
                print("can't move  right")
            elif laby[per_line][per_rows+1] ==" ":
                laby[per_line]=change(laby[per_line],per_rows+1,"8")
                laby[per_line]=change(laby[per_line],per_rows," ")
                per_rows=per_rows+1
                print(per_rows)
                affiche(laby)
              
        if n=='t':
            if laby[per_line-1][per_rows] =="*" or laby[per_line]== 0 :
                print("can't move on the top")
            elif laby[per_line-1][per_rows] ==" ":
                laby[per_line-1]=change(laby[per_line-1],per_rows,"8")
                laby[per_line]=change(laby[per_line],per_rows," ")
                per_line=per_line-1
                affiche(laby)
             
        if n=='d':
            if laby[per_line+1][per_rows] =="*":
                print("can't move down")
            elif laby[per_line+1][per_rows] ==" ":
                laby[per_line+1]=change(laby[per_line+1],per_rows,"8")
                laby[per_line]=change(laby[per_line],per_rows," ")
                per_line=per_line+1
                print(per_line)
                affiche(laby)
            
        if (per_rows == 14 and len(laby)-1):
            affiche(laby)
            print("vous avez gagné")
            sys.exit(0)
            
except IndexError:
    pass
