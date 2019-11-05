### 这个题的主要目的就是看能不能写一个O(n)的写法
```java
class Solution {
    public int maxProfit(int[] prices) {
        int max = 0;
        if (prices.length == 0) {
            return 0;
        }
        int minprice = prices[0];
        for (int i = 1; i < prices.length; ++i) {
            if (prices[i] < minprice) {
                minprice = prices[i];
            } else if (prices[i] - minprice > max) {
                max = prices[i] - minprice;
            }
        }
        return max;
    }
}
```
