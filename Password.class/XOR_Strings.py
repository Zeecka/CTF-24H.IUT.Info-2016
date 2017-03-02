from PIL import Image

cle = 'vcqztxhdwiukgordbsm'
passwd = [16, 15, 16, 29, 29, 22, 30, 1, 5, 26, 16, 1, 6, 25, 19, 86, 86, 93, 92]

x1 = []
x2 = []

# On converti String vers tableau de caractère si on a pas déjà

if(type(cle) == type("a")):
	for elt in cle:
		x1.append(ord(elt))
else:
	x1 = list(cle)

if(type(passwd) == type("a")):
	for elt in passwd:
		x2.append(ord(elt))
else:
	x2 = list(passwd)

output = ""
outputCode = []

for i in range(len(x2)): # x2 : pass a decode (et non la taille de la clef)
	code = x1[i]^x2[i]
	outputCode.append(code)
	output += chr(code)

print(output)