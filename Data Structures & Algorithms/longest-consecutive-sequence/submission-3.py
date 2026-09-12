class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        max_l = 1
        nums = set(nums)
        for num in nums:
            if num-1 in nums:
                continue
            else:
                length = 1
                while num + length in nums:
                    length += 1
                max_l = max(max_l, length)
        return max_l