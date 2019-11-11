### 首先一开始便利的时候只关注`!set.contains(nums[i]-1)`,后面找到才开始`while (set.contains(cur+1))`保证了不会
```java
class Solution {
    public int longestConsecutive(int[] nums) {
        int answer = 0;
        Set<Integer> set = new HashSet<>();
        for (int i = 0; i < nums.length; i++) {
        	set.add(nums[i]);
        }
        for (int i = 0; i < nums.length; i++) {
        	if (!set.contains(nums[i]-1)) {
				int thissequence = 1;
        		int cur = nums[i];
        		while (set.contains(cur+1)) {
        			++cur;
        			++thissequence;
        		}
        		answer = Math.max(answer, thissequence);
        	}
        }
        return answer;
    }
}
```
