### No.40 Combination Sum II
* 和一个区别在于需要判断正确解里的每个数字都不重复，第一个就是搜索的时候索引加一，
* 第二个就是搜索的函数里面加一行判断，如果搜到下一个并且下一个的值等于上一个，那么就不用搜了
```java
class Solution {
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        List<List<Integer>> ans = new ArrayList<>();
        if (candidates.length == 0 && target == 0) return ans;
        Arrays.sort(candidates);
        solver2(candidates, target, 0, new ArrayList<>(), ans);
        return ans;
    }
    
    public void solver2(int[] c, int target, int st, List<Integer> l, List<List<Integer>> ans) {
        if (target < 0) {return ;}
        else if (target == 0) {
            ans.add(new ArrayList<>(l));
        }
        else {
            for (int j = st; j < c.length; ++j) {
            //由于`j+1`和`j>st`所以，j-1不会越界，并且可以判断是否重复
                if (j > st && c[j] == c[j-1]) {continue;}
                l.add(c[j]);
                solver2(c, target-c[j], j+1, l, ans);
                l.remove(l.size() - 1);
            }
        }
    }
}

```
