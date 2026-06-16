class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        hash = {}
        for char in s:
            if char in hash:
                hash[char] +=1
            else:
                hash[char] = 1
        new = {}
        for char in t:
            if char in new:
                new[char] += 1
            else:
                new[char] = 1
        print(hash)
        print(new)
        for k, v in hash.items():
            if k not in new:
                return False
            if v != new[k]:
                return False
        return True

        