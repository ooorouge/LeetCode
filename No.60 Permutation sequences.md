### No.60 Permutation sequences 
* 土办法，而且TLE，就是DFS，下面的这个dfs是对的，就是TLE
```java
class Solution {
    public String getPermutation(int n, int k) {
        List<List<Integer>> ans = new ArrayList<>();
        for (int i = 1; i <= n; ++i) {
            dfs(ans, i, n, new HashSet<>(), new ArrayList<>(), k);
        }
        StringBuilder sb = new StringBuilder();
        for (int i : ans.get(k-1)) {
            sb.append(i);
        }
        return sb.toString();
    }
    public void dfs(List<List<Integer>> ans, int start, int n, HashSet<Integer> set, List<Integer> l, int k) {
        if (set.size() == 0) {
            set.add(start);
            l.add(start);
        }
        if (set.size() == n) {
            ans.add(new ArrayList<>(l));
            if (ans.size() == k) {
                return;
            }
        }
        for (int i = 1; i <= n; ++i) {
            if (!set.contains(i)) {
                set.add(i);
                l.add(i);
                dfs(ans, start, n, set, l, k);
                set.remove(i);
                l.remove(l.size()-1);
            }
        }
    }
}
```
* 其实这个题的每个坐标都能算出来
```java
public class Solution {
public String getPermutation(int n, int k) {
    int pos = 0;
    List<Integer> numbers = new ArrayList<>();
    int[] factorial = new int[n+1];
    StringBuilder sb = new StringBuilder();
    
    // create an array of factorial lookup
    int sum = 1;
    factorial[0] = 1;
    for(int i=1; i<=n; i++){
        sum *= i;
        factorial[i] = sum;
    }
    // factorial[] = {1, 1, 2, 6, 24, ... n!} 这一步为了避免反复算阶乘，节约空间和时间
    
    // create a list of numbers to get indices
    for(int i=1; i<=n; i++){
        numbers.add(i);
    }
    // numbers = {1, 2, 3, 4} 为了方便删除
    
    k--;
    
    for(int i = 1; i <= n; i++){
        int index = k/factorial[n-i];
        sb.append(String.valueOf(numbers.get(index)));
        numbers.remove(index);
        k-=index*factorial[n-i];
    }
    
    return String.valueOf(sb);
}
```
