### No.34 Find First and Last Position of Element in Sorted Array
* 二分查找
```java
class Solution {
    public int[] searchRange(int[] nums, int target) {
        int[] ans = new int[2];
        ans[0] = -1; ans[1] = -1;
        if (nums.length == 0) return ans;
        
        int first = 0;
        int last = nums.length - 1;
        int mid = 0;
        while (first < last) {
            mid = first + (last - first) / 2;
            if (nums[mid] < target) {
                first = mid + 1;
            } else if (nums[mid] > target) {
                last = mid - 1;
            } else {
                ans[0] = mid;
                ans[1] = mid;
                break;
            }
        }
        mid = first + (last-first)/2;
        if (nums[mid] == target) {
            first = mid; last = mid;
            ans[0] = mid; ans[1] = mid;
            while(first > 0 && nums[first-1] == target) {
                ans[0] = --first;
            }
            while(last < nums.length - 1 && nums[last+1] == target) {
                ans[1] = ++last;
            }
        }
        
        return ans;
    }
}
```
