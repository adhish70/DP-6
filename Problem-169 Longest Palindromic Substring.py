# 5. Longest Palindromic Substring
# https://leetcode.com/problems/longest-palindromic-substring/

# Logic: For each index, we start an odd length and an even length palindrome search.

# Time Complexity: O(n*n)
# Space Complexity: O(1)

class Solution:
    def _helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        
        return s[l+1:r]
    
    def longestPalindrome(self, s: str) -> str:
        res = ''
        
        for i in range(len(s)):
            odd_len = self._helper(s, i, i) # We have to start expanding from the same element when odd length input
            even_len = self._helper(s, i, i+1)
            
            temp = odd_len if len(odd_len) > len(even_len) else even_len
            if len(temp) > len(res):
                res = temp
        
        return res