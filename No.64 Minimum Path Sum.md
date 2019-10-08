### dp,用dfs有个问题，必须弄一个全局的min，没比要
* 这个可以在原址上加，然后dp每次加的东西需要注意加上`g[i][j]`而不是`dp[i][j]`的值
``java
class Solution {
    int min = -1;
    public int minPathSum(int[][] g) {
        if (g.length == 0) {return 0;}
        
        int r = g.length;
        int c = g[0].length;
        int[][] dp = new int[r][c];
        dp[0][0] = g[0][0];
        
        for (int i = 1; i < r; ++i) {
            dp[i][0] = g[i][0] + dp[i-1][0];
        }
        for (int i = 1; i < c; ++i) {
            dp[0][i] = g[0][i] + dp[0][i-1];
        }
        for (int i = 1; i < r; ++i) {
            for (int j = 1; j < c; ++j) {
                dp[i][j] = g[i][j] + Math.min(dp[i-1][j], dp[i][j-1]);
            }
        }
        return dp[r-1][c-1];
    }
}
```
