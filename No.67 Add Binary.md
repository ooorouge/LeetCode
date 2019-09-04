### Add Binary
* 之前做过，大概就是这么写的，直接从discuss找了个思路一样的
* StringBuilder是mutable String immutable
```java
class Solution {
    public String addBinary(String a, String b) {
        if (a == null || b == null)
            return a == null ? b : a;

        final StringBuilder sb = new StringBuilder();
        int i = a.length() - 1;
        int j = b.length() - 1;
        int carry = 0;

        while (i >= 0 || j >= 0) {

            int sum = carry;
            if (j >= 0) sum += b.charAt(j--) - '0';  // subtract 0 to get the int value of char from ascii
            if (i >= 0) sum += a.charAt(i--) - '0';

            sb.append(sum % 2);
            carry = sum/2;
        }

        if(carry != 0) sb.append(carry);
        return sb.reverse().toString();
    }
}
```
