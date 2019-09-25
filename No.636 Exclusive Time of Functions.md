### No.636 Exclusive Time of Functions
* 给出一系列string "work#:{start|end}time" 来标记一件工作是否开始或者结束，统计每项工作消耗的时间
* !!!!!part[1] == "start" 或者 part[1] == "end"并不是单纯的只比较字符串，所以直接这样写会在第一个String出现EmptyStackException
```java
class Solution {
    public int[] exclusiveTime(int n, List<String> logs) {
        int[] ans = new int[n];
        if (logs.size() == 0) return ans;
        int lt = 0;
        Stack<Integer> stack = new Stack<>();
        for (String str:logs) {
            String[] part = str.split(":");
            int p0 = Integer.valueOf(part[0]);
            int p2 = Integer.valueOf(part[2]);
            if (part[1].equals("start")) {
                if (!stack.isEmpty()) {
                    ans[stack.peek()] += p2 - lt;  
                } 
                stack.push(p0);
                lt = p2;
            } else {
                ans[stack.pop()] += p2 - lt + 1;
                lt = p2 + 1;
            }
        }
        return ans;
    }
}
```
