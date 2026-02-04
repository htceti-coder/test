import pytest
from src.debugger import Debugger

def test_syntax_error_analysis():
    debugger = Debugger()
    mock_result = {
        'success': False,
        'error': 'SyntaxError: invalid syntax (line 2)',
        'output': ''
    }
    analysis = debugger.analyze_error(mock_result)
    assert analysis['type'] == 'SyntaxError'
    assert analysis['line'] == '2'
    assert "colons" in analysis['suggestion']

def test_success_case():
    debugger = Debugger()
    mock_result = {'success': True, 'output': 'Hello', 'error': None}
    analysis = debugger.analyze_error(mock_result)
    assert analysis['status'] == 'Clean'
