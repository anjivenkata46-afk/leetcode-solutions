class Solution(object):
    def reverseWords(self, s):
        """:type s: str
        :rtype: str
        """
        # split() without arguments handles leading, trailing, 
        # and multiple whitespace between words automatically.
        words = s.split()
        
        # Reverse the list of words and join them back with a single space
        return " ".join(words[::-1])