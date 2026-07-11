from scanner import scan_directory
from hasher import calculate_hash 

folder = input("Dossier à analyser : ") #on demande le dossier
files = scan_directory(folder) #on applique le scan au dossier
print(f"{len(files)} fichiers trouvés :") #on veut le nombre de fichier
for file in files:
    print(file) #une boucle pour afficher tout les fichiers
    print(calculate_hash(file))