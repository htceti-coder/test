# Documentation Module 2 : Moteur de Debugging

## Introduction
Le module `Debugger` est conçu pour analyser les sorties du moteur d'exécution et fournir une aide au diagnostic immédiate.

## Architecture
- **Classe principale** : `Debugger`
- **Méthode `analyze(result)`** : Prend en entrée le dictionnaire du Module 1 et retourne un rapport structuré.
- **Méthode `format_report(analysis)`** : Convertit l'analyse en une chaîne de caractères lisible.

## Dépendances
- `re` (Standard library) : Pour le parsing des lignes.
- `loguru` : Pour la persistance des logs dans `logs/debugger.log`.

## Tests et Qualité
Le module est couvert à 100% par des tests unitaires (`pytest`).
