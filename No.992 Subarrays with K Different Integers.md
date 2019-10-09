### 这个题可以变种成，A是个String，求子串，把A改成char[]就好了，一样的做
* 这个方法在LC这道题的环境下遇到很长，K很大的时候会TLE，但是是OA的写法
```java
class Solution {
    public int subarraysWithKDistinct(int[] A, int K) {
        if (K == 0 || K > A.length) {return 0;}
        int count = 0;
        int len = K;
        while(len <= A.length) {
            for (int i = 0; i <= A.length-len; ++i) {
                if (helper(Arrays.copyOfRange(A, i, i+len), K))                       
                {
                    count++;
                }
            }
            len++;
        }
        return count;
    }
    public boolean helper(int[] A, int K) {
        HashSet<Integer> hset = new HashSet<>();
        for (int i = 0; i < A.length; ++i) {
            hset.add(A[i]);
        }
        if (hset.size() == K) {return true;}
        return false;
    }
}
```
