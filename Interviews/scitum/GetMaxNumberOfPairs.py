"""
Problema 1 (2 horas)
Pedro esta por irse de viaje, Pero antes necesita revisar el estado de sus calcetines. Cada calcetín
tiene su propio color. Pedro quiere llevar el mayor número posible de pares de calcetines limpios,
(los pares deben ser del mismo color).
Los calcetines están divididos en 2 cajones, sucios y limpios. Pedro únicamente tiene tiempo para
un ciclo de lavado y su lavadora puede lavar un máximo de K calcetines. El quiere elegir los
calcetines para lavar de tal forma que después de lavar el tenga el máximo número de pares limpios
del mismo color. Es posible que algunos calcetines no encuentren su par, porque Pedro pudo haber
perdido calcetines anteriormente.
Pedro tiene exactamente N calcetines limpios y M calcetines sucios, que están descritos en los
arreglos L y S respectivamente. El color de los calcetines está representado por enteros (números
iguales representan colores iguales).

Por ejemplo, si tuviéramos 4 calcetines limpios y 5
calcetines sucios:
Limpios
Sucios

Si la lavadora de Pedro puede limpiar hasta K = 2 calcetines, entonces el puede conseguir un
máximo de 3 pares limpios de calcetines. Él puede lavar un calcetín rojo y un calcetín verde,
indicados con el número 1 y 2 respectivamente. Entonces conseguirá un par rojo y uno verde de
calcetines limpios.
Escriba una función solucion(K,L,S)
que dado un entero K (el máximo de calcetines que puede lavar la lavadora), dos arreglos L y S
(conteniendo la representación de colores de N calcetines limpios y M calcetines sucios
respectivamente), devuelva el máximo número de pares que Pedro puede llevar en su viaje.
Por ejemplo, dado K = 2, L= [1, 2, 1, 1] y S=[1, 4, 3, 2, 4] la función deberá devolver 3, como se
explicó anteriormente
Asuma que
• K es un entero en el rango [0...50]
• cada elemento de los arreglos L y S es un entero en el rango [1..50]
• L y S no están vacíos y que cada uno contiene como máximo 50 elementos.

NOTA: Se espera que la solución no haga uso de librerías externas.
"""

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