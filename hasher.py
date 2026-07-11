import hashlib
from pathlib import Path

def calculate_hash(file_path: Path) -> str: #la fct prends le fichier et renvoie du texte
    """
    Calcule le hash d'un fichier.
    """
    sha256 = hashlib.sha256() #reçoit le contenu du fichier
    with file_path.open("rb") as file:
        #on utilise rb et pas r pour les images, exe, vidéos
        #with chunk := file.read(4096): #on lit par 4 ko et on calcule peu à peu
            #sha256.update(chunk)

            #pour python en 3.1x
        while True: 
            chunk = file.read(4096)
            if not chunk:
                break #vérifie si chunk est vide
            sha256.update(chunk)
    return sha256.hexdigest() #on transforme le hash en texte lisible