### No.33 Search in Rotated Sorted Array
* 基本情况就是四种，具体上下边界移动情况就是两种，在写if的时候只写两种执行一直判断容易TLE，拆开成四种写，注意边界情况
```java
public class Solution {
public int search(int[] nums, int target) {
    int start = 0, end = nums.length - 1;
    if (nums.length == 0) return -1;
    
    while (start < end) {
        int mid = start + (end - start) / 2;
        if (nums[mid] > nums[end]) {
            //将target == end 或者 target == start视为最坏情况，不要单独写
            if (target > nums[mid] || target <= nums[end]) {
                start = mid + 1;
                //其实可以把这个else再拆一下写成命中提前返回
            } else {
                end = mid;
            }
        } else {
            if (target > nums[mid] && target <= nums[end]) {
                start = mid + 1;
            } else {
                end = mid;
            }
        }
    }
    if (start == end && target != nums[start]) return -1;
    return start;
    }
}
```
* 错误示范
```java
if ((nums[mid] > nums[0] && (target < nums[0] || target > nums[mid])) || (nums[mid] < nums[0] && target < nums[0] && target > nums[mid])){
                start = mid + 1;
            } else if ((nums[mid] > nums[0] && target > nums[0] && target < nums[mid]) || (nums[mid] < nums[0] && (target < nums[mid] || target > nums[0]))) {
                end = mid - 1;
```
