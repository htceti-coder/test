# Documentation Module 3 : Collaboration Temps Réel

## Rôle
Ce module gère l'aspect humain et collaboratif du projet. Il permet de tracer l'activité des développeurs sur la plateforme.

## Fonctionnalités
1. **Gestion des Collaborateurs** : Enregistrement des membres présents lors d'une session Live Share ou Colab.
2. **Historique des Corrections** : Journalisation de qui a corrigé quel bug et comment.
3. **Rapport de Session** : Génération d'un résumé de l'activité d'équipe.

## Interaction avec les autres modules
- Le **Module 2 (Debugger)** identifie l'erreur.
- Le **Module 3 (Collaboration)** enregistre l'action corrective prise par un humain pour cette erreur.

## Guide Live Share
Pour utiliser ce projet en collaboration temps réel :
1. Installer l'extension **VS Code Live Share**.
2. Cliquer sur "Share" et envoyer le lien à vos coéquipiers.
3. Utiliser `CollaborationManager.register_collaborator()` pour logger votre présence.
