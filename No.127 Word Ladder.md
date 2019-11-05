### bfs,自己写的写法时间复杂度非常高。。。
```java
class Solution {
    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        if (wordList.size() == 0 || !wordList.contains(endWord)) {
            return 0;
        }
        Set<String> list = new HashSet<>(wordList);
        Queue<String> queue = new LinkedList<>();
        queue.offer(beginWord);
        int len = 1;
        while (!queue.isEmpty()) {
			len++;
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                String s = queue.poll();
                for (String neighbor : getNeighbors(list, s)) {
                    if (neighbor.equals(endWord))
                        return len;
                    queue.offer(neighbor);
                }
            }
        }
        return 0;
    }
     private Set<String> getNeighbors(Set<String> list, String s) {
        Set<String> res = new HashSet<>();
        char[] chars = s.toCharArray();
        for (int i = 0; i < s.length(); i++) {
            for (char ch = 'a'; ch <= 'z'; ch++) {
                if (chars[i] == ch) continue;
                char tmp = chars[i];
                chars[i] = ch;
                String word = new String(chars);
                if (list.remove(word)) res.add(word);
                chars[i] = tmp;
            }
        }
        return res;
    }
}
```
```java
class Solution {
    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        int ans = 0;
        if (wordList.size()==0 || !wordList.contains(endWord)) {
            return ans;
        }
        HashMap<String, Integer> counter = new HashMap<>();
        Queue<String> queue = new LinkedList<>();
        counter.put(beginWord, 1);
        queue.offer(beginWord);
        
        while (!queue.isEmpty()) {
            String cur = queue.poll();
            for (String str : wordList) {
                if (onediff(cur, str)) {
                    if (str.equals(endWord)) {
                        return counter.getOrDefault(cur,1)+1;
                    }
                    if (!counter.containsKey(str)) {
                        counter.put(str, counter.get(cur)+1);
                        queue.offer(str);
                    }
                }
            }
        }
        return ans;
    }
    public boolean onediff(String a, String b) {
        int len = a.length();
        int counter = 0;
        for (int i = 0; i < len; ++i) {
            if (a.charAt(i) == b.charAt(i)) {
                ++counter;
            }
        }
        return counter == (len - 1);
    }
}
```
