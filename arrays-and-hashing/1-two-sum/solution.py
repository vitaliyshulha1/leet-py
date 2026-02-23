class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {} # we save all items with their index
        for i, n in enumerate(nums):
            diff = target - n # substract num from target so we get second number
            if diff in seen: # check if the diff number is in already seen, if yes, return senn[index of diff] and i - current num
                return [seen[diff], i]
            seen[n] = i # just add curret number to seen
        return []

sol = Solution()
print(sol.twoSum([2, 7, 11, 15], 9))