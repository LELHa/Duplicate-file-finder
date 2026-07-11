from collections import defaultdict #permet de créer automatiquement une liste vide 
from pathlib import Path 
from hasher import calculate_hash

def find_duplicates(files: list[Path]) -> dict[str, list[Path]]:
    """
    Regroupe les fichiers ayant le même hash
    """
    hashes = defaultdict(list)

    for file in files:
        file_hash = calculate_hash(file) #on use la fct de calcul de hasher
        hashes[file_hash].append(file) #on définit hash comme clé

    duplicates = {}

    for file_hash, file_list in hashes.items():
        if len(file_list) > 1: #on garde les hash que si y a doublons
            duplicates[file_hash] = file_list
    return duplicates