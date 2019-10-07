### No.198 House Robber
*  DP，想清楚DP的具体怎么推导的
```java
class Solution {
    public int rob(int[] nums) {
        if (nums.length == 0) {return 0;}
        if (nums.length == 1) {return nums[0];}
        int ans = 0;
        int[] dp = new int[nums.length+1];
        dp[0] = 0;
        dp[1] = nums[0];
        //dp[2] = Math.max(dp[1], nums[1]);
        // nums 0 1 2 3 4 5 6
        // dp 0 1 2 3 4 5 6 7
        for (int i = 2; i <= nums.length; ++i) {
            dp[i] = Math.max(dp[i-2]+nums[i-1], dp[i-1]);
        }
        return dp[nums.length];
    }
}
```