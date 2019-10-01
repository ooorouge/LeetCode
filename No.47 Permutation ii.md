### No.47 Permutation II
* 这个和permutation I的区别还是挺大的，注意used[i]的两种写法导致的区别，runtime
```java
class Solution {
    public List<List<Integer>> permuteUnique(int[] nums) {
        List<List<Integer>> ans = new ArrayList<>();
        if (nums.length == 0) {return ans;}
        Arrays.sort(nums);
        boolean[] used = new boolean[nums.length];
        dfs(ans, nums, used, new ArrayList<Integer>());
        return ans;
    }
    public void dfs(List<List<Integer>> ans, int[] nums, boolean[] used, List<Integer> l) {
        if (l.size() == nums.length) {
            ans.add(new ArrayList<Integer>(l));
        }
        
        for (int i = 0; i < nums.length; ++i) {
            //i-1和i数字相同，而且i-1还没用过才continue？？？
            //用!used[i-1]能保证生成的每一个枝都能走到底，不会浪费
            //用used[i]如果上一层用了i,走到下一层搜到i+1那么i+1不用，意味着再怎么找这个枝都搜不够nums.length个
            if (used[i] || i > 0 && nums[i] == nums[i-1] && !used[i-1]) continue; //used
            l.add(nums[i]);
            used[i] = true;
            dfs(ans, nums, used, l);
            l.remove(l.size()-1);
            used[i] = false;
        }
        
    }
}
```
