* No 7 Reverse Integer 

  * easy

  * 要求在[-2^31, 2^31-1] 换句话说在long long integer内

    * 有一些语言越界之后数值会变，可以直接靠验算比如

      ```java
      int tail = x % 10;
      int newResult = result * 10 + tail;
      if ((newResult - tail) / 10 != result)
         { return 0; }
      ```

      解决

  * 第一版

    * 先把每个位置上的数字求出来
    * 反着乘回去
    * 10/0/负数等特殊数据除了问题
    * 坏处：runtime大，memory差不多？

  * 第二版

    * 先`str`然后`[::-1]`负序再`int`然后判断添加上符号
    * 好像是目前runtime和memory最好，区别不大，不过用了很多builtins

  * 第三版以至以后

    * 和第一版相同，但是每求得一个数字就用上

      ```python
      y = abs(x)
      while y != 0:
          rest = rest*10 + y%10
          y = y//10
      ```

      `abs`不能少，这样每一步都能用上不需要再写个循环和算10的幂

    * 第二，用flags标记正负

      ```python
      flags = (1 if x>= 0 else -1)
      ```

* 其余的奇怪收获
  * http://www.matrix67.com/blog/page/173
  * <<编程之美>>