from scanner import scan_directory
from hasher import calculate_hash 
from duplicate_finder import find_duplicates

folder = input("Dossier à analyser : ") #on demande le dossier
files = scan_directory(folder) #on applique le scan au dossier
duplicates = find_duplicates(files) #on appel notre fct

#pour les doublons 
print("\nDoublons trouvés:")
for file_hash, files in duplicates.items():
    print("\nHash :", file_hash)
    for file in files:
        print(".", file)


from utils import get_file_size, format_size
for file in files: 
    size = get_file_size(file)
    print(file, format_size(size))

#print(f"{len(files)} fichiers trouvés :") #on veut le nombre de fichier
#for file in files:
 #   print(file) #une boucle pour afficher tout les fichiers
  #  print(calculate_hash(file))