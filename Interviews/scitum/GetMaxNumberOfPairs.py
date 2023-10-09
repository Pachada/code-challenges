from collections import Counter
from typing import List

# O(n + m) where n is the len of l and m is the len of s | O(n + m) space 
def get_total_pairs(k: int, l: List[int], s: List[int]) -> int:
    # Utilizamos Counter para contar la frecuencia de cada color en los calcetines limpios (l) y sucios (s)
    clean_count = Counter(l)
    dirty_count = Counter(s)
    
    total_pairs = 0
    
    # Revizamos cuando pares podemos formar con los calcetines limpios
    for color, quantity in clean_count.items():
        clean_pairs = quantity // 2
        total_pairs += clean_pairs
        clean_count[color] %= 2
    
    # Si tenemos calcetines limpios sin par, intentamos formar pares con calcetines sucios del mismo color.
    # Hacemos esto hasta que no tengamos más pares o ya no tengamos espacio en la lavadora
    for color in clean_count:
        while clean_count[color] > 0 and dirty_count.get(color, 0) > 0 and k > 0:
            total_pairs += 1
            k -= 1
            dirty_count[color] -= 1
            clean_count[color] -= 1
    
    # Si todavía tenemos capacidad en la lavadora, lavamos pares sucios
    if k >= 2:
        for color in dirty_count:
            while dirty_count[color] >= 2 and k >= 2:
                total_pairs += 1
                k -= 2
                dirty_count[color] -= 2
    
    return total_pairs 


k = 2
l = [1, 1]
s = [2, 3, 3]
print(get_total_pairs(k, l, s))

k = 2
l = [1, 2, 1, 1]
s = [1, 4, 3, 2, 4]
print(get_total_pairs(k, l, s))