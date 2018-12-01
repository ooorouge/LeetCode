## 滑动窗口
* dict -> 模拟hash table
* res 
* start
* enumerate(s) for s = {'a', 'b', 'c'}
```
  i, val = enumerate[0]
  0, a
```
# 注意
* 第一版
```
if ch in d: start = max(start, d[ch]+1)
    res = max(res, i-start+1)    
```
* 第二版
```
if s[i] in usedChar and start <= usedChar[s[i]]:
    start = usedChar[s[i]] + 1
```
