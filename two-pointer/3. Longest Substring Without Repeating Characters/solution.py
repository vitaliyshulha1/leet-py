from typing import List

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Словарь для хранения последнего индекса каждого символа
        char_index = {}
        
        # left — левая граница текущего окна (скользящее окно)
        left = 0
        max_len = 0

        for right in range(len(s)):
            char = s[right]

            # Если символ уже встречался И он находится внутри текущего окна
            # (char_index[char] >= left), сдвигаем левую границу вправо
            if char in char_index and char_index[char] >= left:
                left = char_index[char] + 1  # сдвигаем за повторяющийся символ

            # Обновляем последний известный индекс символа
            char_index[char] = right

            # Длина текущего окна: right - left + 1
            max_len = max(max_len, right - left + 1)

        return max_len


sol = Solution()

# "abcabcbb" → окно [a,b,c], потом сдвигается → ответ 3
print(sol.lengthOfLongestSubstring("abcabcbb"))   # 3

# "bbbbb" → каждый раз сдвигаем left, окно всегда длиной 1 → ответ 1
print(sol.lengthOfLongestSubstring("bbbbb"))       # 1

# "pwwkew" → окно [w,k,e,w], но первый w повторяется → [k,e,w] → ответ 3
print(sol.lengthOfLongestSubstring("pwwkew"))      # 3

# "" → пустая строка → ответ 0
print(sol.lengthOfLongestSubstring(""))            # 0