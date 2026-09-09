class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for num in nums[:len(nums)-1]:
            i = nums.index(num)
            for j in range(i+1, len(nums)):
                if num + nums[j] == target:
                    return [i, j]