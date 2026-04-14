class Solution:
    def isValid(self, s: str) -> bool:
        # Словарь соответствия: ключ — закрывающая скобка, значение — открывающая
        bracket_map = {")": "(", "}": "{", "]": "["}
        # Стек для хранения открывающих скобок
        stack = []

        for char in s:
            # Если символ есть в ключах словаря — значит это закрывающая скобка
            if char in bracket_map:
                # Достаем верхний элемент, если стек не пуст. 
                # Если пуст — берем заглушку '#', которая не совпадет ни с одной скобкой.
                top_element = stack.pop() if stack else '#'
                
                # Если пара не совпала — строка невалидна
                if bracket_map[char] != top_element:
                    return False
            else:
                # Если символ — открывающая скобка, кладем её "на верхушку" стека
                stack.append(char)

        # В конце стек должен быть пустым (not stack вернет True)
        return not stack

# Создаем экземпляр класса
sol = Solution()

# --- ТЕСТЫ ---

# Правильные последовательности
print(sol.isValid("()"))          # True
print(sol.isValid("()[]{}"))      # True
print(sol.isValid("{[]}"))        # True

# Неправильные последовательности
print(sol.isValid("(]"))          # False (разные типы)
print(sol.isValid("([)]"))        # False (нарушен порядок)
print(sol.isValid("]"))           # False (закрывающая без открывающей)
print(sol.isValid("(("))          # False (открывающая не закрыта)