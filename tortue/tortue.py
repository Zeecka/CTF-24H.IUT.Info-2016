# -*- coding: utf-8 -*-
from tkinter import *

fileturtle = r"C:\Users\Zeecka\Desktop\IUT\24H INFO 2016\Epreuve Secu\tortue.txt"

fen = Tk() # Instanciate windows

screen=Canvas(fen, bg="#d0d0d0", height=250, width=1200)
screen.pack(expand=YES, fill=BOTH)

X = 100 # Start X
Y = 100 # Start Y

with open(fileturtle) as f: # Open File
	for elt in f: # Parse Line
		for caract in list(elt): # Parse char
			if(caract == ">"): # Move to Right
				X += 2
			elif(caract == "<"): # Move to Left
				X -= 2
			elif(caract == "^"): # Move to Top
				Y -= 2
			elif(caract == "v"): # Move to Bottom
				Y += 2
			screen.create_rectangle(X-1,Y-1,X+1,Y+1,fill="black",outline="black") # Write Current Pixel
fen.mainloop()