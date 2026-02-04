# Ajoutez ceci à votre classe CollaborationManager dans src/collaboration.py
def share_code_snippet(self, user, code):
    """Enregistre un fragment de code partagé dans l'historique."""
    timestamp = datetime.datetime.now().strftime("%H:%M:%S")
    entry = {"user": user, "code": code, "time": timestamp}
    # On peut aussi le sauvegarder dans un fichier logs/shared_code.py
    with open("logs/last_submitted_code.py", "w") as f:
        f.write(code)
    return entry
