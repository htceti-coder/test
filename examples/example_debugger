"""
Exemple d'utilisation du Module de Debugging
Auteur: Ilies
Date: 04/02/2026

Ce fichier montre comment utiliser le debugger pour analyser
des erreurs et fournir des suggestions de correction.
"""

import sys
import os

# Ajouter le chemin du module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.debugger import Debugger

def example_1_analyze_syntax_error():
    """Exemple 1: Analyse d'une erreur de syntaxe"""
    print("\n" + "="*60)
    print("EXEMPLE 1: Analyse d'une erreur de syntaxe")
    print("="*60)
    
    debugger = Debugger()
    mock_result = {
        'success': False,
        'error': 'SyntaxError: invalid syntax (line 5)',
        'output': ''
    }
    
    analysis = debugger.analyze(mock_result)
    print(debugger.format_report(analysis))

def example_2_analyze_runtime_error():
    """Exemple 2: Analyse d'une erreur d'exécution (ZeroDivision)"""
    print("\n" + "="*60)
    print("EXEMPLE 2: Analyse d'une erreur d'exécution")
    print("="*60)
    
    debugger = Debugger()
    mock_result = {
        'success': False,
        'error': 'ZeroDivisionError: division by zero (line 10)',
        'output': ''
    }
    
    analysis = debugger.analyze(mock_result)
    print(debugger.format_report(analysis))

def example_3_unknown_error():
    """Exemple 3: Gestion d'une erreur inconnue"""
    print("\n" + "="*60)
    print("EXEMPLE 3: Gestion d'une erreur inconnue")
    print("="*60)
    
    debugger = Debugger()
    mock_result = {
        'success': False,
        'error': 'CustomHardwareError: device not found',
        'output': ''
    }
    
    analysis = debugger.analyze(mock_result)
    print(debugger.format_report(analysis))

def main():
    print("\n DÉMONSTRATIONS DU MODULE DE DEBUGGING")
    example_1_analyze_syntax_error()
    example_2_analyze_runtime_error()
    example_3_unknown_error()
    print("\n Démonstrations de Ilies terminées!\n")

if __name__ == "__main__":
    main()
