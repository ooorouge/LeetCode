### No.55 Jump Game
* 这个题有很多种写法，第一种写法和JumpGame ii写法很类似，不过效率非常不高，这个题有一种思路就是BFS，但是效率最高的写法是贪心算法
* 第一种写法，贪心算法，效率最高
```java
class Solution {
    public boolean canJump(int[] A) {
    int max = 0;
    for(int i=0;i<A.length;i++){
        if(i>max) {return false;}
        max = Math.max(A[i]+i,max);
    }
    return true;
    }
}
```
* 第二个写法，从后往前的BFS
```java
class Solution {
    public boolean canJump(int[] nums) {
        if (nums.length < 2) {return true;}
        if (nums[0] == 0) {return false;}
        if (nums[0] >= nums.length) {return true;}
        
        int len = nums.length - 1;
        boolean t = true;
        while (t && len > 0) {
            t = false;
            for (int i = 0; i < len; ++i) {
                if (nums[i] + i >= len) {
                    t = true;
                    len = i;
                    break;
                }
            }
        }
        return t;
    }
}
```
