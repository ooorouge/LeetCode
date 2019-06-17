* No 9 Palindrome Number 

* easy

* 罗马数字的一般都是大数在左，如果大数在右，那么左边的小数只可能有一位(不然会出现XIIV之类)
* 以下是discuss里的一个答案

```c++
class Solution {
public:
    int romanToInt(string s) {
        if(s.empty()){return 0;}
        unordered_map<char, int> T = { { 'I' , 1 },
                                   { 'V' , 5 },
                                   { 'X' , 10 },
                                   { 'L' , 50 },
                                   { 'C' , 100 },
                                   { 'D' , 500 },
                                   { 'M' , 1000 } };                                  
        int sum = T[s.back()];
        for (int i = s.length() - 2; i >= 0; --i) 
        {
           if (T[s[i]] < T[s[i + 1]])
           {
               sum -= T[s[i]];
           }
           else
           {
               sum += T[s[i]];
           }
        }
        return sum;
    }
}
```
* 用一个map来做这种事 stl
* 反序对于重复出现的数字判断是属于 小数在大数左边 or 小数出现在大数右边 更方便
