### 事实上这道题还是在考重载比较函数
```java
class Solution {
    public String[] reorderLogFiles(String[] logs) {
        ArrayList<String> ans = new ArrayList<>();
        if (logs.length < 2) {return logs;}
        Queue<String> q = new LinkedList<>();
        for (String s : logs) {
            String[] s1 = s.split(" ");
            if ( s1[1].charAt(0) >= '0' && s1[1].charAt(0) <='9' ) {
                q.offer(s);
            } else {
                ans.add(s);
            }
        }
        ans.sort(new Comparator<String>() {
            @Override
            public int compare(String a, String b) {
                int s1 = a.indexOf(" ");
                int s2 = b.indexOf(" ");
                
                int preCompute = a.substring(s1+1).compareTo(b.substring(s2+1));
                if (preCompute == 0) return a.substring(0,s1).compareTo(b.substring(0,s2));
                return preCompute;
            }
        });
        while (!q.isEmpty()) {
            ans.add(q.poll());
        }
        
        return ans.toArray(new String[0]);
    }
}
```
