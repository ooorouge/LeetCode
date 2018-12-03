## 找出需要的indice
* O(lg(m+n))意味着binary search相关，而且要把两个array一起搜
```
        imin, imax, half = 0, m, int((m+n)/2)
        while imin <= imax:
        	i = (imin + imax) / 2
        	j = half - i
```
* 还有就是输出问题，谨慎考虑 
``` 
    i, j = 0, 0 
    i, j = m, n
````
* m+n+1 / 2 和 m+n / 2 两种分组的返回值是不一样的
