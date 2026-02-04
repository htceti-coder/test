import pytest
from src.execution_engine import ExecutionEngine

@pytest.fixture
def engine():
    """Fixture pour initialiser le moteur avant chaque test."""
    return ExecutionEngine(timeout=5, max_memory_mb=50)

def test_execute_success(engine):
    """Vérifie qu'un code simple s'exécute correctement."""
    code = "print('Hello World')"
    result = engine.execute_code(code)
    assert result['success'] is True
    assert "Hello World" in result['output']
    assert result['execution_time'] >= 0

def test_execute_syntax_error(engine):
    """Vérifie la capture des erreurs de syntaxe."""
    code = "print('Test"  # Erreur : guillemet et parenthèse manquants
    result = engine.execute_code(code)
    assert result['success'] is False
    assert "syntaxe" in result['error'].lower()

def test_execute_runtime_error(engine):
    """Vérifie la capture des erreurs d'exécution (ZeroDivision)."""
    code = "1 / 0"
    result = engine.execute_code(code)
    assert result['success'] is False
    assert "ZeroDivisionError" in result['error']

def test_execute_with_input(engine):
    """Vérifie la simulation de l'entrée utilisateur input()."""
    code = "name = input(); print(f'Hello {name}')"
    result = engine.execute_code(code, user_input="Sofiane")
    assert result['success'] is True
    assert "Hello Sofiane" in result['output']

def test_validate_code(engine):
    """Vérifie la fonction de validation de syntaxe seule."""
    valid_code = "x = 10"
    invalid_code = "x ="
    
    is_valid_1, _ = engine.validate_code(valid_code)
    is_valid_2, _ = engine.validate_code(invalid_code)
    
    assert is_valid_1 is True
    assert is_valid_2 is False

def test_history_and_stats(engine):
    """Vérifie que l'historique et les statistiques se mettent à jour."""
    # Exécuter un succès et un échec
    engine.execute_code("x = 1")
    engine.execute_code("1 / 0")
    
    stats = engine.get_stats()
    history = engine.get_history()
    
    assert stats['total_executions'] == 2
    assert stats['success_rate'] == 50.0
    assert len(history) == 2

def test_memory_limit_logic(engine):
    """
    Vérifie la logique de calcul de mémoire.
    Note: Le dépassement réel est difficile à tester de manière stable en CI,
    mais on vérifie que la valeur est calculée.
    """
    code = "x = [i for i in range(1000)]"
    result = engine.execute_code(code)
    assert 'memory_used' in result
    assert isinstance(result['memory_used'], float)
