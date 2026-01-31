"""
Exemple d'utilisation du Moteur d'Exécution
Auteur: Sofiane
Date: 28/01/2026

Ce fichier montre comment utiliser le moteur d'exécution
dans différents scénarios réels.
"""

import sys
import os

# Ajouter le chemin du module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.execution_engine import ExecutionEngine


def example_1_basic_execution():
    """Exemple 1: Exécution basique"""
    print("\n" + "="*60)
    print("EXEMPLE 1: Exécution basique")
    print("="*60)
    
    engine = ExecutionEngine()
    
    code = """
# Programme simple
name = "Python"
version = 3.11
print(f"Bienvenue dans {name} {version}!")

# Calcul
numbers = [1, 2, 3, 4, 5]
total = sum(numbers)
print(f"La somme est: {total}")
"""
    
    result = engine.execute_code(code)
    
    print(f"\n✓ Succès: {result['success']}")
    print(f"✓ Output:\n{result['output']}")
    print(f"✓ Temps d'exécution: {result['execution_time']:.4f}s")
    print(f"✓ Mémoire utilisée: {result['memory_used']:.2f}MB")


def example_2_error_handling():
    """Exemple 2: Gestion des erreurs"""
    print("\n" + "="*60)
    print("EXEMPLE 2: Gestion des différents types d'erreurs")
    print("="*60)
    
    engine = ExecutionEngine()
    
    # Erreur de syntaxe
    print("\n[Test A] Erreur de syntaxe:")
    code_syntax = "if True"
    result = engine.execute_code(code_syntax)
    print(f"  Erreur: {result['error']}")
    
    # Division par zéro
    print("\n[Test B] Division par zéro:")
    code_zero = """
x = 100
y = 0
result = x / y
"""
    result = engine.execute_code(code_zero)
    print(f"  Erreur: {result['error']}")
    
    # Variable non définie
    print("\n[Test C] Variable non définie:")
    code_undefined = "print(variable_qui_nexiste_pas)"
    result = engine.execute_code(code_undefined)
    print(f"  Erreur: {result['error']}")


def example_3_validation():
    """Exemple 3: Validation de code"""
    print("\n" + "="*60)
    print("EXEMPLE 3: Validation de code avant exécution")
    print("="*60)
    
    engine = ExecutionEngine()
    
    codes_to_test = [
        ("Code correct", "x = 10\nprint(x)"),
        ("Syntaxe incorrecte", "if True"),
        ("Parenthèse manquante", "print('hello'"),
        ("Code valide complexe", "def func():\n    return 42\nprint(func())")
    ]
    
    for name, code in codes_to_test:
        is_valid, message = engine.validate_code(code)
        status = "✓" if is_valid else "✗"
        print(f"\n{status} {name}:")
        print(f"  Message: {message}")


def example_4_statistics():
    """Exemple 4: Statistiques d'utilisation"""
    print("\n" + "="*60)
    print("EXEMPLE 4: Statistiques après plusieurs exécutions")
    print("="*60)
    
    engine = ExecutionEngine()
    
    # Exécuter plusieurs codes
    test_codes = [
        "print('Test 1')",
        "x = 10 * 20\nprint(x)",
        "invalid syntax here",  # Erreur
        "import time\ntime.sleep(0.1)\nprint('Done')",
        "y = 1 / 0",  # Erreur
        "for i in range(3):\n    print(i)",
    ]
    
    print("\nExécution de 6 tests...")
    for i, code in enumerate(test_codes, 1):
        result = engine.execute_code(code)
        symbol = "✓" if result['success'] else "✗"
        print(f"  {symbol} Test {i}: {result['success']}")
    
    # Afficher les statistiques
    stats = engine.get_stats()
    print("\n--- STATISTIQUES ---")
    print(f"Total exécutions: {stats['total_executions']}")
    print(f"Taux de succès: {stats['success_rate']:.1f}%")
    print(f"Temps moyen: {stats['avg_execution_time']:.4f}s")
    print(f"Mémoire moyenne: {stats['avg_memory_used']:.2f}MB")
    print(f"Timeout configuré: {stats['timeout_limit']}s")
    print(f"Limite mémoire: {stats['memory_limit_mb']}MB")


def example_5_history():
    """Exemple 5: Historique des exécutions"""
    print("\n" + "="*60)
    print("EXEMPLE 5: Consultation de l'historique")
    print("="*60)
    
    engine = ExecutionEngine()
    
    # Exécuter quelques codes
    engine.execute_code("print('Première exécution')")
    engine.execute_code("x = 42\nprint(x)")
    engine.execute_code("print('Dernière exécution')")
    
    # Récupérer l'historique
    history = engine.get_history(limit=3)
    
    print(f"\nDernières {len(history)} exécutions:")
    for i, entry in enumerate(history, 1):
        result = entry['result']
        print(f"\n--- Exécution #{i} ---")
        print(f"Code: {entry['code']}")
        print(f"Succès: {result['success']}")
        print(f"Temps: {result['timestamp']}")
        if result['output']:
            print(f"Output: {result['output'][:50]}...")


def example_6_practical_use_case():
    """Exemple 6: Cas d'usage pratique - Vérificateur de devoirs"""
    print("\n" + "="*60)
    print("EXEMPLE 6: Cas pratique - Vérification de devoirs")
    print("="*60)
    
    engine = ExecutionEngine(timeout=3, max_memory_mb=30)
    
    # Code d'un étudiant pour calculer la factorielle
    student_code = """
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Tests
print("5! =", factorial(5))
print("10! =", factorial(10))
"""
    
    print("\n📝 Code étudiant à évaluer:")
    print(student_code)
    
    # Exécution et évaluation
    result = engine.execute_code(student_code)
    
    print("\n📊 RÉSULTAT DE L'ÉVALUATION:")
    if result['success']:
        print("✅ ACCEPTÉ - Le code s'exécute correctement")
        print(f"\nOutput obtenu:\n{result['output']}")
        print(f"\nPerformance:")
        print(f"  - Temps: {result['execution_time']:.4f}s")
        print(f"  - Mémoire: {result['memory_used']:.2f}MB")
        
        # Vérifier la sortie attendue
        if "120" in result['output'] and "3628800" in result['output']:
            print("\n✓ Les résultats sont corrects!")
        else:
            print("\n⚠ Les résultats semblent incorrects")
    else:
        print("❌ REJETÉ - Erreur détectée")
        print(f"\nErreur: {result['error']}")
        print(f"\nConseils pour l'étudiant:")
        print("  - Vérifier la syntaxe du code")
        print("  - S'assurer que toutes les variables sont définies")
        print("  - Tester le code localement avant soumission")


def main():
    """Fonction principale pour exécuter tous les exemples"""
    print("\n" + "🚀 " + "="*58)
    print("🚀  DÉMONSTRATIONS DU MOTEUR D'EXÉCUTION SÉCURISÉ")
    print("🚀 " + "="*58)
    
    examples = [
        example_1_basic_execution,
        example_2_error_handling,
        example_3_validation,
        example_4_statistics,
        example_5_history,
        example_6_practical_use_case,
    ]
    
    for example in examples:
        try:
            example()
        except Exception as e:
            print(f"\n❌ Erreur dans {example.__name__}: {e}")
    
    print("\n" + "="*60)
    print("✅ Toutes les démonstrations sont terminées!")
    print("="*60 + "\n")


if __name__ == "__main__":
    main()
