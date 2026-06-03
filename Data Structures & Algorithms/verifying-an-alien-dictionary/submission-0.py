from typing import List

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # Mapa letra -> posición en el alfabeto alien
        letters = {char: i for i, char in enumerate(order)}
        
        # Recorrer pares de palabras consecutivas
        for i in range(len(words) - 1):
            prev = words[i]
            current = words[i + 1]
            
            # Buscar la primera letra donde difieren
            for j in range(len(prev)):
                # Caso: prev es más larga y current es su prefijo -> mal orden
                # Ej: ["apple", "app"] -> False
                if j >= len(current):
                    return False
                
                if prev[j] != current[j]:
                    # Primera diferencia: comparar con el orden alien
                    if letters[prev[j]] > letters[current[j]]:
                        return False
                    # Si está bien, ya decidimos este par, salimos
                    break
        
        return True