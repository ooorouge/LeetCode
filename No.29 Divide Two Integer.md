### No.29 Divide Two Integer
* JAVA没有uint。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。
* c++
```c++
class Solution {
public:
    int divide(int dividend, int divisor) {
        if (dividend == INT_MIN && divisor == -1) {
            return INT_MAX;
        }
        long dvd = labs(dividend), dvs = labs(divisor), ans = 0;
        int sign = dividend > 0 ^ divisor > 0 ? -1 : 1;
        while (dvd >= dvs) {
            long temp = dvs, m = 1;
            while (temp << 1 <= dvd) {
                temp <<= 1;
                m <<= 1;
            }
            dvd -= temp;
            ans += m;
        }
        return sign * ans;
    }
};
```
* 这个办法能起效，在discuss里看到的，但是测试了一下
`Math.abs(Integer.MIN_VALUE)`还是一个负数，不知道为什么如果涉及到` a == Integer.MIN_VALUE `的时候怎么过的第一个判断
```java
class Solution {
    public int divide(int dividend, int divisor) {
        //System.out.println(Integer.MIN_VALUE - 1);
        //System.out.println(Integer.MAX_VALUE);
        if(dividend == Integer.MIN_VALUE && divisor == -1){
            return Integer.MAX_VALUE;
        }
        int a = Math.abs(dividend);
        int b = Math.abs(divisor);
        int res = 0;
        while(a - b >= 0){
            
            int x = 0;
            while( a - (b << 1 << x) >= 0){
                x++;
            }
            res += 1 << x;
            a -= b << x;
        }
        return (dividend >= 0) == (divisor >= 0) ? res :-res;
    }
}
```
