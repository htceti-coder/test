# mini-projet-python-debugging-collaboratif-g01

📌 Contexte : 
Mini-projet collaboratif réalisé dans le cadre du Doctorat – Troisième Cycle, visant à approfondir les techniques de debugging Python et le travail collaboratif à l’aide des outils DevOps.

🎯 Objectifs pédagogiques : 
- Maîtriser le debugging avancé en Python
- Identifier, analyser et corriger des erreurs complexes
- Travailler efficacement en équipe via Git/GitHub
- Utiliser des outils collaboratifs (cloud, Live Share)

🧩 Description du projet : 
Développer une plateforme permettant aux utilisateurs de soumettre du code Python, de détecter automatiquement les erreurs, de visualiser les logs et de collaborer à la correction du code.

⚙️ Fonctionnalités attendues : 
+ Exécution sécurisée de scripts Python
+ Capture et analyse des exceptions
+ Génération de logs détaillés
+ Correction collaborative du code
+ Historique des erreurs et corrections

🛠️ Technologies à utiliser : 
    - Python
    - Git / GitHub
    - Google Colab
    - Visual Studio Live Share

👥 Répartition du travail (suggestion) : 
- Membre 1 : moteur d’exécution
- Membre 2 : module de debugging
- Membre 3 : collaboration temps réel
- Membre 4 : documentation & gestion GitHub

📦 Livrables attendus : 
         - Dépôt GitHub structuré (Code source versionné)
         - Wiki Documentation projet 
         - Rapport technique PDF
         - Journal de commits


# PACK COMPLET - MODULE 1 : MOTEUR D'EXÉCUTION

**Auteur** : Sofiane  
**Projet** : Mini-Projet Python Debugging Collaboratif - G01  
**Module** : 1 - Moteur d'Exécution Sécurisé  
**Date** : 28/01/2026  

## 📁 Structure du projet

```
mini-projet-python-debugging-collaboratif-g01/
│
├── src/                          # Code source
│   ├── __init__.py
│   ├── execution_engine.py       # ✅ Module 1 - Moteur d'exécution (Sofiane)
│   ├── debugger.py               # ⏳ Module 2 - Debugging (Membre 2)
│   ├── collaboration.py          # ⏳ Module 3 - Collaboration (Membre 3)
│   └── utils.py                  # Utilitaires communs
│
├── tests/                        # Tests unitaires
│   ├── __init__.py
│   ├── test_execution_engine.py  # ✅ Tests module 1
│   ├── test_debugger.py          # ⏳ Tests module 2
│   └── test_collaboration.py     # ⏳ Tests module 3
│
├── docs/                         # Documentation
│   ├── execution_engine_doc.md   # ✅ Doc module 1
│   ├── debugger_doc.md           # ⏳ Doc module 2
│   └── collaboration_doc.md      # ⏳ Doc module 3
│
├── examples/                     # Exemples d'utilisation
│   └── example_usage.py          # ✅ Démonstrations
│
├── logs/                         # Fichiers de logs
│   └── .gitkeep
│
├── .gitignore                    # Fichiers à ignorer
├── requirements.txt              # Dépendances Python
├── README.md                     # Ce fichier
└── CONTRIBUTING.md               # Guide de contribution
```
### Étapes d'installation

```bash
# 1. Cloner le repository
git clone https://github.com/[superviseur]/mini-projet-python-debugging-collaboratif-g01.git
cd mini-projet-python-debugging-collaboratif-g01

# 2. Créer un environnement virtuel (recommandé)
python -m venv venv

# 3. Activer l'environnement virtuel
# Sur Windows:
venv\Scripts\activate
# Sur Linux/Mac:
source venv/bin/activate

# 4. Installer les dépendances
pip install -r requirements.txt

# 5. Vérifier l'installation
python -c "from src.execution_engine import ExecutionEngine; print('✓ Installation réussie!')"
```

---

## 💻 Utilisation

### Exemple rapide - Module 1 (Moteur d'exécution)

```python
from src.execution_engine import ExecutionEngine

# Créer une instance
engine = ExecutionEngine(timeout=10, max_memory_mb=100)

# Exécuter du code
code = """
print("Hello World!")
x = 10 + 20
print(f"Résultat: {x}")
"""

result = engine.execute_code(code)

# Afficher le résultat
if result['success']:
    print("✓ Exécution réussie!")
    print(result['output'])
else:
    print("✗ Erreur:", result['error'])
```

### Lancer les tests

```bash
# Tous les tests
pytest tests/ -v

# Tests avec couverture de code
pytest tests/ --cov=src --cov-report=html

# Tests d'un module spécifique
pytest tests/test_execution_engine.py -v
```

### Lancer les exemples

```bash
# Démonstration du moteur d'exécution
python examples/example_usage.py

# Démonstration basique
python src/execution_engine.py
```

---

## 📚 Documentation

- **[Module 1 - Moteur d'Exécution](docs/execution_engine_doc.md)** ✅
- **[Module 2 - Debugger](docs/debugger_doc.md)** ⏳
- **[Module 3 - Collaboration](docs/collaboration_doc.md)** ⏳
- **[Guide de contribution](CONTRIBUTING.md)** ⏳

---

## 🔄 Workflow Git

### Pour commencer à travailler

```bash
# 1. Créer une branche pour votre fonctionnalité
git checkout -b feature/nom-fonctionnalite

# 2. Faire vos modifications
# ... coder ...

# 3. Ajouter les fichiers modifiés
git add .

# 4. Commit avec un message descriptif
git commit -m "feat: ajout de la fonctionnalité X"

# 5. Pousser vers GitHub
git push origin feature/nom-fonctionnalite

# 6. Créer une Pull Request sur GitHub
```

### Convention de nommage des commits

- `feat:` Nouvelle fonctionnalité
- `fix:` Correction de bug
- `docs:` Documentation
- `test:` Ajout/modification de tests
- `refactor:` Refactorisation du code
- `style:` Formatage, indentation

---

## 🧪 Tests et qualité du code

```bash
# Lancer tous les tests
pytest tests/ -v

# Tests avec couverture
pytest tests/ --cov=src --cov-report=term-missing

# Générer un rapport HTML de couverture
pytest tests/ --cov=src --cov-report=html
# Puis ouvrir: htmlcov/index.html

# Vérifier le style de code (PEP 8)
flake8 src/ tests/
```

---

## 📦 Livrables attendus

- [x] ✅ **Dépôt GitHub structuré** (avec branches, commits réguliers)
- [x] ✅ **Code source versionné** (Module 1 complété)
- [ ] ⏳ **Wiki / Documentation projet**
- [ ] ⏳ **Rapport technique PDF**
- [ ] ⏳ **Journal de commits détaillé**

---
### Règles de base

1. **Créer une branche** pour chaque nouvelle fonctionnalité
2. **Écrire des tests** pour le nouveau code
3. **Documenter** les fonctions et modules
4. **Faire des commits atomiques** avec des messages clairs
5. **Créer une Pull Request** pour review

---

## 📊 Progression du projet

| Module | Progression | Dernière mise à jour |
|--------|------------|---------------------|
| Moteur d'exécution | ████████████ 100% | 28/01/2026 - Sofiane |
| Module debugging | ░░░░░░░░░░░░ 0% | - |
| Collaboration | ░░░░░░░░░░░░ 0% | - |
| Documentation | ████░░░░░░░░ 33% | 28/01/2026 |

---

## 📝 Changelog

### [Version 0.1.0] - 28/01/2026

#### Ajouté (par Sofiane)
- ✅ Moteur d'exécution sécurisé complet
- ✅ Gestion des exceptions et timeout
- ✅ Monitoring mémoire et temps d'exécution
- ✅ Historique et statistiques
- ✅ Tests unitaires (8 tests, 100% couverture)
- ✅ Documentation complète
- ✅ Exemples d'utilisation

---

## 👨‍🎓 Équipe

- **Sofiane** - Module 1: Moteur d'exécution ✅
- **Membre 2** - Module 2: Debugging ⏳
- **Membre 3** - Module 3: Collaboration ⏳
- **Membre 4** - Documentation & GitHub ⏳

---

**Dernière mise à jour:** 28/01/2026 par Sofiane  
**Projet:** Mini-projet Python Debugging Collaboratif - G01  
