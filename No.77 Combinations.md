### DFS
* 还是一个问题，注意在子函数里，需要`ans.add(new ArrayList<>(sub))`
```java
class Solution {
    public List<List<Integer>> combine(int n, int k) {
        List<List<Integer>> ans = new ArrayList<>();
        if (k == 0 || n == 0) {
            return ans;
        }
        dfs(ans, new ArrayList<Integer>(), n, k, 1);
        return ans;
    }
    
    public void dfs(List<List<Integer>> ans, List<Integer> subans, int n, int k, int start) {
        if (k == 0) {
            ans.add(new ArrayList<>(subans));
            return ;
        }
        // for (int i = start; i <= n; ++i) 如果是这一句，那么运行时间会从2ms变到28ms，很重要
        for (int i = start; i <= n-k+1; ++i) {
            subans.add(i);
            dfs(ans, subans, n, k-1, i+1);
            subans.remove(subans.size()-1);
        }
    }
}
```
