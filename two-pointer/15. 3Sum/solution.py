from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Сортируем массив — это ключевой шаг:
        # 1) Позволяет использовать два указателя
        # 2) Позволяет легко пропускать дубликаты
        nums.sort()
        result = []

        for i in range(len(nums) - 2):
            # Пропускаем дубликаты для первого элемента
            # (чтобы не добавить одинаковые тройки)
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Два указателя: left — сразу после i, right — конец массива
            left, right = i + 1, len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])

                    # Пропускаем дубликаты для второго элемента
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Пропускаем дубликаты для третьего элемента
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # Сдвигаем оба указателя навстречу
                    left += 1
                    right -= 1

                elif total < 0:
                    # Сумма слишком мала — нужно большее число, сдвигаем left вправо
                    left += 1
                else:
                    # Сумма слишком велика — нужно меньшее число, сдвигаем right влево
                    right -= 1

        return result


sol = Solution()

# [-1,0,1,2,-1,-4] → тройки: [-1,-1,2] и [-1,0,1]
print(sol.threeSum([-1, 0, 1, 2, -1, -4]))   # [[-1,-1,2],[-1,0,1]]

# [0,1,1] → нет тройки с суммой 0
print(sol.threeSum([0, 1, 1]))                # []

# [0,0,0] → единственная тройка [0,0,0]
print(sol.threeSum([0, 0, 0]))               # [[0,0,0]]

# [] → пустой массив → нет троек
print(sol.threeSum([]))                       # []