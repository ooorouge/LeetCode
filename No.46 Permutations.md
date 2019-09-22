### No.46 Permutations
* 这个做法是一个通用的办法
* new ArrayList<>(single)替换成single是传不出来的，猜测nums[i]是基本类型所以每个single实例化指向stack上的nums[i]值传递产生的副本，副本到return ans就会失效释放
```java
class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> ans = new ArrayList<>();
        permutation(ans, new ArrayList<>(), nums, new boolean[nums.length]);
        return ans;
    }
    public void permutation(List<List<Integer>> ans, List<Integer> single, int[] nums, boolean[] ava) {
        if (single.size() == nums.length) {
            ans.add(new ArrayList<>(single));               //!!!IMPORTANT
        } else {
            for (int i = 0; i < nums.length; ++i) {
                if (ava[i]) continue;
                else {
                    single.add(nums[i]);
                    ava[i] = true;
                    permutation(ans, single, nums, ava);
                    single.remove(single.size() - 1);      //!!!IMPORTANT
                    ava[i] = false;                        //!!!IMPORTANT
                }
            }
        }
    }
}
```
