### Maximum Subarray
* 注意11/12行别写错了
* Java三元运算符

```java
class Solution {
    public int maxSubArray(int[] nums) {
        int sum = nums[0];
        int max_sum = nums[0];
        int len = nums.length;
        int cur = 0;
        for(int i = 1; i < len; ++i){
            if(sum< 0) {sum = 0;}
            sum += nums[i];
            ++cur;
            //java里的三元运算符不能单独出现，具体原因Java里三元运算符是作为表达式而不是完整语句
            max_sum = (sum > max_sum)? sum : max_sum;
        }
        return max_sum;
    }
}
```
