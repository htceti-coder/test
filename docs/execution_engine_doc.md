# 📚 Documentation - Moteur d'Exécution Sécurisé

**Auteur:** Sofiane  
**Date:** 28/01/2026  
**Module:** `execution_engine.py`

---

## 📌 Vue d'ensemble

Le moteur d'exécution sécurisé permet d'exécuter du code Python fourni par les utilisateurs de manière isolée et contrôlée, avec capture des erreurs, timeout et monitoring des ressources.

---

## 🎯 Fonctionnalités principales

### 1. **Exécution sécurisée**
- Isolation du code utilisateur
- Protection contre les boucles infinies (timeout)
- Limitation de la consommation mémoire
- Capture des outputs (stdout/stderr)

### 2. **Gestion des erreurs**
- Détection des erreurs de syntaxe
- Capture des exceptions runtime
- Stack trace détaillée
- Classification des types d'erreurs

### 3. **Monitoring**
- Temps d'exécution précis
- Consommation mémoire
- Historique des exécutions
- Statistiques globales

---

## 🔧 Utilisation

### Installation des dépendances

```bash
pip install -r requirements.txt
```

### Exemple basique

```python
from src.execution_engine import ExecutionEngine

# Créer une instance du moteur
engine = ExecutionEngine(timeout=10, max_memory_mb=100)

# Exécuter du code
code = """
print("Hello World")
x = 10 + 20
print(f"Résultat: {x}")
"""

result = engine.execute_code(code)

# Vérifier le résultat
if result['success']:
    print("✓ Exécution réussie!")
    print(f"Output: {result['output']}")
    print(f"Temps: {result['execution_time']:.4f}s")
else:
    print("✗ Erreur détectée!")
    print(f"Erreur: {result['error']}")
    print(f"Traceback: {result['traceback']}")
```

### Exemple avec validation préalable

```python
# Valider le code avant exécution
code = "print('test')"
is_valid, message = engine.validate_code(code)

if is_valid:
    result = engine.execute_code(code)
else:
    print(f"Code invalide: {message}")
```

### Consulter l'historique

```python
# Récupérer les 5 dernières exécutions
history = engine.get_history(limit=5)

for i, entry in enumerate(history, 1):
    print(f"\n--- Exécution #{i} ---")
    print(f"Code: {entry['code']}")
    print(f"Succès: {entry['result']['success']}")
```

### Obtenir des statistiques

```python
stats = engine.get_stats()

print(f"Total exécutions: {stats['total_executions']}")
print(f"Taux de succès: {stats['success_rate']:.2f}%")
print(f"Temps moyen: {stats['avg_execution_time']:.4f}s")
print(f"Mémoire moyenne: {stats['avg_memory_used']:.2f}MB")
```

---

## 📊 Structure du résultat

La méthode `execute_code()` retourne un dictionnaire avec les clés suivantes:

| Clé | Type | Description |
|-----|------|-------------|
| `success` | bool | True si l'exécution a réussi |
| `output` | str | Sortie standard du programme |
| `error` | str | Message d'erreur (si échec) |
| `execution_time` | float | Temps d'exécution en secondes |
| `memory_used` | float | Mémoire utilisée en MB |
| `traceback` | str | Stack trace complète |
| `timestamp` | str | Date et heure de l'exécution |

---

## ⚙️ Configuration

### Paramètres du constructeur

```python
ExecutionEngine(timeout=10, max_memory_mb=100)
```

- **timeout** (int): Temps maximum d'exécution en secondes (défaut: 10s)
- **max_memory_mb** (int): Mémoire maximale autorisée en MB (défaut: 100MB)

---

## 🛡️ Sécurité

### Mesures de protection

1. **Timeout**: Arrêt automatique après le délai défini
2. **Limite mémoire**: Protection contre la surconsommation
3. **Isolation**: Environnement d'exécution séparé
4. **Pas d'accès fichiers**: Le code ne peut pas lire/écrire de fichiers (par défaut)

### Limitations connues

⚠️ **Attention**: Ce moteur ne protège pas contre:
- Les opérations réseau non contrôlées
- L'import de modules système dangereux
- Les attaques par déni de service sophistiquées

Pour une utilisation en production, considérer l'ajout de:
- `RestrictedPython` pour limiter les imports
- Conteneurisation (Docker) pour isolation complète
- Rate limiting au niveau applicatif

---

## 🧪 Tests

Exécuter les tests unitaires:

```bash
# Tous les tests
pytest tests/test_execution_engine.py -v

# Avec couverture de code
pytest tests/test_execution_engine.py --cov=src/execution_engine
```

---

## 🔄 Intégration avec les autres modules

### Module de debugging (Membre 2)
```python
# Le moteur peut passer ses résultats au debugger
from src.debugger import Debugger

result = engine.execute_code(code)
if not result['success']:
    debugger = Debugger()
    analysis = debugger.analyze_error(result)
```

### Module de collaboration (Membre 3)
```python
# Partager les résultats d'exécution
from src.collaboration import ShareSession

result = engine.execute_code(code)
session = ShareSession()
session.broadcast_execution_result(result)
```

---

## 📈 Évolutions futures

- [ ] Support des entrées utilisateur multiples
- [ ] Sauvegarde de l'historique en base de données
- [ ] Export des logs au format JSON
- [ ] Interface web pour visualisation
- [ ] Support des notebooks Jupyter
- [ ] Sandboxing renforcé avec Docker

---

## 🤝 Contribution

Pour contribuer à ce module:

1. Créer une branche: `git checkout -b feature/nom-feature`
2. Commiter les changements: `git commit -m "Description"`
3. Pousser: `git push origin feature/nom-feature`
4. Créer une Pull Request

---

## 📝 Changelog

### Version 1.0.0 (28/01/2026)
- ✨ Première version du moteur d'exécution
- ✅ Exécution sécurisée avec timeout
- ✅ Capture des exceptions
- ✅ Monitoring mémoire et temps
- ✅ Historique et statistiques
- ✅ Tests unitaires complets

---

## 📞 Contact

**Auteur:** Sofiane  
**Projet:** Mini-projet Python Debugging Collaboratif - G01  
**Module:** Doctorat - Troisième Cycle