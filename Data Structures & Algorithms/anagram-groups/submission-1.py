from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        
        for word in strs:
            # Build frequency array of size 26
            count = [0] * 26
            for char in word:
                count[ord(char) - ord('a')] += 1
            
            # List is unhashable → convert to tuple for dict key
            key = tuple(count)
            anagram_map[key].append(word)
        
        return list(anagram_map.values())