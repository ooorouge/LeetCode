### No.22 Generate Parentheses
* backtracking回溯算法，还有更多的[典型回溯算法](https://www.geeksforgeeks.org/top-20-backtracking-algorithm-interview-questions/)
```java
//这个空间复杂度很高，因为在回溯的过程中保存了很多种情况的数据
class Solution {
    public List<String> generateParenthesis(int n) {
        //第一个问题，StringBuilder没有.add()方法，然后第二个问题，为什么StringBuilder需要设置长度
        List<String> ans = new ArrayList<String>();
        if (n == 0) {ans.add("");return ans;}
        ansFinder(ans, new StringBuilder(), 0, 0, n);
        return ans;
    }
    public void ansFinder(List<String> ls, StringBuilder s, int left, int right, int max) {
        if (left == max && left == right) {
            ls.add(s.toString());
        }
        if (left < max) {
            s.append("(");
            ansFinder(ls, s, left+1, right, max);
            //原因是这样，这条节点的一种分支已经靠上面的语句进行下去了，当前的节点需要剪掉已经修改过的痕迹，方便继续寻找其他当前节点下的情况
            //第二个原因，String不用写下面这一句的原因是，在Java里的String的concat其实是return new String()
            //然而StringBuilder是在原值上做修改的，所以要维护原值
            s.setLength(s.length()-1);
        }
        if (right < left) {
            s.append(")");
            ansFinder(ls, s, left, right+1, max);
            s.setLength(s.length()-1);
        }
    }
}
```
