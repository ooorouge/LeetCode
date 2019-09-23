### No.32 Longest Valid Parentheses
* 可以用stack来做，但是也可以用DP做，从后往前DP，比如dp[i]，s的i-1个字符是'(',那么dp[i] = 0;
* 如果s[i-1] == ')'然后s[i-2] == '(',dp[i] = dp[i-2] + 2;
* 如果s[i-1] == ')'然后s[i-2] == ')',然后s[i-2-dp[i-2]] == '(' dp[i] = dp[i-2-dp[i-2]] + 2 + dp[i-1]
*                                                                          ^前段        ^i-1   ^中段
```java
class Solution {
    public int longestValidParentheses(String s) {
        int ans = 0;
        Stack<Integer> s1 = new Stack<>();
        s1.push(-1);
        for (int i = 0; i < s.length(); ++i) {
            if (s.charAt(i) == '(') s1.push(i);
            else {
                s1.pop();
                if (s1.empty()) {
                    s1.push(i);
                } else {
                    ans = Math.max(ans, i - s1.peek());
                }
            }
        }
        return ans;
    }
}
```
