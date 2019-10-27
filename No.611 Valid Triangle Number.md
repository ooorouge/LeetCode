### 这个问题，自己brute force很好想，找出所有组合然后一一判断，TLE
* three sum closet
```java
public class Solution {
    public int triangleNumber(int[] A) {
        if (A.length < 3) {
            return 0;
        }
        Arrays.sort(A);
        int count = 0, n = A.length;
        
        for (int i = n-1; i >= 2; i--) {
            int l = 0, r = i-1;
            while (l < r) {
                if (A[l] + A[r] > A[i]) {
                    count += r-l;
                    --r;
                }
                else ++l;
            }
        }
        return count;
    }
}
```
---
* TLE 
```java
class Solution {
    public int triangleNumber(int[] nums) {
        int ans = 0;
        if (nums.length == 0) {
            return ans;
        }
        List<List<Integer>> set = new ArrayList<>();
        dfs(set, nums, new ArrayList<Integer>(), 0);
        for (List<Integer> sub : set) {
            int add = sub.get(0) + sub.get(1);
            int min = Math.abs(sub.get(0) - sub.get(1));   //!!!!!!ABS
            if (add > sub.get(2) && min < sub.get(2)) {
                ++ans;
            }
        }
        return ans;
    }
    public void dfs(List<List<Integer>> set, int[] nums, List<Integer> subset, int start) {
        if (subset.size() == 3) {
            set.add(new ArrayList<>(subset));
            return ;
        }
        if (start >= nums.length) {
            return ;
        }
        for (int i = start; i < nums.length; ++i) {
            if (nums[i] > 0) {
                subset.add(nums[i]);
                dfs(set, nums, subset, i+1);
                subset.remove(subset.size()-1);
            }
        }
    }
}
```
