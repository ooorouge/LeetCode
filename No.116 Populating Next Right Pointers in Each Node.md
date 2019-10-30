### 唯一核心语句：
* ![pictureExplanation](https://assets.leetcode.com/uploads/2019/02/14/116_sample.png)
```java
        if (root.right != null) {
            root.right.next = root.next != null ? root.next.left : null;
        }
```
```java
class Solution {
    public Node connect(Node root) {
        helper(root);
        return root;
    }
    public void helper(Node root) {
        if (root == null) {
            return ;
        }
        if (root.left != null) {
            root.left.next = root.right;
        }
        if (root.right != null) {
            root.right.next = root.next != null ? root.next.left : null;
        }
        helper(root.left);
        helper(root.right);
    }
}
```
