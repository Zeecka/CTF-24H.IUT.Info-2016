# -*- coding: utf-8 -*-
from tkinter import *

fichier = r"C:\Users\Zeecka\Desktop\IUT\24H INFO 2016\Epreuve Secu\tortue.txt"
fen = Tk()

ecran=Canvas(fen, bg="#d0d0d0", height=1000, width=1000)
ecran.pack(expand=YES, fill=BOTH)

X = 250
Y = 250

with open(fichier) as f:
	for elt in f:
		for caract in list(elt):
			ecran.create_rectangle(X-1,Y-1,X+1,Y+1,fill="black",outline="black")
			if(caract == ">"):
				X += 2
			elif(caract == "<"):
				X -= 2
			elif(caract == "^"):
				Y -= 2
			elif(caract == "v"):
				Y += 2