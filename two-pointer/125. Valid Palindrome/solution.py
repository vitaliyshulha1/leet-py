from typing import List

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1 # 2 pointers, left 0, right length of array -1 (cuz array starts with 0)

        while left < right: 
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1 # move pointer to right->
            right -= 1 #

        return True

sol = Solution()
print(sol.groupAnagrams("A man, a plan, a canal: Panama"))





#  **`left < right`** — проверяет, что левый указатель не пересёк правый (не вышли за границы)
#  **`not s[left].isalnum()`** — проверяет, что текущий символ **не** является буквой или цифрой
#  **`left += 1`** — если оба условия верны, сдвигает левый указатель вправо