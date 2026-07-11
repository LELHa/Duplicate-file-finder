from pathlib import Path

def get_file_size(file: Path) -> int:
    """
    Retourne la taille d'un fichier en octets.
    """
    return file.stat().st_size
#file.stat() à les infos de nom, date de création, taille, permissions
#st_size c'est la taille en octets

def format_size(size: int) -> str:
    """
    Convertit une taille en octets en format lisible
    """
    #on définits les unités dispo
    units = ["B", "KB","MB", "GB"]

    for unit in units:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /=1024 #on divise pour le nombre 
    return f"{size:.2f}TB"