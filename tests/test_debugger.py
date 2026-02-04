import pytest
from src.debugger import Debugger

@pytest.fixture
def db():
    return Debugger()

def test_analyze_success(db):
    res = {'success': True, 'output': 'Hi'}
    analysis = db.analyze(res)
    assert analysis["status"] == "SUCCESS"
    assert "valide" in db.format_report(analysis)

def test_analyze_known_error(db):
    res = {'success': False, 'error': 'SyntaxError: invalid syntax (line 5)'}
    analysis = db.analyze(res)
    assert analysis["error_type"] == "SyntaxError"
    assert analysis["line_number"] == 5
    assert "deux-points" in analysis["suggestion"]
    assert "DEBUGGING" in db.format_report(analysis)

def test_analyze_unknown_error(db):
    res = {'success': False, 'error': 'RuntimeError: unknown issue'}
    analysis = db.analyze(res)
    assert "documentation" in analysis["suggestion"]
    assert analysis["line_number"] == "Unknown"

def test_formatting_failure(db):
    analysis = {
        "status": "FAILED", "error_type": "NameError", "line_number": 1,
        "message": "x not defined", "suggestion": "Check typos", "severity": "Medium"
    }
    report = db.format_report(analysis)
    assert "NameError" in report
