### No.44 Wildcard Matching 
* 第一种做法和NO 10的正则表达式匹配很像，用的DP，而且这次的DP更加清楚一些
* 第二个办法快了非常多，但是感觉。。很难想，所以，还是把这个题当作一道DP吧
```java
class Solution {
    public boolean isMatch(String s, String p) {
    int m=s.length(), n=p.length();
    boolean[][] dp = new boolean[m+1][n+1];
    dp[0][0] = true;
    for (int i=1; i<=m; i++) {
        dp[i][0] = false;
    }
    
    for(int j=1; j<=n; j++) {
        if(p.charAt(j-1)=='*'){
            dp[0][j] = true;
        } else {
            break;
        }
    }
    
    for(int i=1; i<=m; i++) {
        for(int j=1; j<=n; j++) {
            if (p.charAt(j-1)!='*') {
                dp[i][j] = dp[i-1][j-1] && (s.charAt(i-1)==p.charAt(j-1) || p.charAt(j-1)=='?');
            } else {
            //               任意字符串    0个
                dp[i][j] = dp[i-1][j] || dp[i][j-1];
            }
        }
    }
    return dp[m][n];
    }
}
---
* 第二个办法快非常多
```java
class Solution {
    public boolean isMatch(String s, String p) {
        
        int ss = 0, pp = 0, match = 0, starIdx = -1;
        
        while (ss < s.length()){
            
            // if both match, then increment both pointers
            if (pp < p.length() && (p.charAt(pp) == '?' || (s.charAt(ss) == p.charAt(pp)))){
                ss++;
                pp++;
            }
            
            // If * is encountered, mark the position of the *, but incremement pp, in case this * catches 0
            else if (pp < p.length() && p.charAt(pp) == '*'){
                starIdx = pp;
                match = ss;
                pp++;
            }
            
            // if the star is not catching 0, then increment match and set ss to that (since match is the last matched one)
            else if (starIdx != -1){
                pp = starIdx + 1;
                match++;
                ss = match;
            }
                
            // anything else is bad, return false
            else{
                return false;
            }
        }
        
        // Consume out any trailing *
        while (pp < p.length() && p.charAt(pp) == '*')
            pp++;
        
        return pp == p.length();
    }
}
```
