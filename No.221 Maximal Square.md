### No.221 Maximal Square
* 本来要用bfs,发现复杂度肯定很高然后开始看答案，用的dp
* 基本理由，一个点的最大square由上，左，左上的最小square决定，如果上，左，左上都是n,加上这个点可以构成n+1 square,相反，短板限制了square
```java
class Solution {
    public int maximalSquare(char[][] m) {
        if (m.length == 0 || m[0].length == 0) {return 0;}
        int max = 0;
        int[][] dp = new int[m.length+1][m[0].length+1];
        
        for (int i = 0; i < m[0].length; ++i) {
            if (m[0][i] == '1') {dp[0][i] = 1;max = 1;}
            else {continue;}
        }
        for (int i = 0; i < m.length; ++i) {
            if (m[i][0] == '1') {dp[i][0] = 1;max = 1;}
            else {continue;}
        }
        for (int i = 1; i < m.length; ++i) {
            for (int j = 1; j < m[0].length; ++j) {
                if (m[i][j] == '1') {
                //!!!!!!!!!!!!!!!!!!!!!!!
                    dp[i][j] = Math.min(Math.min(dp[i-1][j], dp[i][j-1]), dp[i-1][j-1]) + 1;
                    max = Math.max(dp[i][j], max);
                } else {
                    dp[i][j] = 0;
                }
            }
        }
        return max*max;
    }
}
```
