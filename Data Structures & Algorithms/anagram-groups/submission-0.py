from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        
        for word in strs:
            key = "".join(sorted(word))   # "eat" → "aet"
            anagram_map[key].append(word) # group by key
        
        return list(anagram_map.values())