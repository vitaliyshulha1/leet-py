from typing import List

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        dic = {}
        for s in strs:   
            freq = [0] * 26    #  26 букв в алфавите
            for c in s:
                freq[ord(c) - ord('a')] += 1  #  создаем ключ. а = 97, другие буквы идут за ей, б - 98, г - 99 и так далее. так нахожти например индекс Б  .  Б(98)  - А(97) = 1. и деалем freq[1] ++
            
            key = tuple(freq) # tuple(freq) превращает список в неизменяемый кортеж, чтобы использовать его как ключ словаря.

            if key not in dic:  #  теперь смотрим, есть ли такой ключ в словаре, если нету, то добавляем.
                dic[key] = []

            dic[key].append(s)#  добавляем в ключ само слово.

        return list(dic.values())

sol = Solution()
print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))




# // A naive solution would be to sort each string and group them using a hash map. This would be an O(m * nlogn) solution. Though this solution is acceptable, can you think of a better way without sorting the strings?
# в аннаграмме нас интересует количество каждой буквы, поэтому мы можем создать HashMap как ключ для кажого слова: мы создаем словарь, ключ freq это Array из 26 букв.
# берем кадое слова и для каждой его буквы букву(ее значение в ASCII Table ) - a.    a имеет номер 97. тоесть если это буква Б, то будет 98 - 97 = 1. вот идекс один мы увеличиваем.++
# в пайтоне ord() возврашет аски код символа