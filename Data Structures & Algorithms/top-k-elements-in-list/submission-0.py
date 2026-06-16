from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count frequencies
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        
        # Step 2: Sort by frequency descending
        sorted_nums = sorted(freq.keys(), key=lambda x: freq[x], reverse=True)
        # sorted_nums = sorted(freq.keys(), key=lambda x: freq[x], reverse=True)

        print(sorted_nums)
        
        # Step 3: Return top k
        return sorted_nums[:k]