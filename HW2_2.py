# Імпортуємо лібу.
from collections import deque

# Створюємо функцію.
def is_palindrome(input_value):

    input_value = ''.join(char.lower() for char in input_value if char.isalnum())

    char_deque = deque(input_value)
# Створюємо цикл перебору.
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False
        return True

# Запускаємо нашу функцію з заданим значенням.
print(is_palindrome("A man a plan a canal Panama"))
print(is_palindrome("Deep Purple"))