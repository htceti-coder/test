import pytest
import time
import sys
import io
import runpy
from src.execution_engine import ExecutionEngine, demo

@pytest.fixture
def engine():
    """Fixture to provide a clean ExecutionEngine instance."""
    return ExecutionEngine(timeout=2, max_memory_mb=50)

class TestExecutionEngine:
    
    ## --- Logic Tests ---

    def test_successful_execution(self, engine):
        code = "print('Hello World'); x = 5 + 5; print(x)"
        result = engine.execute_code(code)
        assert result['success'] is True
        assert "10" in result['output']

    def test_input_simulation(self, engine):
        code = "name = input(); print(f'Hello {name}')"
        result = engine.execute_code(code, user_input="Sofiane")
        assert "Hello Sofiane" in result['output']

    def test_syntax_error(self, engine):
        code = "if True print('Missing colon')"
        result = engine.execute_code(code)
        assert result['success'] is False
        assert "Erreur de syntaxe" in result['error']

    def test_runtime_error(self, engine):
        code = "1 / 0"
        result = engine.execute_code(code)
        assert result['success'] is False
        assert "ZeroDivisionError" in result['error']

    def test_timeout_violation(self, engine):
        # Setting a very short timeout to ensure the catch
        engine.timeout = 0.1
        code = "import time; time.sleep(0.5)"
        result = engine.execute_code(code)
        assert result['success'] is False
        assert "Exécution interrompue" in result['error']

    def test_memory_limit_trigger(self, engine):
        """Forces a MemoryError by setting limit to near zero."""
        engine.max_memory_mb = -1 
        code = "x = [1] * 100"
        result = engine.execute_code(code)
        assert result['success'] is False
        assert "Limite mémoire dépassée" in result['error']

    def test_validate_code(self, engine):
        assert engine.validate_code("print(1)")[0] is True
        assert engine.validate_code("print(1")[0] is False

    def test_history_and_stats(self, engine):
        # Test empty stats first
        empty_stats = ExecutionEngine().get_stats()
        assert empty_stats['total_executions'] == 0
        
        # Fill history
        engine.execute_code("print(1)")
        assert len(engine.get_history(limit=1)) == 1
        stats = engine.get_stats()
        assert stats['total_executions'] == 1

    def test_history_overflow(self, engine):
        """Triggers the pop(0) logic for history > 100."""
        for i in range(105):
            engine._save_to_history(f"code_{i}", {"success": True})
        assert len(engine.execution_history) == 100

    def test_stderr_capture(self, engine):
        code = "import sys; sys.stderr.write('err_msg')"
        result = engine.execute_code(code)
        assert "err_msg" in result['output']

    def test_demo_function(self, monkeypatch):
        """
        Executes the demo() function. 
        We mock stdout so it doesn't clutter the terminal.
        """
        monkeypatch.setattr(sys, 'stdout', io.StringIO())
        demo()

    def test_force_main_block(self, monkeypatch):
            """
            Forces coverage of the 'if __name__ == "__main__":' line and the demo() call.
            Using runpy.run_module allows us to simulate the script execution.
            """
            # We redirect stdout so the demo output doesn't flood the test console
            monkeypatch.setattr(sys, 'stdout', io.StringIO())
            
            try:
                runpy.run_module("src.execution_engine", run_name="__main__")
            except SystemExit:
                pass
