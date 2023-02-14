
# --------------------  MY SOLUTION --------------------

def isAnagram(s: str, t: str) -> bool:
        # Contamos cuantas veces se repiten las letras de s
        s_letter_count = {}
        for s_letter in s:
            if count:= s_letter_count.get(s_letter):
                s_letter_count[s_letter] = count+1
            else:
                 s_letter_count[s_letter] = 1

        # Iteramos sobre las letras de t y revisamos que exista en s_letter_count
        # Si no existe no es anagram, si sí, revizamos si la cuenta es diferente de cero
        # si lo es reducimos la cuenta de esa letra y continuamos a la siguiente letra de t
        for t_letter in t:
            if s_letter_count.get(t_letter):
                    # Reducimos la cuenta
                    s_letter_count[t_letter] -= 1
            else:
                return False

        # Si alguna de las letras de s no se uso no es un anagrama
        return not any(s_letter_count.values())


# ------------------------  ONE LINER ------------------------

def isAnagramOneLiner(s: str, t: str) -> bool:
        return sorted(s)==sorted(t)


if __name__ == '__main__':
    s = "anagram"
    t = "nagaram"
    print(isAnagram(s, t))
    print(isAnagramOneLiner(s, t))
    s = "rat"
    t = "car"
    print(isAnagram(s, t))
    print(isAnagramOneLiner(s, t))