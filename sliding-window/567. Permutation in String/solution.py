from collections import Counter
# a permutation is an anagram of a string.
# ab ba .


# there are 2 ways to solve this problem.
# we can use sliding window pattern

# we have 26 characters
# we use 2 hash sets 


# one for window one for string we are looking for.

# We slide a window and compare character frequencies. If the count of every letter in our window matches the count in , we found a permutation

# this would be  O(26)

# for that we have to use variabel matches

# ─── Решение 1: Counter (простое и читаемое) ───────────────────────────────
class SolutionCounter:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        count1 = Counter(s1) # hashMap each char is a key, value is frequency
        count2 = Counter(s2[:len(s1)]) ## s2[:3]  take o to 3 (substring)

        if count1 == count2:
            return True

        for i in range(len(s1), len(s2)): # i is now end of window -> ]
            count2[s2[i]] += 1 # add character to the right

            left = s2[i - len(s1)] # move left pointer len(s1) is length of sliding window
            count2[left] -= 1
            if count2[left] == 0: ## {'a': 1, 'b': 1} == {'b': 0, 'a': 1, 'c': 1} → False. to avoid thos we need to delete key
                del count2[left]

            if count1 == count2:
                return True

        return False


# ─── Решение 2: Массив + matches (быстрее, O(1) сравнение) ─────────────────
class SolutionOptimized:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count, s2Count = [0] * 26, [0] * 26

        # Заполняем первое окно
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        # Считаем сколько букв уже совпадают
        matches = sum(1 for i in range(26) if s1Count[i] == s2Count[i])

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            # Добавляем правый символ
            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            # Убираем левый символ
            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            l += 1

        return matches == 26


# ─── Тесты ─────────────────────────────────────────────────────────────────
test_cases = [
    ("ab",    "eidbaooo",      True),
    ("ab",    "eidboaoo",      False),
    ("a",     "a",             True),
    ("abc",   "ab",            False),
    ("aab",   "lecaabee",      True),
    ("hello", "ooolleoooleh",  False),
]

sol1 = SolutionCounter()
sol2 = SolutionOptimized()

print(f"{'Тест':<10} {'s1':<8} {'s2':<18} {'Ожид.':<8} {'Counter':<10} {'Optimized'}")
print("-" * 65)

for i, (s1, s2, expected) in enumerate(test_cases, 1):
    r1 = sol1.checkInclusion(s1, s2)
    r2 = sol2.checkInclusion(s1, s2)
    status1 = "✓" if r1 == expected else "✗"
    status2 = "✓" if r2 == expected else "✗"
    print(f"Тест {i:<5} {s1:<8} {s2:<18} {str(expected):<8} {str(r1)+status1:<10} {str(r2)+status2}")