class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
            
        # Create a combined string: s + '#' + reversed(s)
        rev_s = s[::-1]
        combined = s + "#" + rev_s
        
        # Build the KMP prefix table (LPS - Longest Prefix Suffix)
        lps = [0] * len(combined)
        j = 0
        
        for i in range(1, len(combined)):
            while j > 0 and combined[i] != combined[j]:
                j = lps[j - 1]
            if combined[i] == combined[j]:
                j += 1
                lps[i] = j
                
        # The last value in the LPS array gives the length of the 
        # longest palindromic prefix of s
        palindrome_len = lps[-1]
        
        # Characters after the longest palindromic prefix need to be reversed 
        # and prepended to s
        to_add = rev_s[:len(s) - palindrome_len]
        return to_add + s