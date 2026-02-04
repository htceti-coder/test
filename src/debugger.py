import pytest
from src.debugger import Debugger

@pytest.fixture
def debugger():
    """Fixture to provide a clean Debugger instance for each test."""
    return Debugger()

def test_analyze_success(debugger):
    """Test that a successful execution result returns the correct status."""
    mock_result = {
        'success': True,
        'output': 'Hello World',
        'error': None
    }
    analysis = debugger.analyze(mock_result)
    assert analysis["status"] == "SUCCESS"
    assert analysis["analysis"] is None

def test_analyze_syntax_error(debugger):
    """Test analysis of a SyntaxError with a line number."""
    mock_result = {
        'success': False,
        'error': 'SyntaxError: invalid syntax (line 3)',
        'output': ''
    }
    analysis = debugger.analyze(mock_result)
    assert analysis["status"] == "FAILED"
    assert analysis["error_type"] == "SyntaxError"
    assert analysis["line_number"] == 3
    assert "colons" in analysis["suggestion"]
    assert analysis["severity"] == "High"

def test_analyze_runtime_error(debugger):
    """Test analysis of a ZeroDivisionError."""
    mock_result = {
        'success': False,
        'error': 'ZeroDivisionError: division by zero on line 10',
        'output': ''
    }
    analysis = debugger.analyze(mock_result)
    assert analysis["error_type"] == "ZeroDivisionError"
    assert analysis["line_number"] == 10
    assert "mathematically impossible" in analysis["suggestion"]
    assert analysis["severity"] == "Medium"

def test_unknown_error(debugger):
    """Test that unknown errors get a default suggestion."""
    mock_result = {
        'success': False,
        'error': 'MyCustomError: something went wrong',
        'output': ''
    }
    analysis = debugger.analyze(mock_result)
    assert analysis["error_type"] == "MyCustomError"
    assert "official documentation" in analysis["suggestion"]

def test_format_report(debugger):
    """Test that the report formatting produces a visible string."""
    analysis = {
        "status": "FAILED",
        "error_type": "NameError",
        "line_number": 5,
        "message": "name 'x' is not defined",
        "suggestion": "Check for typos.",
        "severity": "Medium"
    }
    report = debugger.format_report(analysis)
    assert "DEBUGGER ANALYSIS" in report
    assert "NameError" in report
    assert "Line 5" in report
    assert "Check for typos" in report
