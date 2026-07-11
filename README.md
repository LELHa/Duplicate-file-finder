# Duplicate-file-finder
Tool to find duplicates files

*on utilise les hash des fichiers pour détecter les doublons*

On commence par créer le scanner pour obtenir les fichiers existants

2e etape on veut reconnaitre les doublons on veux le hash des fichiers
on utilise sha et pas md5 car des collisions sont possibles (same hash alors que fichier différents par md5)

on utilise sha 256 et pas sha 512 car plus long (et permet encore plus d'éviter les collisions) mais ici le plus rapide est le 256 dans le projet

mnt on veut détecter les fichiers identiques par un dico 
par hash on aura la liste de ceux avec le meme hash 

mnt on veut ajouter la taille supprimable si on supprime les copies

puis on rajoute la conversion 