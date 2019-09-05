### Regular Expression Match
* 难点很多，感觉第一是不知道用dp来做，还想着用状态机的办法来写
* 为什么用dp需要好好想清楚
* 细节
  * Java boolean默认值为false
  * `dp[i][j]`里的`ij`是指的个数，而`ss[i][j]`里的`ij`实际上是指的索引，索引=当前个数-1
  * 里面有一些`j-2`的索引之所以不会出现错误完全是因为所有的testcase都没有p的第一个char就是*的情况，这样写也不符合re
```java
class Solution {
    public boolean isMatch(String s, String p) {
        if (s != null && p == null) return false;

        int ls = s.length(); int lp = p.length();
        char[] ss = s.toCharArray();
        char[] pp = p.toCharArray();

        boolean[][] dp = new boolean[ls+1][lp+1];//长度包括两个都是空串的最初子问题，所以+1
        dp[0][0] = true;

        //实际上dp[m][n]表示的是 s[:m] 和 p[:n]的匹配情况，所以和子问题有关
        for (int t = 1; t < lp+1; ++t) {
        	if (pp[t-1] == '*') {
        		dp[0][t] = dp[0][t-2];
        	}
        	//else dp[0][t] = false; java boolean默认值为false
        }
        //注意以下dp中的索引ij实际上指的是个数，而不是实际的char[]索引，所以需要-1
        for (int i = 1; i < ls+1; ++i ) {
        	for (int j = 1; j < lp+1; ++j) {
        		if (ss[i-1] == pp[j-1] || pp[j-1] == '.') {
        			dp[i][j] = dp[i-1][j-1];
        		}
        		else if (pp[j-1] == '*') {
        			dp[i][j] = dp[i][j-2];
        			if (ss[i-1] == pp[j-2] || pp[j-2] == '.') dp[i][j] = dp[i-1][j] || dp[i][j];
        		}
        	}
        }
        return dp[ls][lp];
    }
}
```
