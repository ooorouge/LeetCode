### No.104 Maximum Depth of Binary Tree
* 递归，然后很常见的还有判断是否平衡啊，是否symmetry之类的
```java
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public int maxDepth(TreeNode root) {
        if (root == null) return 0;
        else {
            return countDown(root);
        }
    }
    public int countDown(TreeNode node) {
        if (node == null) return 0;
        else if (node.left == null && node.right == null) return 1;
        else {
            return Math.max(1+countDown(node.left), 1+countDown(node.right));
        } 
    }
}
```
