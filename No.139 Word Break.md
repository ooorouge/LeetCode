### dp
* 模式在于对s的每一个字符，都尝试找以他开始的每个可能的wordDict里的string，主要比较麻烦的是索引，dp[i+str.length()], 然后substring(i)
* 但是这个题有个问题，冗余的string出现在wordDict里也算对
```java
class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        int slen = s.length();
        boolean[] dp = new boolean[slen+1];
        dp[0] = true;
        
        for (int i = 0; i <=  slen; ++i) {
            if (!dp[i]) {
                continue;
            } else {
                
                String substr = s.substring(i);
                for (String str : wordDict) {
                    if (substr.startsWith(str)) {
                        dp[i+str.length()] = true;
                    }
                }
            }
        }
        return dp[slen];
    }
}
```
