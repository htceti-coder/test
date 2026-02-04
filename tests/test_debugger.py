import pytest
from src.debugger import Debugger

@pytest.fixture
def db():
    return Debugger()

# 1. Test Success Path
def test_analyze_success(db):
    mock_result = {'success': True, 'output': 'Hello', 'error': None}
    analysis = db.analyze(mock_result)
    assert analysis["status"] == "SUCCESS"
    # Test the formatting for success too
    report = db.format_report(analysis)
    assert "perfectly" in report

# 2. Test Known Error (SyntaxError)
def test_analyze_syntax_error(db):
    mock_result = {
        'success': False, 
        'error': 'SyntaxError: invalid syntax (line 5)', 
        'output': ''
    }
    analysis = db.analyze(mock_result)
    assert analysis["error_type"] == "SyntaxError"
    assert analysis["line_number"] == 5
    assert "colons" in analysis["suggestion"]
    # Test the formatting for failure
    report = db.format_report(analysis)
    assert "DEBUGGER ANALYSIS" in report
    assert "Line 5" in report

# 3. Test Unknown Error (The "Missed" logic)
def test_analyze_unknown_error(db):
    mock_result = {
        'success': False, 
        'error': 'SuperRareError: something weird happened', 
        'output': ''
    }
    analysis = db.analyze(mock_result)
    assert analysis["error_type"] == "SuperRareError"
    # This checks the fallback suggestion line
    assert "official documentation" in analysis["suggestion"]

# 4. Test Error with no line number (Regex fallback)
def test_error_no_line(db):
    mock_result = {
        'success': False, 
        'error': 'ValueError: bad value', 
        'output': ''
    }
    analysis = db.analyze(mock_result)
    assert analysis["line_number"] == "Unknown"
