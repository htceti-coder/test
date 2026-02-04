### 📄 `docs/collaboration_doc.md` (Module 3)

# 📚 Documentation - Collaboration Temps Réel

**Auteur:** Faiçal Hima 
**Module:** `collaboration.py`

---

## 📌 Vue d'ensemble

Le module de collaboration gère l'aspect social et la traçabilité du projet. Il permet de suivre les membres actifs d'une session et d'historiser chaque correction apportée, créant ainsi un journal d'audit pour le travail d'équipe.

---

## 🎯 Fonctionnalités principales

### 1. **Gestion de Session**
- Enregistrement des collaborateurs par nom
- Calcul de la durée de la session collaborative
- Monitoring du nombre de participants actifs

### 2. **Suivi des Corrections (Audit Trail)**
- Journalisation de "Qui a corrigé Quoi"
- Horodatage automatique des interventions
- Description textuelle des solutions appliquées

### 3. **Reporting d'Équipe**
- Résumés statistiques des sessions
- Export de rapports d'activité formatés pour le Wiki/Rapport final

---

## 🔧 Utilisation

### Exemple basique de gestion de session

```python
from src.collaboration import CollaborationManager

# Créer une session
collab = CollaborationManager()

# Enregistrer des membres
collab.register_collaborator("Sofiane")
collab.register_collaborator("Ilyes")

# Enregistrer une action de correction
collab.log_correction(
    collaborator="Membre 2",
    error_type="SyntaxError",
    fix_description="Ajout des deux-points manquants ligne 5"
)

# Afficher le rapport d'activité
print(collab.format_collab_report())
```

---

## 📊 Structure du résultat

La méthode `get_session_summary()` retourne un dictionnaire avec les clés suivantes:

| Clé | Type | Description |
|-----|------|-------------|
| `duration` | str | Temps écoulé depuis le début de session |
| `total_collaborators` | int | Nombre de membres uniques enregistrés |
| `total_fixes` | int | Nombre total de corrections logguées |
| `fixes` | list | Liste détaillée des dictionnaires de correction |

---

## ⚙️ Configuration

- **Stockage**: Les données sont maintenues en mémoire vive pour la session actuelle et persistées via les logs système dans `logs/debugger.log`.
- **Mode Collaborative**: Compatible avec l'utilisation de VS Code Live Share.

---

## 🧪 Tests

Exécuter les tests unitaires:

```bash
# Lancer les tests de collaboration
pytest tests/test_collaboration.py -v

# Vérifier la couverture
pytest tests/test_collaboration.py --cov=src.collaboration
```

---

## 🔄 Intégration avec les autres modules

### Module de Debugging (Module 2)
Le `CollaborationManager` utilise les `error_type` identifiés par le Debugger pour documenter les corrections effectuées par les membres de l'équipe.

---
## 📝 Changelog

- ✨ Première version du gestionnaire de collaboration
- ✅ Système d'enregistrement des membres
- ✅ Journal d'audit des corrections
- ✅ Générateur de rapports de session
