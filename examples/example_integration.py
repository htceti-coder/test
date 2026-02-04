"""
Exemple d'Intégration Complète de la Plateforme
Auteur: Abderrahman
Date: 04/02/2026

Ce fichier démontre le workflow complet : Exécution -> Debugging -> Collaboration.
"""

import sys
import os

# Ajouter le chemin du module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.execution_engine import ExecutionEngine
from src.debugger import Debugger
from src.collaboration import CollaborationManager

def example_full_workflow():
    """Flux complet : Erreur -> Analyse -> Correction d'équipe"""
    print("\n" + "="*60)
    print("WORKFLOW COMPLET : SCÉNARIO DE DOCTORAT")
    print("="*60)
    
    # 1. Initialisation de l'environnement
    engine = ExecutionEngine()
    debugger = Debugger()
    collab = CollaborationManager()
    
    # 2. Arrivée de l'équipe
    collab.register_collaborator("Sofiane")
    collab.register_collaborator("Ilies")
    collab.register_collaborator("Abderrahman")

    # 3. Exécution d'un code erroné
    code = "print(10 / 0) # Erreur de division"
    print("\n1. Tentative d'exécution du code...")
    result = engine.execute_code(code)

    # 4. Diagnostic automatique
    if not result['success']:
        print("2. Échec détecté. Analyse en cours...")
        analysis = debugger.analyze(result)
        print(debugger.format_report(analysis))

        # 5. Résolution collaborative
        print("3. Correction appliquée par l'expert.")
        collab.log_correction(
            collaborator="Abderrahman",
            error_type=analysis['error_type'],
            fix_description="Ajout d'une vérification de division par zéro"
        )

    # 6. Rapport Final
    print("\n4. Rapport final de la session collaborative :")
    print(collab.format_collab_report())

def main():
    print("\n🚀 DÉMONSTRATION D'INTÉGRATION GLOBALE (Membre 4)")
    example_full_workflow()
    print("\n✅ Démonstration d'Abderrahman terminée!\n")

if __name__ == "__main__":
    main()
