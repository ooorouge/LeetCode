### Plus One
```java
class Solution {
    public int[] plusOne(int[] digits) {
       //进位
        int cur = digits.length - 1;
        boolean jinwei = true;
        while(jinwei){
            if(cur >= 0){
                jinwei = !(digits[cur] < 9);
                digits[cur] = (digits[cur]+1) % 10;
                --cur;
                continue;
            }
            else{
                int[] extended = new int[digits.length+1];
                extended[0] = 1;
                System.arraycopy(digits, 0, extended, 1, digits.length);
                return extended;
            }
        }
        return digits;
    }
}
```
