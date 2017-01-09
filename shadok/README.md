#[EN]Stegano - Pompe

There was given a file called ![pompe.png]("pompe.png")
![pompe.png](pompe.png "pompe.png")

I decided to analyze it with StegSolve 1.3 by Caesum and found words written on the 2 last red bits ![lsbred.png]("lsbred.png"):


![lsbred.png](lsbred.png "lsbred.png")

Here is the witted message:

>BU BU GA GA GA MEU GA GA BU
>MEU BU BU BU MEU GA ZO BU
>MEU GA BU BU MEU BU BU GA
>MEU GA GA GA MEU GA GA BU
>GA BU ZO GA MEU BU GA BU ZO
>ZO BU BU MEU GA ZO BU ZO BU
>BU BU BU GA MEU GA MEU GA
>BU BU ZO MEU BU BU MEU GA
>GA BU ZO MEU GA GA MEU GA
>MEU GA MEU MEU MEU

After few search, I found that it was the "Shadok Language" (in base 4) :
http://www.dcode.fr/numeration-shadok

After decoding, I had a base 4 encoded string:
>11000300131113021301131103000301101203101221130212

Then I had to convert it to binary (from base 4 to base 2): 
http://www.dcode.fr/conversion-base-n

>101 0000 0011 0000 0111 0101 0111 0010 0111 0001 0111 0101 0011 0000 0011 0001 0100 0110 0011 0100 0110 1001 0111 0010 0110

The given number length wasn’t a multiple of 4 (and will be problematic for Ascii decoding), so I added a 0 at the beginning:

>0101 0000 0011 0000 0111 0101 0111 0010 0111 0001 0111 0101 0011 0000 0011 0001 0100 0110 0011 0100 0110 1001 0111 0010 0110

Then I converted it to Ascii 
(There is good websites who do base conversion and Ascii decoding).
For this, I used http://www.binaryhexconverter.com/binary-to-ascii-text-converter :

>P0urqu01F4ir
("Pourquoi Faire" mean "Why" / "To do what" in french. It refers to "Pourquoi faire simple quand on peut faire compliqué" which means "Why make it simple when you can make it complicated")

#[FR]Stegano - Pompe

Le fichier dont nous disposions s'appelait ![pompe.png]("pompe.png")
![pompe.png](pompe.png "pompe.png")

J'ai décidé de l'analyser avec StegSolve 1.3 by Caesum et j'ai trouvé des mots écrits sur les 2 derniers bits rouge ![lsbred.png]("lsbred.png"):


![lsbred.png](lsbred.png "lsbred.png")

Voici le message qui y était écrit:

>BU BU GA GA GA MEU GA GA BU
>MEU BU BU BU MEU GA ZO BU
>MEU GA BU BU MEU BU BU GA
>MEU GA GA GA MEU GA GA BU
>GA BU ZO GA MEU BU GA BU ZO
>ZO BU BU MEU GA ZO BU ZO BU
>BU BU BU GA MEU GA MEU GA
>BU BU ZO MEU BU BU MEU GA
>GA BU ZO MEU GA GA MEU GA
>MEU GA MEU MEU MEU

Après quelques recherches, le message semblait écrit en "Langage Shadok" (en base 4) :
http://www.dcode.fr/numeration-shadok

Après le décodage, j'avais une chaine de caractère encodée en base 4:
>11000300131113021301131103000301101203101221130212

Ensuite, je l'ai converti en base 2 (de la base 4 à la base 2): 
http://www.dcode.fr/conversion-base-n

>101 0000 0011 0000 0111 0101 0111 0010 0111 0001 0111 0101 0011 0000 0011 0001 0100 0110 0011 0100 0110 1001 0111 0010 0110

La taille du nombre donné n'était pas un multiple de 4 (et aurait été problématique pour le décodage Ascii), j'ai donc ajouté un 0 au début de la chaine:

>0101 0000 0011 0000 0111 0101 0111 0010 0111 0001 0111 0101 0011 0000 0011 0001 0100 0110 0011 0100 0110 1001 0111 0010 0110

Enfin, je l'ai converti en Ascii
(Il existe de bons sites proposant des conversions de bases et du décodage Ascii).
Pour ce challenge, j'ai utilisé http://www.binaryhexconverter.com/binary-to-ascii-text-converter :

>P0urqu01F4ir
("Pourquoi Faire" fait référence au proverbe Shadok "Pourquoi faire simple quand on peut faire compliqué")

