### Unique Path. DP和第一个的做法是一样的
* 实际上这个题可以原址计算
```java
class Solution {
    public int uniquePathsWithObstacles(int[][] g) {
        if (g.length == 0) {return 0;}
        int row = g.length;
        int col = g[0].length;
        int start = 0;
        while (start < row && g[start][0] != 1) {
            g[start][0] = 1;
            ++start;
        }
        start = 0;
        while (start < col && g[0][start] != 1) {
            dp[0][start] = 1;
            ++start;
        }
        
        for (int i = 1; i < row; ++i) {
            for (int j = 1; j < col; ++j) {
                if (g[i][j] != 1)
                    dp[i][j] = dp[i-1][j] + dp[i][j-1];
                else 
                    dp[i][j] = 0;
            }
        }
        return dp[row-1][col-1];
    }
}
```
