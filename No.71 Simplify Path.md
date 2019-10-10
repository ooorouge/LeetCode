### 用栈做
* 这个题继续发现`str == "aaaaa"`和`str.equals("aaaaa")`是不一样的，会检查存储位置
```java
class Solution {
    public String simplifyPath(String path) {
        Stack<String> st = new Stack<>();
        String[] ss = path.split("/");
        for (String s:ss) {
            if (s.equals(".") || s.equals("/") || s.equals("")) {
                continue;
            } else if (s.equals("..")) {
                if (!st.isEmpty()) {
                    st.pop();
                }
            } else {
                st.push(s);
            }
        }
        StringBuilder sb = new StringBuilder();
        if (st.isEmpty()) {
            return "/";
        }
        while (!st.isEmpty()) {
            sb.insert(0, "/"+st.pop());
        }
        return sb.toString();
    }
}
```
