"""
Exemple d'utilisation du Module de Collaboration
Auteur: Faical
Date: 04/02/2026

Ce fichier montre comment gérer les sessions collaboratives
et l'historique des corrections d'équipe.
"""

import sys
import os

# Ajouter le chemin du module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.collaboration import CollaborationManager

def example_1_session_management():
    """Exemple 1: Gestion des membres de la session"""
    print("\n" + "="*60)
    print("EXEMPLE 1: Gestion des collaborateurs")
    print("="*60)
    
    manager = CollaborationManager()
    manager.register_collaborator("Sofiane")
    manager.register_collaborator("Ilies")
    members = manager.register_collaborator("Faical")
    
    print(f"Membres enregistrés : {members}")

def example_2_fix_tracking():
    """Exemple 2: Historique des corrections"""
    print("\n" + "="*60)
    print("EXEMPLE 2: Suivi des corrections d'erreurs")
    print("="*60)
    
    manager = CollaborationManager()
    manager.register_collaborator("Ilies")
    
    # Simulation de corrections
    manager.log_correction("Ilies", "NameError", "Définition de la variable x")
    manager.log_correction("Faical", "TypeError", "Conversion de str vers int")
    
    print(manager.format_collab_report())

def main():
    print("\n🚀 DÉMONSTRATIONS DU MODULE DE COLLABORATION")
    example_1_session_management()
    example_2_fix_tracking()
    print("\n✅ Démonstrations de Faical terminées!\n")

if __name__ == "__main__":
    main()
