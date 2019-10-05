### No.213 House Robber II
* 唯一不同的就是这个首尾是相连的，所以
```java
class Solution {
    public int rob(int[] nums) {
        if (nums.length == 0) {return 0;}
        if (nums.length == 1) {return nums[0];}
        int[] start = Arrays.copyOfRange(nums, 0, nums.length-1);
        int[] end = Arrays.copyOfRange(nums, 1, nums.length);
        int pre12 = 0;
        int pre11 = 0;
        int pre22 = 0;
        int pre21 = 0;
        // pre2, pre1, current
        for (int i = 0; i < start.length; ++i) {
            int t1 = pre11;
            pre11 = Math.max(start[i]+pre12, pre11);
            pre12 = t1;
            
            int t2 = pre21;
            pre21 = Math.max(end[i]+pre22, pre21);
            pre22 = t2;
        }
        return Math.max(pre11, pre21);
    }
}
```
