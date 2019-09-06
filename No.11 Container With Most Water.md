### Container With Most Water
* ![explanation](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg)
* 首先自己做了一个O(n^2) runtime 200ms
* 后来只用遍历一次的办法 runtime 2ms
---
#### 好的方法,总体思路最开始一个指向头，一个指向尾巴，由于短板限制了容量，所以只有移动短板才可能导致优化
```java
class Solution {
    public int maxArea(int[] height) {
        int left = 0;
        int right = height.length-1;
        int max = 0;
        while(left < right){
            max = Math.max(max, Math.min(height[left], height[right]) * (right - left));
            if(height[left] < height[right]){
                ++left;
            }else{
                --right;
            }
        }
        return max;
    }
}
```
---
#### 第一次直接写的一个套嵌遍历
```java
class Solution {
    public int maxArea(int[] height) {
        int len = height.length;
        int w = 0;
        int h = 0;
        int v = 0;
        
        for(int i = 0; i < len - 1; ++i){
            for(int j = i + 1; j < len; ++j){
                w = j - i;
                int temp = Math.min(height[i], height[j]) * w;
                v = (v < temp) ? temp : v;
            }
        }
        return v;
    }
}
```
