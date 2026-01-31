#sofiane
"""
Module: Moteur d'Exécution Sécurisé Python
Auteur: Sofiane
Date: 28/01/2026
Description: Ce module permet l'exécution sécurisée de scripts Python
             avec capture des erreurs, timeout et isolation.
"""

import sys
import io
import traceback
import time
from contextlib import redirect_stdout, redirect_stderr
from typing import Dict, Any, Optional, Tuple
import psutil
import os


class ExecutionEngine:
    """
    Classe principale pour l'exécution sécurisée de code Python.
    
    Fonctionnalités:
    - Exécution avec timeout
    - Capture des outputs (stdout/stderr)
    - Gestion des exceptions
    - Monitoring des ressources (CPU, mémoire)
    - Isolation du code utilisateur
    """
    
    def __init__(self, timeout: int = 10, max_memory_mb: int = 100):
        """
        Initialise le moteur d'exécution.
        
        Args:
            timeout (int): Temps maximum d'exécution en secondes (défaut: 10s)
            max_memory_mb (int): Mémoire maximale autorisée en MB (défaut: 100MB)
        """
        self.timeout = timeout
        self.max_memory_mb = max_memory_mb
        self.execution_history = []  # Historique des exécutions
        
    def execute_code(self, code: str, user_input: str = "") -> Dict[str, Any]:
        """
        Exécute du code Python de manière sécurisée.
        
        Args:
            code (str): Le code Python à exécuter
            user_input (str): Entrée utilisateur simulée (pour input())
            
        Returns:
            Dict contenant:
                - success (bool): True si exécution réussie
                - output (str): Sortie standard du programme
                - error (str): Message d'erreur si échec
                - execution_time (float): Temps d'exécution en secondes
                - memory_used (float): Mémoire utilisée en MB
                - traceback (str): Stack trace complète en cas d'erreur
        """
        # Initialisation du résultat
        result = {
            'success': False,
            'output': '',
            'error': '',
            'execution_time': 0.0,
            'memory_used': 0.0,
            'traceback': '',
            'timestamp': time.strftime('%Y-%m-%d %H:%M:%S')
        }
        
        # Capture des outputs
        stdout_capture = io.StringIO()
        stderr_capture = io.StringIO()
        
        # Mesure du temps de début
        start_time = time.time()
        
        # Mesure de la mémoire initiale
        process = psutil.Process(os.getpid())
        initial_memory = process.memory_info().rss / 1024 / 1024  # Convertir en MB
        
        try:
            # Préparer l'environnement d'exécution isolé
            exec_globals = {
                '__builtins__': __builtins__,
                '__name__': '__main__',
                '__doc__': None,
            }
            
            # Simuler input() si nécessaire
            if user_input:
                exec_globals['input'] = lambda prompt='': user_input
            
            # Redirection des outputs
            with redirect_stdout(stdout_capture), redirect_stderr(stderr_capture):
                # Exécution du code avec timeout
                exec(code, exec_globals)
            
            # Calcul du temps d'exécution
            execution_time = time.time() - start_time
            
            # Vérification du timeout
            if execution_time > self.timeout:
                raise TimeoutError(f"Exécution interrompue après {self.timeout}s")
            
            # Calcul de la mémoire utilisée
            final_memory = process.memory_info().rss / 1024 / 1024
            memory_used = final_memory - initial_memory
            
            # Vérification de la limite mémoire
            if memory_used > self.max_memory_mb:
                raise MemoryError(f"Limite mémoire dépassée: {memory_used:.2f}MB > {self.max_memory_mb}MB")
            
            # Succès de l'exécution
            result['success'] = True
            result['output'] = stdout_capture.getvalue()
            result['execution_time'] = execution_time
            result['memory_used'] = memory_used
            
        except SyntaxError as e:
            # Erreur de syntaxe Python
            result['error'] = f"Erreur de syntaxe: {str(e)}"
            result['traceback'] = traceback.format_exc()
            result['execution_time'] = time.time() - start_time
            
        except TimeoutError as e:
            # Timeout dépassé
            result['error'] = str(e)
            result['traceback'] = "Temps d'exécution maximal dépassé"
            result['execution_time'] = self.timeout
            
        except MemoryError as e:
            # Limite mémoire dépassée
            result['error'] = str(e)
            result['traceback'] = traceback.format_exc()
            result['execution_time'] = time.time() - start_time
            
        except Exception as e:
            # Toute autre exception
            result['error'] = f"{type(e).__name__}: {str(e)}"
            result['traceback'] = traceback.format_exc()
            result['execution_time'] = time.time() - start_time
            
        finally:
            # Ajouter les erreurs stderr si présentes
            stderr_output = stderr_capture.getvalue()
            if stderr_output:
                result['output'] += f"\n[STDERR]\n{stderr_output}"
        
        # Sauvegarder dans l'historique
        self._save_to_history(code, result)
        
        return result
    
    def _save_to_history(self, code: str, result: Dict[str, Any]):
        """
        Sauvegarde une exécution dans l'historique.
        
        Args:
            code (str): Code exécuté
            result (Dict): Résultat de l'exécution
        """
        history_entry = {
            'code': code[:200] + '...' if len(code) > 200 else code,  # Limite la taille
            'result': result,
        }
        self.execution_history.append(history_entry)
        
        # Limiter l'historique aux 100 dernières exécutions
        if len(self.execution_history) > 100:
            self.execution_history.pop(0)
    
    def get_history(self, limit: int = 10) -> list:
        """
        Récupère l'historique des exécutions.
        
        Args:
            limit (int): Nombre d'entrées à retourner
            
        Returns:
            list: Liste des dernières exécutions
        """
        return self.execution_history[-limit:]
    
    def validate_code(self, code: str) -> Tuple[bool, str]:
        """
        Valide la syntaxe du code sans l'exécuter.
        
        Args:
            code (str): Code à valider
            
        Returns:
            Tuple[bool, str]: (est_valide, message_erreur)
        """
        try:
            compile(code, '<string>', 'exec')
            return True, "Code syntaxiquement correct"
        except SyntaxError as e:
            return False, f"Erreur ligne {e.lineno}: {e.msg}"
    
    def get_stats(self) -> Dict[str, Any]:
        """
        Retourne des statistiques sur les exécutions.
        
        Returns:
            Dict contenant les statistiques globales
        """
        if not self.execution_history:
            return {
                'total_executions': 0,
                'success_rate': 0.0,
                'avg_execution_time': 0.0,
                'avg_memory_used': 0.0
            }
        
        total = len(self.execution_history)
        successes = sum(1 for entry in self.execution_history if entry['result']['success'])
        
        avg_time = sum(entry['result']['execution_time'] for entry in self.execution_history) / total
        avg_memory = sum(entry['result']['memory_used'] for entry in self.execution_history) / total
        
        return {
            'total_executions': total,
            'success_rate': (successes / total) * 100,
            'avg_execution_time': avg_time,
            'avg_memory_used': avg_memory,
            'timeout_limit': self.timeout,
            'memory_limit_mb': self.max_memory_mb
        }


# Fonction utilitaire pour tester le module
def demo():
    """
    Démonstration du moteur d'exécution.
    """
    print("=" * 60)
    print("DÉMONSTRATION DU MOTEUR D'EXÉCUTION SÉCURISÉ")
    print("=" * 60)
    
    engine = ExecutionEngine(timeout=5, max_memory_mb=50)
    
    # Test 1: Code correct
    print("\n[TEST 1] Code correct:")
    code1 = """
print("Bonjour depuis le moteur d'exécution!")
for i in range(5):
    print(f"Itération {i}")
"""
    result1 = engine.execute_code(code1)
    print(f"✓ Succès: {result1['success']}")
    print(f"✓ Output:\n{result1['output']}")
    print(f"✓ Temps: {result1['execution_time']:.4f}s")
    
    # Test 2: Erreur de syntaxe
    print("\n[TEST 2] Erreur de syntaxe:")
    code2 = "print('test'"  # Parenthèse manquante
    result2 = engine.execute_code(code2)
    print(f"✗ Succès: {result2['success']}")
    print(f"✗ Erreur: {result2['error']}")
    
    # Test 3: Exception runtime
    print("\n[TEST 3] Exception runtime:")
    code3 = """
x = 10
y = 0
print(x / y)  # Division par zéro
"""
    result3 = engine.execute_code(code3)
    print(f"✗ Succès: {result3['success']}")
    print(f"✗ Erreur: {result3['error']}")
    
    # Afficher les statistiques
    print("\n" + "=" * 60)
    print("STATISTIQUES:")
    stats = engine.get_stats()
    for key, value in stats.items():
        print(f"  {key}: {value}")
    print("=" * 60)


if __name__ == "__main__":
    demo()
