* 更快的办法是不要用map,每一次创建一个新的int[26]来判断，而且int[i]的值是Math.min
```java
class Solution {
    public List<String> commonChars(String[] A) {
        List<String> ans = new ArrayList<>();
        if (A.length == 0) {
            return ans;
        }
        if (A.length == 1) {
            for (int i = 0; i < A[0].length(); ++i) {
                ans.add(String.valueOf(A[0].charAt(i)));
            }
            return ans;
        }
        char[] c0 = A[0].toCharArray();
        Map<Character, Integer> map = new HashMap<>();
        for (int i = 0; i < c0.length; ++i) {
            if (!map.containsKey(c0[i])) {
                map.put(c0[i], 1);
            } else {
                map.put(c0[i], map.get(c0[i])+1);
            }
        }
        for (int i = 1; i < A.length; ++i) {
            Map<Character, Integer> tempmap = new HashMap<>();
            char[] c = A[i].toCharArray();
            for (int j = 0; j < c0.length; ++j) {
                if (!tempmap.containsKey(c[j])) {
                    tempmap.put(c[j], 1);
                } else {
                    tempmap.put(c[j], tempmap.get(c[j])+1);
                }
            }
            List<Character> toRemove = new ArrayList<>();
            for (char str : map.keySet()) {
                if (tempmap.containsKey(str)) {
                    //只记录最小的
                    if (tempmap.get(str) < map.get(str)) {
                        map.put(str, tempmap.get(str));
                    }
                } else {
                    //这里直接map.remove会出现concurrentModificatException
                    toRemove.add(str);
                }
            }
            for (char remove : toRemove) {
                map.remove(remove);
            }
        }
        for (char c : map.keySet()) {
            int howmany = map.get(c);
            for (int i = 0; i < howmany; ++i) {
                ans.add(String.valueOf(c));
            }
        }
        return ans;
    }
}
```
