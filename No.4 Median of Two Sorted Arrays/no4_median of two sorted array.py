class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(nums1), len(nums2)
        if m > n:
        	nums1, nums2, m, n = nums2, nums1, n, m
        if n <= 0:
        	return False

        # m+n+1 !!!!! not m+n 
        #比如一共有九个数的时候，如果没写+1的话i+j为4不是5
        #如果不+1返回函数需要重新写
        #这种情况下return的东西是不对的
        imin, imax, half = 0, m, int((m+n+1)/2)
        while imin <= imax:
        	i = int((imin + imax) / 2)
        	j = half - i
        	if i < m and nums2[j-1] > nums1[i]:
        		imin = i + 1 
        	elif i > 0 and nums1[i-1] > nums2[j]:
        		imax = i - 1
        	else:
        		if i == 0:
        			max_l = nums2[j-1]
        		elif j == 0:
        			max_l = nums1[i-1]
        		else:
        			max_l = max(nums1[i-1], nums2[j-1])

        		if (m+n) % 2 == 1:
        			return max_l

        		if i == m:
        			min_r = nums2[j]
        		elif j == n:
        			min_r = nums1[i]
        		else:
        			min_r = min(nums1[i], nums2[j])

        		return (max_l + min_r) / 2.0


