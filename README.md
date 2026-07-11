# Duplicate-file-finder
Tool to find duplicates files

*on utilise les hash des fichiers pour détecter les doublons*

On commence par créer le scanner pour obtenir les fichiers existants

2e etape on veut reconnaitre les doublons on veux le hash des fichiers
on utilise sha et pas md5 car des collisions sont possibles (same hash alors que fichier différents par md5)

on utilise sha 256 et pas sha 512 car plus long (et permet encore plus d'éviter les collisions) mais ici le plus rapide est le 256 dans le projet