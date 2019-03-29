* No 9 Palindrome Number 

* easy

* 判断是不是回文

  * 负数不是
  * 0是
  * 涉及到`%10` `//10`的操作要注意10和10的整数倍
  * 也有人直接算得反序的数再比较的，主要想的是万一反序太长，那么算一半可能会快一点？

  ```python
  import math
  class Solution:
      def isPalindrome(self, x: int) -> bool:
          y = x
          r = 0
          res = 0
          if x < 0: return False
          elif x == 0: return True
          else:
              L = int(bitofx(x))
              ODD = L & 1
              L = L // 2            
              while r != L:
                  res = res*10 + y % 10
                  y = y // 10                
                  r = r + 1
              if ODD == 1:
                  return res==y//10
              else:
                  return res==y
                      
  def bitofx(x: int) -> int:
      return math.log(x, 10) + 1
  ```

* 出错的地方有：
  * L的位置没放对，负数参与了对数运算
  * `y//10`放在了`res = res*10 + y % 10`前面
* 最近看的奇怪的东西
  * 树状数组
  * DP
