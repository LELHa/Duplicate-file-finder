from scanner import scan_directory
from hasher import calculate_hash 
from duplicate_finder import find_duplicates
from utils import get_file_size, format_size



def main(): #on créer une sorte de classe
    print("\n---------DUPLICATE FINDER---------\n")

    folder = input("Dossier à analyser : ") #on demande le dossier
    print("\nAnalyse en cours\n") 

    files = scan_directory(folder) #on applique le scan au dossier
    print(f"{len(files)} fichiers trouvés :") #on veut le nombre de fichier

    duplicates = find_duplicates(files) #on appel notre fct

    if not duplicates:
        print("\n Aucun doublon trouvé")
        return
    
    print(f"\nDoublons trouvés : {len(duplicates)} groupe(s)")

    total_saved = 0

    for index, (file_hash, file_list) in enumerate(duplicates.items(), start=1):

        print(f"\nGroupe {index}")
        print("-" * 20)

        group_size = get_file_size(file_list[0])

        for file in file_list:
            print("-", file)

        saved = group_size * (len(file_list) - 1) #calcul la taille 
        total_saved += saved

    print("\nEspace récupérable :", format_size(total_saved))


if __name__ == "__main__": #initialisation
    main()


