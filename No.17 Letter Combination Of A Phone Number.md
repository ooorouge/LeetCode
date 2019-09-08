### No.17 Letter Combination Of A Phone Number
* 做错的主要原因在不知道LinkedList方法.remove()其实是删除第一个并且返回其值，所以怎么遍历出了问题
* ![Description](http://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Telephone-keypad2.svg/200px-Telephone-keypad2.svg.png)
```java
class Solution {
    public List<String> letterCombinations(String digits) {
        LinkedList<String> ans = new LinkedList<String>();
        if(digits.isEmpty()) return ans;
        int[] dint = new int[digits.length()];
        for(int i = 0; i < digits.length(); ++i) {
            dint[i] = digits.charAt(i) - '0';
        }
        
        String[] map = new String[] {"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
        ans.add(""); 
        
        for(int i = 0; i < digits.length(); ++i) {
            int x = dint[i];
            while(ans.peek().length() == i) {
                String temp = ans.remove();
                for(char c : map[x].toCharArray()) {
                    ans.add(temp+c);
                }
            }
        }
        return ans;
    }
}
```
