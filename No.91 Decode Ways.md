### No.91 Decode Ways
* DP，最大的问题是要想清楚DP的顺序
* 这个题的边界情况
  1 开头是0
  2 中间有0且能和前一个数组成10或者20
  3 中间有0但是不能组成10或者20
* 遇到3采取的策略是不变动dp[i]让他继续为0；其实做到这一步后面的就不用算了
```java
class Solution {
    public int numDecodings(String s) {
        char[] t = s.toCharArray();
        if (t.length == 0) return 0;
        if (t[0] == '0') return 0;
        //会算到dp[n]所以n+1
        int[] dp = new int[t.length+1];
        dp[0] = 1;
        dp[1] = 1;
        // a b c
        //     ^
        for (int i = 2; i <= t.length; ++i) {
            int front = (t[i-2] - '0')*10 + (t[i-1] - '0');
            
            if (t[i-1] != '0') {
                dp[i] = dp[i] + dp[i-1];
            }
            
            if (front > 9 && front < 27) {
                dp[i] = dp[i] + dp[i-2];
            }
            
            if (t[i-1] == '0') {
                if (front > 20 || front == 0) {
                    return 0;
                }
            }
        }
        return dp[t.length];
    }
}
```
