### No.49 Group Anagrams
* 用hashmap的做法想到了，然后就是优化问题，第一个办法14ms,第二个办法7ms
```java
class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> ans = new HashMap<>();
        for (String s:strs) {
            int[] use = new int[26];
            for (int i = 0; i < s.length(); ++i) {
                use[s.charAt(i)-'a']++;
            }
            String ss = Arrays.toString(use);
            if (ans.containsKey(ss)) {
                ans.get(ss).add(s);
            } else {
                List<String> temp = new ArrayList<>();
                temp.add(s);
                ans.put(ss, temp);
            }
        }
        return new ArrayList<>(ans.values());
    }
}
```
---
* 这个方法确实很好，多看多学，有一点点First Missing Positive的感觉
```java
class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String,List<String>> map = new HashMap<>();
        for (String s : strs) {
            String code = getCode(s);
            map.putIfAbsent(code, new ArrayList<>());
            map.get(code).add(s);
        }
        
        return new ArrayList<>(map.values());
    }
    
    public String getCode(String s) {
        char[] freq = new char[26];
        for (char c : s.toCharArray()) freq[c-'a']++;
        
        return new String(freq);
    }
}
```
