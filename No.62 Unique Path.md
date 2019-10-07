### Unique Paths
* 这个问题其实是可以直接拿排列组合算出来的，因为每个mn对，都必须走m-1步下和n-1步右
* 但是直接阶乘会出现一个问题，int越界，所以迭代的每一步一边做乘法一边做除法，不要一次性乘出来
```java
class Solution {
    public int uniquePaths(int m, int n) {
        if (m == 0||n == 0) {return 0;}
        if (m == 1||n == 1) {return 1;}
        int[] dp = new int[n];
        dp[0] = 1;
        for (int i = 0; i < m; i++) {
            for (int j = 1; j < n; j++) {
                dp[j] += dp[j-1];
            }
        }
        return dp[n-1];
    }
}
```
