#!/usr/bin/env python

# programme  pyramide


def interet(w,b,d):
	i=1
	while (i<=b):
		w=w+(w*d)
		print(int(w))
		i+=1
				
x=int(input("somme versée =" ))
a=20
taux=4.5/100
interet(x,a,taux)


