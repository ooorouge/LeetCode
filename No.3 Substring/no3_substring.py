class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
#最开始感觉用stack来做，应该可行，估计是有些地方写错了，有时间再改改
'''
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        d, res, start = {}, 0, 0
        for i, ch in enumerate(s):
            if ch in d: start = max(start, d[ch]+1)
            res = max(res, i-start+1)                
            d[ch] = i
        return res
'''
        d, res, start = {}, 0, 0
        for i, ch in enumerate(s):
            if ch in d: start = max(start, d[ch]+1)
            res = max(res, i-start+1)                
            d[ch] = i
        return res
