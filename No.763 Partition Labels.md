### 按照前面的字串里每个字符是不是只在这个字串中出现，划分字串
* 下面应该是O(n^2),O(n)
```java
class Solution {
    public List<Integer> partitionLabels(String S) {
        int len = S.length();
        if (len == 0) {return new ArrayList<Integer>();}
        int div = 1;
        int start = 0;
        List<Integer> ans = new ArrayList<>();
        while (div <= len) {
            HashSet<Character> set = new HashSet<>();
            for (char c : (S.substring(start, div).toCharArray())) {
                set.add(c);
            }
            if (help(S.substring(div, len), set)) {
                ans.add(div - start);
                start = div;
            }
            ++div;
        }
        return ans;
    }
    
    public boolean help(String s, HashSet<Character> set) {
        for (char c : s.toCharArray()) {
            if (set.contains(c)) {
                return false;
            }
        }
        return true;
    }
}
```
---
* 这个就是O(n)O(1)的
```java
public List<Integer> partitionLabels(String S) {
        if(S == null || S.length() == 0){
            return null;
        }
        List<Integer> list = new ArrayList<>();
        int[] map = new int[26];  // record the last index of the each char

        for(int i = 0; i < S.length(); i++){
            map[S.charAt(i)-'a'] = i;
        }
        // record the end index of the current sub string
        int last = 0;
        int start = 0;
        for(int i = 0; i < S.length(); i++){
            last = Math.max(last, map[S.charAt(i)-'a']);
            if(last == i){
                list.add(last - start + 1);
                start = last + 1;
            }
        }
        return list;
    }
    ```
