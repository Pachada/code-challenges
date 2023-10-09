from collections import defaultdict
from typing import List

NEW_FISH_STARTING_TIMER = 8
FATHER_FISH_STARTING_TIMER = 6
FISH_READY_TO_BE_FATHER_TIMER = -1


class Ocean:
    def __init__(self, starting_fishes_counters: List[int], target_days: List[int]) -> None:

        # Día actual en la simulación
        self.current_day = 0

        # Días en los que se quiere saber la cantidad de peces
        self.target_days = target_days

        # Llevamos el registro de la cuenta de los peces en un dict para que cada día
        # solo hagamos sumas y restas de la cuenta de los peces y no estamos guardando
        # en memoria los mil millones de peces que pueden haber despues de x días
        # la llave es la cuenta actual y el valor es el número de peceses con esa cuenta
        self.fishes_count_by_timer = defaultdict(int)

        # Inicializamos la cuenta de los peces con los valores iniciales
        for fish_counter in starting_fishes_counters:
            self.fishes_count_by_timer[fish_counter] += 1

        print(f"Estado Inicial: Hay {sum(self.fishes_count_by_timer.values())} peces")

    def new_day(self):
        # Copia del contador actual para hacer las modificaciones del día
        new_fishes_count_by_timer = self.fishes_count_by_timer.copy()

        # Actualizamos los contadores de cada pez
        for timer, count in self.fishes_count_by_timer.items():
            # Le restamos el contador a los peces
            new_fishes_count_by_timer[timer - 1] += count

            # Despues de actualizar el contador de los peces le restamos al timer los peces actualizados
            new_fishes_count_by_timer[timer] -= count

        if fish_that_spawn_new_fishes_count := new_fishes_count_by_timer.get(FISH_READY_TO_BE_FATHER_TIMER):
            # Agrega nuevos peces con el contador en 8
            new_fishes_count_by_timer[NEW_FISH_STARTING_TIMER] += fish_that_spawn_new_fishes_count
            # Reinicia el contador a 6 para los peces "padres"
            new_fishes_count_by_timer[FATHER_FISH_STARTING_TIMER] += fish_that_spawn_new_fishes_count
            # Reiniciamos el contador de peces que estan listos para ser "padres"
            new_fishes_count_by_timer[FISH_READY_TO_BE_FATHER_TIMER] = 0  

        # Actualizamos el contador del Ocean con la nueva cuenta del día actual
        self.fishes_count_by_timer = new_fishes_count_by_timer

        # Incrementamos el día actual
        self.current_day += 1

        # Si el día actual esta en los target_days, imprimimos la cuenta del día actual
        if self.current_day in self.target_days:
            self.get_current_fish_count()

    def get_current_fish_count(self):
        print(f"Después de {self.current_day} días: Hay {sum(self.fishes_count_by_timer.values()):,} peces")


if __name__ == '__main__':
    # starting_fishes_counters = list(map(int, input("Ingresa los contadores iniciales de los peces, separados por comas: ").split(",")))
    starting_fishes_counters = [3, 1, 4, 2, 1, 1, 1, 1, 1, 1, 1, 4, 1, 4, 1, 2, 1, 1, 2, 1, 3, 4, 5, 1, 1, 4, 1, 3, 3, 1, 1, 1, 1, 3, 3, 1, 3, 3, 1, 5,
                                5, 1, 1, 3, 1, 1, 2, 1, 1, 1, 3, 1, 4, 3, 2, 1, 4, 3, 3, 1, 1, 1, 1, 5, 1, 4, 1, 1, 1, 4, 1, 4, 4, 1, 5, 1, 1, 4, 5, 1,
                                1, 2, 1, 1, 1, 4, 1, 2, 1, 1, 1, 1, 1, 1, 5, 1, 3, 1, 1, 4, 4, 1, 1, 5, 1, 2, 1, 1, 1, 1, 5, 1, 3, 1, 1, 1, 2, 2, 1, 4,
                                1, 3, 1, 4, 1, 2, 1, 1, 1, 1, 1, 3, 2, 5, 4, 4, 1, 3, 2, 1, 4, 1, 3, 1, 1, 1, 2, 1, 1, 5, 1, 2, 1, 1, 1, 2, 1, 4, 3, 1,
                                1, 1, 4, 1, 1, 1, 1, 1, 2, 2, 1, 1, 5, 1, 1, 3, 1, 2, 5, 5, 1, 4, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 4, 5, 1, 1, 1, 1, 1, 1,
                                1, 1, 1, 3, 4, 4, 1, 1, 4, 1, 3, 4, 1, 5, 4, 2, 5, 1, 2, 1, 1, 1, 1, 1, 1, 4, 3, 2, 1, 1, 3, 2, 5, 2, 5, 5, 1, 3, 1, 2,
                                1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1, 3, 1, 4, 1, 4, 2, 1, 3, 4, 1, 1, 1, 2, 3, 1, 1, 1, 4, 1, 2, 5, 1, 2, 1, 5, 1, 1,
                                2, 1, 2, 1, 1, 1, 1, 4, 3, 4, 1, 5, 5, 4, 1, 1, 5, 2, 1, 3]
    # target_days = list(map(int, input("Ingresa los días que quieres ver la cuenta de peces, separado por comas: ").split(",")))
    target_days = [18, 80, 256]
    max_target_days = max(target_days)
    ocean = Ocean(starting_fishes_counters, target_days)
    for _ in range(max_target_days):
        ocean.new_day()
