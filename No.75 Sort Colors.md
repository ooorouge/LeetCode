### 仔细审题，这个题只会有1，2，0三个数字，然后edge case其实也没考虑，不过这道题考虑因为return void才没有问题
* 第一个办法是扫一遍，保存0有多少个，1有多少个，2有多少个
* 第二个办法是两个指向首尾的指针，找到0，交换，然后判断交换后的是不是2，这个第二个if，第一个作用是判断当前i，第二个作用是在交换了i和首之后
* 判断是不是把2给交换到了当前位置，所以第一个if里不需要动index，第二个里需要`--index`
```java
class Solution {
    public void sortColors(int[] nums) {
    // 1-pass
    int p1 = 0, p2 = nums.length - 1, index = 0;
    while (index <= p2) {
        if (nums[index] == 0) {
            nums[index] = nums[p1];
            nums[p1] = 0;
            ++p1;
            
        }
        if (nums[index] == 2) {
            nums[index] = nums[p2];
            nums[p2] = 2;
            --p2;
            
            // ######
            --index;
            // ######
        }
        ++index;
        }
    }
}
```
