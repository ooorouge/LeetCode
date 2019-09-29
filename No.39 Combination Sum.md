### No.39 Combination Sum
* 其实这个题的回溯思路和求解数独非常的像
* 总结一下回溯的模式
* 第一，添加每个有可能的，然后往后搜索（在当前结果上递归掉用），不要改动结果
* 第二，搜索到最后一个的时候发现解是正确的，添加到整体结果上去
* 返回，在出现分支的地方剪掉已经用过的分支，
```java
class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> ans = new ArrayList<>();
        if (candidates.length == 0 && target == 0) return ans;
        Arrays.sort(candidates);//防止重复项
        solver(candidates, target, 0, new ArrayList<>(), ans);
        return ans;
    }
    
    public void solver(int[] c, int target, int i, List<Integer> l, List<List<Integer>> ans) {
        if (target < 0) {return ;}
        else if (target == 0) {
            ans.add(new ArrayList<>(l));
        }
        else {
            for (int j = i; j < c.length; ++j) {
                l.add(c[j]);
                solver(c, target-c[j], j, l, ans);
                l.remove(l.size() - 1);
                //这个地方和求解数独还是很不一样，数独只有唯一解
            }
        }
    }
}
```
