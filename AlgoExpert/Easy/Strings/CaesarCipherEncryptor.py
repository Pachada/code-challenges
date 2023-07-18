"""
Caesar Cipher Encryptor | AlgoExpert
Given a non-empty string of lowercase letters and a non-negative integer representing a key, 
write a function that returns a new string obtained by shifting every letter in the input string 
by k positions in the alphabet, where k is the key.

Note that letters should "wrap" around the alphabet; in other words, the letter z shifted by one returns the letter a.

Sample Input
string = "xyz"
key = 2
Sample Output
"zab"
"""
Z_UNICODE_VALUE = ord("z")
A_UNICODE_VALUE = ord("a")

# O(n) time | O(n) space
def caesarCipherEncryptor(string: str, key: int) -> str:
    if not key:
        return string
    new_values = []
    for letter in string:
        new_value = ord(letter) + key
        if new_value > Z_UNICODE_VALUE:
            new_value = A_UNICODE_VALUE + (new_value - A_UNICODE_VALUE) % 26

        new_values.append(chr(new_value))

    return "".join(new_values)


if __name__ == "__main__":
    string = "abc"
    key = 52
    print(caesarCipherEncryptor(string, key))
