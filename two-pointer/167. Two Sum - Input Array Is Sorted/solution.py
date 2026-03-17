class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        # we make two pointers, left[0] right[arraylength]
        left, right = 0, len(numbers) - 1

        while left < right: # while pointer dont meet
            current_sum = numbers[left] + numbers[right] # sum current numbers

            if current_sum == target:
                # if current sum same as target - numer found.
                return [left + 1, right + 1]

            elif current_sum < target:
                # if sum is too small, we move LEFT poniter to right, to make sum bigger (because we know that array is sorted in non-decreasing order )
                left += 1

            else:
                # if sum is too big (bigger thank target) , we need to make sum smaller, so we move right pointer to left
                right -= 1




sol = Solution()
print(sol.twoSum( [1,2,3,4], 3))


# брутфорс был бы сравнивать кадое число с другим (суммировать) и результат сравнивать с икомым. но это О(N^2)
# так как массив отсортирован, мы можем двигаться двумя поинтерами из разных сторон массива навстречу.abs
# и проверять является ли сумма двух чисел искомому? если сумма слижком мала, то мы двигаем левый поинтер врпаво, а если сумма сжижком большая, то двигаем правый влево