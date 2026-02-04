import re
from loguru import logger

# Configuration du logging pour le module 2
logger.add("logs/debugger.log", rotation="1 MB", retention="10 days", level="INFO")

class Debugger:
    """
    Module 2: Analyseur d'erreurs et suggestions.
    """
    def __init__(self):
        self.knowledge_base = {
            "SyntaxError": "Vérifiez les deux-points (:), les parenthèses ou l'indentation.",
            "NameError": "Variable non définie. Vérifiez l'orthographe ou l'initialisation.",
            "ZeroDivisionError": "Division par zéro impossible. Ajoutez une condition 'if'.",
            "TypeError": "Types incompatibles. Utilisez int() ou str() pour convertir.",
            "IndexError": "Index hors limites. Vérifiez la taille de votre liste."
        }

    def analyze(self, execution_result):
        """Analyse le dictionnaire de sortie du moteur d'exécution."""
        if execution_result.get('success'):
            logger.info("Exécution réussie.")
            return {"status": "SUCCESS", "analysis": None}

        raw_error = execution_result.get('error', "")
        
        # Extraction du type et du message
        parts = raw_error.split(':', 1)
        error_type = parts[0].strip()
        error_msg = parts[1].strip() if len(parts) > 1 else "Pas de détails"

        # Extraction de la ligne via Regex
        line_match = re.search(r"line (\d+)", raw_error)
        line_no = int(line_match.group(1)) if line_match else "Unknown"

        analysis = {
            "status": "FAILED",
            "error_type": error_type,
            "line_number": line_no,
            "message": error_msg,
            "suggestion": self.knowledge_base.get(error_type, "Consultez la documentation Python officielle."),
            "severity": "High" if error_type in ["SyntaxError", "IndentationError"] else "Medium"
        }

        logger.error(f"Erreur détectée: {error_type} à la ligne {line_no}")
        return analysis

    def format_report(self, analysis):
        """Génère un rapport lisible pour l'utilisateur."""
        if analysis["status"] == "SUCCESS":
            return "Code valide."

        return (
            f"\n--- RAPPORT DE DEBUGGING ---\n"
            f"Type       : {analysis['error_type']}\n"
            f"Ligne      : {analysis['line_number']}\n"
            f"Message    : {analysis['message']}\n"
            f"Suggestion : {analysis['suggestion']}\n"
            f"---------------------------"
        )
