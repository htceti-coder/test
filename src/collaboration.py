import datetime
from loguru import logger

class CollaborationManager:
    """
    Module 3 : Gestion de la collaboration temps réel.
    Permet de suivre les contributeurs, les sessions de correction et l'historique partagé.
    """
    def __init__(self):
        self.session_start = datetime.datetime.now()
        self.collaborators = set()
        self.correction_history = []
        logger.info(f"Session de collaboration démarrée à {self.session_start}")

    def register_collaborator(self, name):
        """Ajoute un membre à la session active."""
        self.collaborators.add(name)
        logger.info(f"Collaborateur {name} a rejoint la session.")
        return list(self.collaborators)

    def log_correction(self, collaborator, error_type, fix_description):
        """Enregistre une correction effectuée par un membre."""
        entry = {
            "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "user": collaborator,
            "error_fixed": error_type,
            "description": fix_description
        }
        self.correction_history.append(entry)
        logger.info(f"Correction enregistrée par {collaborator} pour l'erreur {error_type}")
        return entry

    def get_session_summary(self):
        """Retourne un résumé de l'activité de collaboration."""
        return {
            "duration": str(datetime.datetime.now() - self.session_start),
            "total_collaborators": len(self.collaborators),
            "total_fixes": len(self.correction_history),
            "fixes": self.correction_history
        }

    def format_collab_report(self):
        """Génère un affichage convivial pour le travail d'équipe."""
        summary = self.get_session_summary()
        report = f"\n{'*'*40}\n"
        report += f"🤝 RAPPORT DE COLLABORATION\n"
        report += f"{'*'*40}\n"
        report += f"👥 Membres actifs : {', '.join(self.collaborators)}\n"
        report += f"⏳ Durée session : {summary['duration']}\n"
        report += f"✅ Corrections effectuées : {summary['total_fixes']}\n"
        
        for fix in summary['fixes']:
            report += f"  - [{fix['timestamp']}] {fix['user']} a corrigé {fix['error_fixed']}\n"
        
        report += f"{'*'*40}"
        return report
