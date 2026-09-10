class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {}
        for num in nums:
            if num in frequencies:
                frequencies[num] = frequencies[num] + 1
            else:
                frequencies[num] = 1
        frequencies = sorted(frequencies.items(), key=lambda x: x[1], reverse=True)
        top = []
        for f in frequencies[:k]:
            top.append(f[0])
        return top
