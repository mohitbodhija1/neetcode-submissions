class Solution:
    def countSubstrings(self, s: str) -> int:
        n=len(s)
        count =0

        def expand(left, right):
            palindromes=0
            while left>=0 and right<len(s) and s[left]==s[right]:
                palindromes+=1
                left -=1
                right +=1
            return palindromes
        
        for i in range(n):

            #odd length only one center
            count +=expand(i,i)
            



            #even length two center
            count += expand(i,i+1)
        return count

        