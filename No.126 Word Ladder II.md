### 这个题比上一个难，需要打印path，所以还需要dfs
* distance哈希表的做法是为了防止获得的不是最短路径
```java
class Solution {
    public List<List<String>> findLadders(String beginWord, String endWord, List<String> wordList) {
        List<List<String>> ans = new ArrayList<>();
        if (wordList.size() == 0 || !wordList.contains(endWord)) {
            return ans;
        }
        Set<String> set = new HashSet<>(wordList);
        HashMap<String, List<String>> neighbor = new HashMap<>();
        HashMap<String, Integer> distance = new HashMap<>();
        set.add(beginWord);
        bfs(beginWord, endWord, neighbor, set, distance);
        dfs(beginWord, endWord, neighbor, distance, ans, new ArrayList<>());
        return ans;
    }
    public void bfs(String beginWord, String endWord, HashMap<String, List<String>> neighbor, Set<String> set, HashMap<String, Integer> distance) {
        for (String str : set) {
            neighbor.put(str, new ArrayList<>());
        }
        
        Queue<String> queue = new LinkedList<>();
        queue.offer(beginWord);
        distance.put(beginWord, 0);
        while (!queue.isEmpty()) {
            boolean found = false;
            int len = queue.size();
            for (int i = 0; i < len; ++i) {
                String start = queue.poll();
                List<String> neighbors = getNeighbors(start, set);
                int curlevel = distance.get(start);
                
                for (String str : neighbors) {
                    neighbor.get(start).add(str);
                    if (!distance.containsKey(str)) {
                        distance.put(str, curlevel+1);
                        if (!str.equals(endWord)) {
                            queue.offer(str);
                        } else {
                            found = true;
                        }
                    }
                }
            }
            if (found) {
                break;
            }
        }
        
    }
    
    public List<String> getNeighbors(String start, Set<String> set) {
        List<String> ans = new ArrayList<>();
        char[] chars = start.toCharArray();
        for (int i = 0; i < start.length(); ++i) {
            for (char j = 'a'; j <= 'z'; ++j) {
                if (chars[i] != j) {
                    char temp = chars[i];
                    chars[i] = j;
                    String stemp = String.valueOf(chars);
                    if (set.contains(stemp)) {
                        ans.add(stemp);
                    }
                    chars[i] = temp;
                }
            }
        }
        return ans;
    }
    
    public void dfs(String beginWord, String endWord, HashMap<String, List<String>> neighbor, HashMap<String, Integer> distance, List<List<String>> ans, List<String> sublist) {
        if (sublist.size() == 0) {
            sublist.add(beginWord);
        }
        if (beginWord.equals(endWord)) {
            ans.add(new ArrayList<>(sublist));
            return ;
        }
        for (String str : neighbor.get(beginWord)) {
            if (distance.get(str) == distance.get(beginWord) + 1) {
                sublist.add(str);
                dfs(str, endWord, neighbor, distance, ans, sublist);
                sublist.remove(sublist.size()-1);
            }
        }
    } 
}
```
