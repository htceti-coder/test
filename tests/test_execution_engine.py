import pytest
from src.execution_engine import ExecutionEngine

@pytest.fixture
def engine():
    """Crée une instance par défaut du moteur pour chaque test."""
    return ExecutionEngine(timeout=5, max_memory_mb=128)

def test_execute_simple_code(engine):
    """Vérifie que le code valide s'exécute correctement."""
    code = "print('Test Réussi'); x = 10 + 20; print(x)"
    result = engine.execute_code(code)
    
    assert result['success'] is True
    assert "Test Réussi" in result['output']
    assert "30" in result['output']

def test_syntax_error(engine):
    """Vérifie la détection d'une erreur de syntaxe."""
    code = "def erreur_syntaxe(" # Parenthèse non fermée
    result = engine.execute_code(code)
    
    assert result['success'] is False
    assert "SyntaxError" in result['error']

def test_runtime_error(engine):
    """Vérifie la capture d'une exception à l'exécution (Division par zéro)."""
    code = "x = 1 / 0"
    result = engine.execute_code(code)
    
    assert result['success'] is False
    assert "ZeroDivisionError" in result['error']

def test_security_restriction_import(engine):
    """Vérifie que RestrictedPython bloque les imports dangereux (os, sys)."""
    code = "import os; os.listdir('/')"
    result = engine.execute_code(code)
    
    # Le moteur doit soit échouer à l'import, soit lever une erreur de sécurité
    assert result['success'] is False
    assert ("ImportError" in result['error'] or "not allowed" in result['error'].lower())

def test_security_restriction_builtins(engine):
    """Vérifie que l'accès à __builtins__ est restreint."""
    code = "open('/etc/passwd', 'r')"
    result = engine.execute_code(code)
    
    assert result['success'] is False
    assert "NameError" in result['error'] # 'open' ne devrait pas être défini

def test_timeout_limit(engine):
    """Vérifie que le moteur interrompt un code trop long (boucle infinie)."""
    # On réduit le timeout pour ce test spécifique
    short_engine = ExecutionEngine(timeout=1)
    code = "while True: pass"
    result = short_engine.execute_code(code)
    
    assert result['success'] is False
    assert "Timeout" in result['error']
