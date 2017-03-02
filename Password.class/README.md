#[EN] Password.class
In this challenge we were given a class file (compiled java) called ![Password.class](Password.class).

I decided to decompile it with an online decompiler ( http://www.javadecompilers.com ) and got a Java file:
 [Password.java](Password.java)

After some desobfuscating, I just saw that the flag was a simple XOR between "crypted_pass" (int array) and the key String.

So i made a simple python script: ![XOR_Strings.py](XOR_Strings.py)

And got the flag: flaginversejava24.1

#[Fr] Password.class
Sur ce challenge nous disposions d'un fichier "class" (java compilé) nommé ![Password.class](Password.class).

J'ai donc commencé par le décompiler avec un décompilateur en ligne ( http://www.javadecompilers.com ) afin d'optenir un fichier java:
 [Password.java](Password.java)

Après une légère desobfuscation, j'ai pu en déduire que le flag était un simple XOR ent "crypted_pass" (type int array) et key (type String).

J'ai donc fait un simple script python: ![XOR_Strings.py](XOR_Strings.py)

Et obtenu le flag: flaginversejava24.1
