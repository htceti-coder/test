### 📄 `docs/debugger_doc.md` (Module 2)

# 📚 Documentation - Moteur de Debugging Avancé

**Auteur:** Membre 2 (Analyste)  
**Date:** 28/01/2026  
**Module:** `debugger.py`

---

## 📌 Vue d'ensemble

Le moteur de debugging avancé intervient après l'exécution d'un script pour intercepter les exceptions. Il analyse les tracebacks bruts, extrait les informations critiques (type d'erreur, ligne) et fournit des suggestions de correction basées sur une base de connaissances intégrée.

---

## 🎯 Fonctionnalités principales

### 1. **Analyse d'Exceptions**
- Extraction du type d'erreur (SyntaxError, NameError, etc.)
- Identification précise de la ligne fautive via Regex
- Nettoyage des messages d'erreur système pour l'utilisateur

### 2. **Système de Suggestions**
- Base de connaissances (Knowledge Base) pour les erreurs courantes
- Conseils pédagogiques pour la résolution
- Gestion des erreurs inconnues avec lien vers la documentation officielle

### 3. **Classification et Logging**
- Évaluation de la sévérité (High/Medium)
- Journalisation persistante via `loguru` dans `logs/debugger.log`
- Historisation des erreurs pour analyse collaborative

---

## 🔧 Utilisation

### Installation des dépendances

```bash
pip install -r requirements.txt
```

### Exemple basique

```python
from src.debugger import Debugger

# Initialiser le debugger
debugger = Debugger()

# Simuler un résultat d'exécution erroné
result_errone = {
    'success': False,
    'error': 'ZeroDivisionError: division by zero (line 4)',
    'output': ''
}

# Analyser l'erreur
analysis = debugger.analyze(result_errone)

# Afficher le rapport formaté
print(debugger.format_report(analysis))
```

---

## 📊 Structure du résultat

La méthode `analyze()` retourne un dictionnaire avec les clés suivantes:

| Clé | Type | Description |
|-----|------|-------------|
| `status` | str | "SUCCESS" ou "FAILED" |
| `error_type` | str | Classe de l'exception (ex: NameError) |
| `line_number` | int/str | Ligne détectée ou "Unknown" |
| `message` | str | Message d'erreur détaillé |
| `suggestion` | str | Conseil de correction proposé |
| `severity` | str | Niveau de criticité (High/Medium) |

---

## 🛡️ Sécurité & Fiabilité

1. **Regex Robustes**: Extraction sécurisée des numéros de ligne même sur des formats de traceback variés.
2. **Fallback**: En cas d'erreur non reconnue, le système bascule sur une suggestion générique sans faire planter l'application.
3. **Isolation des Logs**: Les fichiers de logs sont limités en taille (rotation) pour éviter la saturation disque.

---

## 🧪 Tests

Exécuter les tests unitaires:

```bash
# Tous les tests du module 2
pytest tests/test_debugger.py -v

# Avec couverture de code
pytest tests/test_debugger.py --cov=src.debugger
```

---

## 🔄 Intégration avec les autres modules

### Module d'Exécution (Module 1)
Le debugger reçoit directement le dictionnaire de sortie de `ExecutionEngine`.

### Module de Collaboration (Module 3)
Les erreurs analysées sont transmises au module de collaboration pour être assignées à un membre de l'équipe pour correction.

---

## 📈 Évolutions futures

- [ ] Support multilingue pour les suggestions (Français/Anglais)
- [ ] Recherche automatique sur StackOverflow via API
- [ ] Analyse statique de code complémentaire (Linter)

---

## 📝 Changelog

### Version 1.0.0 (28/01/2026)
- ✨ Implémentation de l'analyseur Regex
- ✅ Base de connaissances initiale (7 types d'erreurs)
- ✅ Intégration de `loguru` pour la traçabilité
- ✅ Tests unitaires avec 100% de couverture

---

## 📞 Contact

**Auteur:** Membre 2 (Analyste)  
**Projet:** Mini-projet Python Debugging Collaboratif - G01  
**Module:** Doctorat - Troisième Cycle
