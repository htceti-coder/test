# examples/demo_debugger.py
import sys
import os

# Ensure the src directory is in the path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.execution_engine import ExecutionEngine
from src.debugger import Debugger

def run_debug_demo():
    engine = ExecutionEngine()
    debugger = Debugger()

    # --- SCENARIO 1: A Syntax Error (The most common beginner error) ---
    print("\n--- Scenario 1: Syntax Error ---")
    code_with_syntax_error = """
def hello()
    print("Missing colon after function definition")
"""
    result = engine.execute_code(code_with_syntax_error)
    analysis = debugger.analyze_error(result)
    print(debugger.format_debug_report(analysis))

    # --- SCENARIO 2: A Runtime Error (ZeroDivision) ---
    print("\n--- Scenario 2: Runtime Error (Division by Zero) ---")
    code_with_runtime_error = """
x = 10
y = 0
result = x / y
"""
    result = engine.execute_code(code_with_runtime_error)
    analysis = debugger.analyze_error(result)
    print(debugger.format_debug_report(analysis))

    # --- SCENARIO 3: A Successful Run ---
    print("\n--- Scenario 3: Success ---")
    clean_code = "print('Everything is working fine!')"
    result = engine.execute_code(clean_code)
    analysis = debugger.analyze_error(result)
    print(f"Status: {analysis['status']}")
    print(f"Output: {result['output']}")

if __name__ == "__main__":
    run_debug_demo()
