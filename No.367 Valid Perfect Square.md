### Valid Perfect Squre
* 用 / 是为了防止overflow
* mid = low + (high - low) / 2为了防止overflow
* + 1 - 1不添加的话，比如high=7,low=6,方向在6-7之间，一直循环
```java

    
class Solution {
    public boolean isPerfectSquare(int num) {
        if(num == 0) return false;

        int left = 1, right = num;
        
        while(left <= right){                       //<=配合+1-1收敛
            int mid = left + (right - left)/2;      //防止overflow
            if(mid > num / mid){                    //防止overflow
                right = mid - 1;                    //防止循环
            }else if(mid < num / mid){              //overflow
                left = mid + 1;                     //死循环
            }else{
                return num % mid == 0;
            }
        }
        return false;
    }
}
```
