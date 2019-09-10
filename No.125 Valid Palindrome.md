### No.125 Valid Palindrom
* 这个问题其实并不是用stack最方便，直接用两个指向首尾的index其实最方便
```java
class Solution {
    public boolean isPalindrome(String s) {
        char[] c = s.toCharArray();
        if(c.length < 2) return true;
        //Character.isLetterOrDigit() 和 Character.toLowerCase() 都是Character下的方法
        for(int i = 0, j = c.length - 1; i <= j;) {
            if ( !Character.isLetterOrDigit(c[i]) ) ++i;
            else if ( !Character.isLetterOrDigit(c[j]) ) --j;
            else {
                if (Character.toLowerCase(c[i++]) != Character.toLowerCase(c[j--])) return  false;
            }
        }
        return true;
    }
}
```
