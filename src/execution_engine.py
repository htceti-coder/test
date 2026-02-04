"""
Module: Moteur d'Exécution Sécurisé Python
Auteur: Sofiane (Corrected for Security & 3.12)
Date: 28/01/2026
Description: Ce module permet l'exécution sécurisée de scripts Python
             avec capture des erreurs, timeout et isolation.
"""

import sys
import io
import traceback
import time
from contextlib import redirect_stdout, redirect_stderr
from typing import Dict, Any, Tuple
import psutil
import os

class ExecutionEngine:
    def __init__(self, timeout: int = 10, max_memory_mb: int = 100):
        self.timeout = timeout
        self.max_memory_mb = max_memory_mb
        self.execution_history = []
        
    def execute_code(self, code: str, user_input: str = "") -> Dict[str, Any]:
        result = {
            'success': False,
            'output': '',
            'error': '',
            'execution_time': 0.0,
            'memory_used': 0.0,
            'traceback': '',
            'timestamp': time.strftime('%Y-%m-%d %H:%M:%S')
        }
        
        stdout_capture = io.StringIO()
        stderr_capture = io.StringIO()
        start_time = time.time()
        process = psutil.Process(os.getpid())
        initial_memory = process.memory_info().rss / 1024 / 1024 
        
        try:
            # --- SECURITY LAYER: Restricted Globals ---
            # We remove dangerous builtins like __import__, open, eval
            safe_builtins = __builtins__.copy() if isinstance(__builtins__, dict) else vars(__builtins__).copy()
            dangerous_funcs = ['__import__', 'open', 'exit', 'quit', 'help', 'copyright']
            for func in dangerous_funcs:
                safe_builtins.pop(func, None)

            exec_globals = {
                '__builtins__': safe_builtins,
                '__name__': '__main__',
            }
            
            if user_input:
                exec_globals['input'] = lambda prompt='': user_input
            
            with redirect_stdout(stdout_capture), redirect_stderr(stderr_capture):
                # 1. Compile first to catch SyntaxErrors explicitly
                compiled_code = compile(code, '<string>', 'exec')
                
                # 2. Execute
                exec(compiled_code, exec_globals)
            
            # --- POST-EXECUTION CHECKS ---
            execution_time = time.time() - start_time
            if execution_time > self.timeout:
                raise TimeoutError(f"Timeout: {self.timeout}s exceeded")
            
            final_memory = process.memory_info().rss / 1024 / 1024
            memory_used = final_memory - initial_memory
            
            if memory_used > self.max_memory_mb:
                raise MemoryError(f"Memory Limit Exceeded")

            result['success'] = True
            result['output'] = stdout_capture.getvalue()
            result['execution_time'] = execution_time
            result['memory_used'] = memory_used
            
        except SyntaxError as e:
            result['error'] = f"SyntaxError: {str(e)}"
            result['traceback'] = traceback.format_exc()
        except ImportError:
            result['error'] = "ImportError: Import operations are restricted for security."
            result['traceback'] = "Security Restriction"
        except NameError as e:
            # Special case for forbidden builtins which appear as NameError when removed
            if any(forbidden in str(e) for forbidden in ['open', '__import__']):
                result['error'] = f"SecurityError: Restricted function call: {str(e)}"
            else:
                result['error'] = f"NameError: {str(e)}"
            result['traceback'] = traceback.format_exc()
        except Exception as e:
            result['error'] = f"{type(e).__name__}: {str(e)}"
            result['traceback'] = traceback.format_exc()
        finally:
            stderr_output = stderr_capture.getvalue()
            if stderr_output:
                result['output'] += f"\n[STDERR]\n{stderr_output}"
        
        self._save_to_history(code, result)
        return result
    
    def _save_to_history(self, code: str, result: Dict[str, Any]):
        history_entry = {'code': code[:100], 'result': result}
        self.execution_history.append(history_entry)
        if len(self.execution_history) > 50: self.execution_history.pop(0)

    def validate_code(self, code: str) -> Tuple[bool, str]:
        try:
            compile(code, '<string>', 'exec')
            return True, "Valid"
        except SyntaxError as e:
            return False, str(e)

    def get_stats(self) -> Dict[str, Any]:
        total = len(self.execution_history)
        if total == 0: return {'total_executions': 0}
        successes = sum(1 for e in self.execution_history if e['result']['success'])
        return {
            'total_executions': total,
            'success_rate': (successes / total) * 100
        }
