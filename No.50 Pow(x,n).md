### 指数函数
* [image](https://www.dropbox.com/s/udnbzx1ihzvc8dy/Screenshot%202018-02-08%2015.37.48.png?raw=1)
```java
public class Solution {
    public double myPow(double x, int n) {
        double ans = 1;
        
        //为了解决MIN_VALUE在abs之后overflow
        long absN = Math.abs((long)n);
        if (absN < 1 && n == Integer.MAX_VALUE) {}
        while(absN > 0) {
            if((absN&1)==1) ans *= x;
            absN >>= 1;
            x *= x;
        }
        return n < 0 ?  1/ans : ans;
    }
}
```
  
