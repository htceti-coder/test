# Membre 2
import traceback
import sys
import io

class Debugger:
    """
    Module 2: Analyzes execution results and provides detailed debugging info.
    """
    
    @staticmethod
    def analyze_error(execution_result):
        """
        Takes the dictionary result from ExecutionEngine and enriches it.
        """
        if execution_result['success']:
            return {"status": "Clean", "message": "No errors detected."}

        error_msg = execution_result.get('error', 'Unknown Error')
        
        # Basic Error Categorization
        error_type = error_msg.split(':')[0]
        
        analysis = {
            "status": "Error Detected",
            "error_type": error_type,
            "raw_message": error_msg,
            "suggestions": Debugger._get_suggestions(error_type, error_msg),
        }
        return analysis

    @staticmethod
    def _get_suggestions(error_type, message):
        """
        Provides helpful tips based on common Python errors.
        """
        suggestions = {
            "SyntaxError": "Check for missing colons (:), unclosed parentheses, or quotes.",
            "NameError": "You are using a variable that hasn't been defined yet.",
            "TypeError": "You are performing an operation on incompatible types (e.g., adding string to int).",
            "IndentationError": "Check your spaces or tabs. Python is strict about alignment.",
            "ImportError": "The module you are trying to use is not installed or spelled incorrectly."
        }
        return suggestions.get(error_type, "Check the traceback logs for the exact line number.")

    def format_debug_report(self, analysis):
        """
        Returns a human-readable string for the collaboration team.
        """
        report = f"--- DEBUG REPORT ---\n"
        report += f"Type: {analysis.get('error_type')}\n"
        report += f"Details: {analysis.get('raw_message')}\n"
        report += f"Suggestion: {analysis.get('suggestions')}\n"
        report += "--------------------"
        return report
