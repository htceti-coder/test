#!/usr/bin/env python
"""
Script de vérification - Installation et Tests
Auteur: Sofiane
Date: 28/01/2026

Ce script vérifie que tout est correctement installé et fonctionne.
"""

import sys
import os


def print_header(title):
    """Affiche un en-tête formaté"""
    print("\n" + "=" * 60)
    print(f"  {title}")
    print("=" * 60)


def check_python_version():
    """Vérifie la version de Python"""
    print_header("VÉRIFICATION DE PYTHON")
    
    version = sys.version_info
    print(f"Version Python: {version.major}.{version.minor}.{version.micro}")
    
    if version.major >= 3 and version.minor >= 8:
        print("✅ Version Python compatible (>= 3.8)")
        return True
    else:
        print("❌ Python 3.8+ requis")
        return False


def check_dependencies():
    """Vérifie que les dépendances sont installées"""
    print_header("VÉRIFICATION DES DÉPENDANCES")
    
    dependencies = {
        'psutil': 'Monitoring système',
        'pytest': 'Framework de tests',
    }
    
    all_installed = True
    for module, description in dependencies.items():
        try:
            __import__(module)
            print(f"✅ {module:15s} - {description}")
        except ImportError:
            print(f"❌ {module:15s} - MANQUANT")
            all_installed = False
    
    if not all_installed:
        print("\n💡 Pour installer les dépendances manquantes:")
        print("   pip install -r requirements.txt")
    
    return all_installed


def check_project_structure():
    """Vérifie la structure du projet"""
    print_header("VÉRIFICATION DE LA STRUCTURE")
    
    required_files = [
        'src/__init__.py',
        'src/execution_engine.py',
        'tests/__init__.py',
        'tests/test_execution_engine.py',
        'docs/execution_engine_doc.md',
        'examples/example_usage.py',
        'requirements.txt',
        'README.md',
    ]
    
    all_present = True
    for file_path in required_files:
        if os.path.exists(file_path):
            print(f"✅ {file_path}")
        else:
            print(f"❌ {file_path} - MANQUANT")
            all_present = False
    
    return all_present


def test_execution_engine():
    """Teste le moteur d'exécution"""
    print_header("TEST DU MOTEUR D'EXÉCUTION")
    
    try:
        # Ajouter src au path
        sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))
        
        from execution_engine import ExecutionEngine
        
        # Test 1: Code simple
        print("\n[Test 1] Exécution de code simple...")
        engine = ExecutionEngine()
        result = engine.execute_code("print('Test réussi!')")
        
        if result['success'] and 'Test réussi!' in result['output']:
            print("  ✅ Test 1 réussi")
        else:
            print("  ❌ Test 1 échoué")
            return False
        
        # Test 2: Détection d'erreur
        print("[Test 2] Détection d'erreur...")
        result = engine.execute_code("x = 1 / 0")
        
        if not result['success'] and 'ZeroDivisionError' in result['error']:
            print("  ✅ Test 2 réussi")
        else:
            print("  ❌ Test 2 échoué")
            return False
        
        # Test 3: Validation de code
        print("[Test 3] Validation de syntaxe...")
        is_valid, _ = engine.validate_code("print('valide')")
        
        if is_valid:
            print("  ✅ Test 3 réussi")
        else:
            print("  ❌ Test 3 échoué")
            return False
        
        print("\n✅ Tous les tests du moteur d'exécution ont réussi!")
        return True
        
    except Exception as e:
        print(f"\n❌ Erreur lors du test: {e}")
        return False


def run_unit_tests():
    """Lance les tests unitaires avec pytest"""
    print_header("TESTS UNITAIRES")
    
    try:
        import pytest
        
        # Lancer pytest
        print("\nLancement de pytest...")
        exit_code = pytest.main([
            'tests/test_execution_engine.py',
            '-v',
            '--tb=short'
        ])
        
        if exit_code == 0:
            print("\n✅ Tous les tests unitaires ont réussi!")
            return True
        else:
            print("\n❌ Certains tests ont échoué")
            return False
            
    except ImportError:
        print("⚠️  pytest non installé, tests unitaires ignorés")
        return True


def print_summary(results):
    """Affiche un résumé des vérifications"""
    print_header("RÉSUMÉ")
    
    checks = {
        'Python': results.get('python', False),
        'Dépendances': results.get('dependencies', False),
        'Structure': results.get('structure', False),
        'Moteur d\'exécution': results.get('engine', False),
        'Tests unitaires': results.get('unit_tests', False),
    }
    
    for check, passed in checks.items():
        status = "✅" if passed else "❌"
        print(f"{status} {check}")
    
    all_passed = all(checks.values())
    
    print("\n" + "=" * 60)
    if all_passed:
        print("🎉 TOUT EST PRÊT ! Vous pouvez commencer à travailler.")
    else:
        print("⚠️  Certaines vérifications ont échoué.")
        print("   Corrigez les problèmes avant de continuer.")
    print("=" * 60)
    
    return all_passed


def main():
    """Fonction principale"""
    print("\n" + "🔍 " + "=" * 58)
    print("🔍  VÉRIFICATION DE L'INSTALLATION ET DES TESTS")
    print("🔍 " + "=" * 58)
    
    results = {}
    
    # Vérifications
    results['python'] = check_python_version()
    results['dependencies'] = check_dependencies()
    results['structure'] = check_project_structure()
    results['engine'] = test_execution_engine()
    results['unit_tests'] = run_unit_tests()
    
    # Résumé
    success = print_summary(results)
    
    # Code de sortie
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
