### Merge Sorted Array
* 感觉这个题考察的点是数组扩容，Java似乎可以直接扩容还是怎么回事
* 这个题目的是将B merge到 A 所以在while判断里只需要监控B剩余的长度，边界情况A长度=0的时候直接复制B
```java
class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        while(n>0){
            nums1[m+n-1] = ( m==0 || nums1[m-1] < nums2[n-1]) ? nums2[--n] : nums1[--m];
        }
    }
}
```
