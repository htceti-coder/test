import datetime
import json
import os
from loguru import logger

class CollaborationManager:
    def __init__(self):
        self.session_start = datetime.datetime.now()
        self.collaborators = set()
        self.correction_history = []
        self.chat_file = "logs/chat_history.json"
        
        # Ensure logs directory exists
        os.makedirs("logs", exist_ok=True)
        if not os.path.exists(self.chat_file):
            with open(self.chat_file, 'w') as f:
                json.dump([], f)

    def register_collaborator(self, name):
        self.collaborators.add(name)
        logger.info(f"Collaborateur {name} a rejoint la session.")
        return list(self.collaborators)

    def send_message(self, user, message):
        """Saves a message to the shared JSON chat file."""
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        new_msg = {"user": user, "text": message, "time": timestamp}
        
        # Read existing messages
        with open(self.chat_file, 'r') as f:
            messages = json.load(f)
        
        messages.append(new_msg)
        
        # Save back
        with open(self.chat_file, 'w') as f:
            json.dump(messages, f)
        return new_msg

    def get_chat_history(self):
        """Retrieves all messages."""
        with open(self.chat_file, 'r') as f:
            return json.load(f)

    def share_code_snippet(self, user, code):
        """Enregistre un fragment de code partagé dans l'historique."""
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        entry = {"user": user, "code": code, "time": timestamp}
        # On peut aussi le sauvegarder dans un fichier logs/shared_code.py
        with open("logs/last_submitted_code.py", "w") as f:
            f.write(code)
        return entry
