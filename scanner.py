from pathlib import Path #on utilise path au lieu d'importer os 

#on veut ignorer les fichiers temporaires ou les fichiers inutiles
EXCLUDED_DIRS = {
    ".venv",
    ".git",
    "__pycache"
}

def scan_directory(directory: str) ->list[Path]: 
    #on prend le chemin directory comme des caractères par : str
    #la fct renvoie une liste de chemins
    """
    Parcourt un dossier et retourne tous les fichiers trouvés.
    """
    path = Path(directory) #on transforme le chemin en objet
    files = []
    for file in path.rglob("*"): # r pour récursif et * pour tout
        #on analyse tout les dossiers et sous-dossiers
        if file.is_file(): #on veut garder que les fichiers et non pas les dossiers
            if not any(folder in file.parts for folder in EXCLUDED_DIRS):
                #condition Booléens qui renvoie true pour l'exclure
                files.append(file)
    return files #on renvoie la liste 