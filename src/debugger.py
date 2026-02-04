import sys
import re
from loguru import logger

# Configure loguru to write to the logs folder
logger.add("logs/debugger.log", rotation="500 MB", level="INFO")

class Debugger:
    """
    Module 2: Analyzes execution results, identifies error types, 
    and provides human-readable suggestions.
    """

    def __init__(self):
        self.common_fixes = {
            "SyntaxError": "Check for missing colons (:), mismatched brackets, or unclosed quotes.",
            "NameError": "A variable name is misspelled or has not been defined yet.",
            "ZeroDivisionError": "You are dividing by zero. Add a check (if divisor != 0).",
            "TypeError": "Data types don't match (e.g., adding a string to an integer).",
            "IndentationError": "Check your spaces/tabs. Python requires consistent indentation.",
            "IndexError": "You're trying to access a list index that doesn't exist.",
            "KeyError": "The key you're looking for isn't in the dictionary."
        }

    def analyze_error(self, execution_result):
        """
        Parses the dictionary output from the ExecutionEngine.
        """
        if execution_result.get('success'):
            logger.info("Code executed successfully. No debugging needed.")
            return {"status": "Clean", "message": "Success"}

        raw_error = execution_result.get('error', "UnknownError: No details provided.")
        
        # Extract Error Type (e.g., "ValueError")
        error_type_match = re.match(r"^(\w+):", raw_error)
        error_type = error_type_match.group(1) if error_type_match else "UnknownError"

        # Extract Line Number (if present in traceback)
        line_match = re.search(r"line (\d+)", raw_error)
        line_no = line_match.group(1) if line_match else "Unknown"

        analysis = {
            "status": "Error",
            "type": error_type,
            "line": line_no,
            "message": raw_error,
            "suggestion": self.common_fixes.get(error_type, "Consult Python documentation for this specific error.")
        }

        # Log the error for Module 4 (Documentation/History)
        logger.error(f"Debug Analysis: {error_type} at line {line_no} | Msg: {raw_error}")
        
        return analysis

    def get_rich_report(self, analysis):
        """Returns a formatted string for the user interface."""
        if analysis['status'] == "Clean":
            return "✅ Code passed all checks."
        
        return (
            f"\n--- 🔍 DEBUG REPORT ---\n"
            f"❌ Error Type: {analysis['type']}\n"
            f"📍 Location  : Line {analysis['line']}\n"
            f"📝 Message   : {analysis['message']}\n"
            f"💡 Suggestion: {analysis['suggestion']}\n"
            f"----------------------"
        )
