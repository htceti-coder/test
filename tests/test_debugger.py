import pytest
from src.debugger import Debugger

def test_analyze_syntax_error():
    fake_result = {
        'success': False,
        'error': 'SyntaxError: invalid syntax',
        'output': ''
    }
    debugger = Debugger()
    analysis = debugger.analyze_error(fake_result)
    assert analysis['error_type'] == 'SyntaxError'
    assert "missing colons" in analysis['suggestions']

def test_analyze_success():
    fake_result = {'success': True, 'output': 'Hello'}
    debugger = Debugger()
    analysis = debugger.analyze_error(fake_result)
    assert analysis['status'] == 'Clean'
