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
                present = True
                i = 1
                while present:
                    if num+i in nums:
                        i = i + 1
                    else:
                        present = False
                max_l = max(max_l, i)
        return max_l