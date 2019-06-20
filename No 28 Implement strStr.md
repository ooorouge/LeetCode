* 本身很简单，有空了把KMP用上

* 有一个问题，为什么不是```(j+1 == n)```
```c++
class Solution {
public:
    int strStr(string haystack, string needle) {
        int m = haystack.size(), n = needle.size();
        if(n == 0) {
            return 0;
        }
        for(int i = 0; i < m - n + 1; ++i) {
            if(haystack[i] == needle[0]) {
                int j = 0;
                for(; j < n; ++j) {
                    if(haystack[i+j] != needle[j]){
                        break;
                    }
                }
                if(j == n){return i;}
            }
        }
        return -1;
    }
};
```
