### No.45 Jump Game
* 这个题还是属于BFS和贪心算法都是好办法的题，写了2个，按照runtime从小到大排列，复习的时候注意比较，思考为什么
* 时间最少
```java
class Solution {
    public int jump(int[] nums) {
        if (nums.length < 2) {return 0;}
        int min = 0; 
        int cur = 0;
        int i = 0;
        int len = nums.length-1;
        
        while(i <= cur) {
            int far = cur;
            for (;i <= cur; ++i) {
                far = Math.max(far, nums[i]+i);
                if (far >= len) {
                    return min+1;
                }
            }
            ++min;
            cur = far;
        }
        return 100; //按照题目的说法，一定可以跳跃到终点，所以这一行随便写写
    }
}
```
* BFS
* 从末尾到头，代码最少， 但是执行次数最多，所以效率很低
```java
class Solution {
    public int jump(int[] nums) {
        int min = 0; int cur = 0;
        int len = nums.length-1;
        
        while(len > 0) {
            for (int i =0; i < len; ++i) {
                //从i=0往前搜索，看到的第一个符合条件的i就是能跳得最远的，所以不用Math.min
                if (nums[i] >= len - i) {
                    len = i;
                    min++;  
                    break;
                } 
            }
        }
        return min;
    }
}
```
