### 杨辉三角
* `ans.add(new ArrayList<>(cur));`如果不是new,那么一直加入的都是cur的地址，n个list都是最后一个
* `List<Integer> sub = new ArrayList<>(cur);`要不然会变成1，11，121，1341，14891
```java
class Solution {
    public List<List<Integer>> generate(int n) {
        List<List<Integer>> ans = new ArrayList<>();
        if (n == 0) {
            return ans;
        }
        List<Integer> cur = new ArrayList<>();
        for (int i = 0; i < n; ++i) {
            cur.add(1);
            List<Integer> sub = new ArrayList<>(cur);
            for (int j = 1; j < sub.size()-1; ++j) {
                cur.set(j, sub.get(j-1)+sub.get(j));
            }
            ans.add(new ArrayList<>(cur));
        }
        return ans;
    }
}
```
