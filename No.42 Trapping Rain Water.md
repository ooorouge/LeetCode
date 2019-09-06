### Trapping Rain Water
* 类似于Container With Most Water，但是中间出现了间隔，要麻烦非常多
* ![Description](https://assets.leetcode.com/uploads/2018/10/22/rainwatertrap.png)
```java
class Solution {
    public int trap(int[] h) {
        if (h.length < 3) return 0;
        int res = 0;
        int l = 0; 
        int r = h.length - 1; 

        while(l < r && h[l] <= h[l+1]) ++l;
        while(l < r && h[r] <= h[r-1]) --r;

        while(l < r){
            int left = h[l];
            int right = h[r];
            //这个判断非常关键，举例如下
            // * ！
            // * x *
            // * * * 这种情况下，如果从长板往短板数装水量，数到的是3-1=2，实际上只能装一格
            if(left <= right){
                while (l < r && left > h[++l]) {
                    res += left - h[l];
                }
            } else{
                while (l < r && right > h[--r]) {
                    res += right - h[r];
                }
            }
        }
        return res;
    }
}
```
