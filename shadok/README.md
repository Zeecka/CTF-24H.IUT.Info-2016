#Stegano - Pompe

There was given a file called "pompe.png"

![pompe.png](https://github.com/Zeecka/CTF-24H.IUT.Info-2016/tree/master/shadok/pompe.png)



LSB Red --> lsbred.png

BU BU GA GA GA MEU GA GA BU
MEU BU BU BU MEU GA ZO BU
MEU GA BU BU MEU BU BU GA
MEU GA GA GA MEU GA GA BU
GA BU ZO GA MEU BU GA BU ZO
ZO BU BU MEU GA ZO BU ZO BU
BU BU BU GA MEU GA MEU GA
BU BU ZO MEU BU BU MEU GA
GA BU ZO MEU GA GA MEU GA
MEU GA MEU MEU MEU

Il s'agit du langage Shadok en base 4:
http://www.dcode.fr/numeration-shadok


L'outil utilisé ici pour la conversions de base: 
http://www.dcode.fr/numeration-shadok
http://www.dcode.fr/conversion-base-n


Conversion Shadok en base 4 "normale":

11000300131113021301131103000301101203101221130212

Conversion en base 10 (intermédiaire sur dcode.fr)

397078141648510744583962269478

Conversion en base 2 (binaire) 

101000000110000011101010111001001110001011101010011000000110001010001100011010001101001011100100110

On observe un zero manquant :
101 0000 0011 0000 0111 0101 0111 0010 0111 0001 0111 0101 0011 0000 0011 0001 0100 0110 0011 0100 0110 1001 0111 0010 0110

Celui-ci est donc ajouté en début de chaine.
0101000000110000011101010111001001110001011101010011000000110001010001100011010001101001011100100110

Conversion en Ascii:

P0urqu01F4ir
