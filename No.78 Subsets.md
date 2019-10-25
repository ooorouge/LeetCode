### 经验教训，几天不做题，会变菜
```java
class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> ans = new ArrayList<>();
        ans.add(new ArrayList<Integer>());
        if (nums.length == 0) {
            return ans;
        }
        for (int i = 1; i <= nums.length; ++i) {
            dfs(ans, new ArrayList<Integer>(), i, nums, 0);
        }
        return ans;
    }
    public void dfs(List<List<Integer>> ans, List<Integer> subset, int len, int[] nums, int start) {
        if (subset.size() == len) {
            ans.add(new ArrayList<Integer>(subset));
            return ;
        }
        /*之前写成这样了，i本来该是len,start该是i+1
        for (int i = start; i < nums.length; ++i) {
            subset.add(nums[i]);
            dfs(ans, subset, i, nums, start+1);
            subset.remove(subset.size() -1);
        }
        */
        for (int i = start; i < nums.length; ++i) {
            subset.add(nums[i]);
            dfs(ans, subset, len, nums, i+1);
            subset.remove(subset.size() -1);
        }
    }
}
```
