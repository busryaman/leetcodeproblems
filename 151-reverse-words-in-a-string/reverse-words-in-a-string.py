class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s.split()
        return ' '.join(s.split()[::-1])

        