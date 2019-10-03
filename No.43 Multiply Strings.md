### No.43 Multiply Strings
* 这个题还是画图分析index怎么写最好
* ![huatu](https://drscdn.500px.org/photo/130178585/m%3D2048/300d71f784f679d5e70fadda8ad7d68f)
```java
class Solution {
    public String multiply(String num1, String num2) {
        if (num1.length() == 0 || num2.length() == 0) {return "0";}
        int[] ans = new int[num1.length()+num2.length()];
        for (int i = num1.length()-1; i > -1; --i) {
            for (int j = num2.length()-1; j > -1; --j) {
                int k = (num1.charAt(i) - '0') * (num2.charAt(j) - '0');
                k = k + ans[i+j+1];           //!!!!!!!!!!
                ans[i+j] += (k/10);           //!!!!!!!!!!
                ans[i+j+1] = (k%10);
            }
        }
        StringBuilder sb = new StringBuilder();
        boolean flag = true;
        for (int i = 0; i < ans.length; ++i) {
            if (flag && ans[i] == 0 && i < ans.length -1) {
                continue;
            }
            if (flag && ans[i] == 0 && i == ans.length -1) {
                sb.append(ans[i]);
                break;
            }
            flag = false;
            sb.append(ans[i]);
        }
        return sb.toString();
    }
}
```
