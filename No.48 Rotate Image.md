### No.48 Rotate Imgae
* 遇到这种情况，画个图来写坐标表达式
```java
class Solution {
    public void rotate(int[][] m) {
        if (m.length < 2) {return;}
        int a = 0;
        int b = m.length-1;
        while(a<b){
            for(int i=0;i<(b-a);++i){
                int temp;
                //swap(m[a][a+i], m[a+i][b]);
                temp = m[a+i][b];
                m[a+i][b] = m[a][a+i];
                m[a][a+i] = temp;
                //swap(m[a][a+i], m[b][b-i]);
                temp = m[b][b-i];
                m[b][b-i] = m[a][a+i];
                m[a][a+i] = temp;
                //swap(m[a][a+i], m[b-i][a]);
                temp = m[b-i][a];
                m[b-i][a] = m[a][a+i];
                m[a][a+i] = temp;
            }
            ++a;
            --b;
        }
    }
}
```
