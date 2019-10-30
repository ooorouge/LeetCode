### dp
* 问题的模式是从底至上，然后每一层的每一个位置都只需要选择上一层两个位置的最小值
```java
class Solution {
    
    public int minimumTotal(List<List<Integer>> t) {
        if (t.size() == 0) {
            return 0;
        }
        if (t.size() == 1) {
            return t.get(0).get(0);
        }
        int[] dp = new int[t.size()+1];
        for (int i = t.size() - 1; i > -1; --i) {
            for (int j = 0; j <= i; ++j) {
                dp[j] = Math.min(dp[j], dp[j+1]) + t.get(i).get(j);
            }
        }
        return dp[0];
    }
}
```
