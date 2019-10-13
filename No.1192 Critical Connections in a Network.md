### 这个问题就是Tarjan algorithm
```java
class Solution {
    public List<List<Integer>> criticalConnections(int n, List<List<Integer>> connections) {
        List<Integer>[] graph = new ArrayList[n];
        for (int i = 0; i < n; ++i) {
            graph[i] = new ArrayList<>();
        }
        for (List<Integer> conn : connections) {
            graph[conn.get(0)].add(conn.get(1));
            graph[conn.get(1)].add(conn.get(0));
        }
        int timer = 0;
        List<List<Integer>> ans = new ArrayList<>();
        boolean[] seen = new boolean[n];
        int[] timestamp = new int[n];
        dfs(-1, 1, seen, timestamp, timer, ans, graph);
        return ans;
    }
    
    public void dfs(int parent, int node, boolean[] seen, int[] timestamp, int timer, List<List<Integer>> ans, List<Integer>[] graph) {
        seen[node] = true;
        timestamp[node] = timer++;
        int current = timestamp[node];
        
        for (int in : graph[node]) {
            if (in == parent) {continue;}
            if (!seen[in]) {dfs(node, in, seen, timestamp, timer, ans, graph);}
            timestamp[node] = Math.min(timestamp[node], timestamp[in]);
            if (current < timestamp[in]) {
                List<Integer> newl = new ArrayList<>();
                newl.add(node);newl.add(in);
                ans.add(newl);
            }
        }
    }
    
}
```
