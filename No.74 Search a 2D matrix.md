### No.74 Search a 2D Matrix
* 多看，多学
```java
class Solution {
    public boolean searchMatrix(int[][] m, int target) {
        if (m.length == 0 || m[0].length == 0) {return false;}
        if (target < m[0][0] || target > m[m.length-1][m[0].length-1]) {return false;}
        int r = 0;
        int c = m[0].length - 1;
        boolean f = false;
        while (r < m.length && c > -1) {
            int tar = m[r][c];
            if (target < tar) {
                --c;
            }
            if (target > tar) {
                ++r;
            }
            else if (target == tar) {
                return true;
            }
        }
        return false;
    }
}
```
