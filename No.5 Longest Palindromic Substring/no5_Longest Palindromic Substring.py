#找出索引而不用复制数据
#s[n:m] = s[n] -> s[m-1]
#最后一步考虑输出问题，最开始全考虑需要的索引是多少就行
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        temp = ""                       #storing
        length, start = 1, 0            #to determine max len and start indices
        len_s = len(s)
        if len_s == 0:
            return ''
        if len_s == 1:
            return s

        for i in range(len_s):
            l, r = self.search(s, i, i, len_s)
            if  r - l + 1 > length:
                start = l
                length = r - l + 1
            l, r = self.search(s, i, i + 1, len_s)
            if  r - l + 1 > length:
                start = l
                length = r - l + 1

        return s[start:start+length]

    def search(self, s, l_s, r_s, len_s):
        while l_s >= 0 and r_s < len_s and s[l_s] == s[r_s]:
            l_s -= 1
            r_s += 1
        return l_s + 1, r_s - 1
