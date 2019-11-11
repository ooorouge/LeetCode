### 一道简单的ood题？
```java
class Solution {
    public int[] nums;
    Random rand;
    public Solution(int[] nums) {
        this.nums = nums;    
        this.rand = new Random();
    }
    
    public int pick(int target) {
        List<Integer> randlist = new ArrayList<>();
        for (int i = 0; i < this.nums.length; ++i) {
            if (nums[i] == target) {
                randlist.add(i);
            }
        }
        if (randlist.size() == 0) {
            return -1;
        } else {
            int index = rand.nextInt(randlist.size());
            return randlist.get(index);
        }
    }
}
```
