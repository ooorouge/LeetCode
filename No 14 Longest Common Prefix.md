- No 14 Longest Common Prefix
- python3里有一个很tricky的写法，对```strs: list[str]```进行```.sort()```于是排序之后，排序是按照字母权重的，等于是预先做了一次common prefix的识别

```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        strs.sort()
        s1, s2 = strs[0], strs[-1]
        
        for i, st in enumerate(s1):
            if s2[i] != st:
                return s2[:i]
            
        return s1
        
            
```

- 其他思路：
  - 我觉得可以直接把所有strs异或，然后看有多少位0，再从任意str直接取多少位就行了
  - 查找方法也可以优化，比如binary search：对单个str、或者对整体同时两两对比(？我觉得这样不太好）
