### Length Of Last Word
* 边界情况
  * `s == ' '`
  * `s == 'axa asd '`感觉并没有说明这种情况算什么
```java
class Solution {
    public int lengthOfLastWord(String s) {
        //edge
        if(s.length() == 0) return 0;
        int count = 0;
        int cur = s.length() - 1;
        char[] temp = s.toCharArray();
        while(cur >= 0){
            if(temp[cur] == ' '){
                break;
            }
            ++count;
            --cur;
        }
        return count;
    }
}
```
