### No.44 Wildcard Matching 
* 第一种做法和NO 10的正则表达式匹配很像，用的DP，而且这次的DP更加清楚一些
```java
class Solution {
    public boolean isMatch(String s, String p) {
    int m=s.length(), n=p.length();
    boolean[][] dp = new boolean[m+1][n+1];
    dp[0][0] = true;
    for (int i=1; i<=m; i++) {
        dp[i][0] = false;
    }
    
    for(int j=1; j<=n; j++) {
        if(p.charAt(j-1)=='*'){
            dp[0][j] = true;
        } else {
            break;
        }
    }
    
    for(int i=1; i<=m; i++) {
        for(int j=1; j<=n; j++) {
            if (p.charAt(j-1)!='*') {
                dp[i][j] = dp[i-1][j-1] && (s.charAt(i-1)==p.charAt(j-1) || p.charAt(j-1)=='?');
            } else {
            //               任意字符串    0个
                dp[i][j] = dp[i-1][j] || dp[i][j-1];
            }
        }
    }
    return dp[m][n];
    }
}
