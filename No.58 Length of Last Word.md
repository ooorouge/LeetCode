### No.58 Length of Last Word
* 这个题就是要考虑边界条件，把边界条件给考虑全就行了
```java
class Solution {
    public int lengthOfLastWord(String s) {
        int ans = 0;
        char[] c = s.toCharArray();
        for (int i = c.length-1; i >= 0; --i) {
            if (i == c.length-1 && c[i] == ' ') {
                while (c[i] == ' ' && i > 0) {--i;}
                if (i == 0 && c[0] == ' ') {
                    return 0;
                }
            }
            if (c[i] != ' ') {
                ++ans;
            }
            else {
                break;
            }
        }
        return ans;
    }
}
```
