### 主要就是看怎么写的更好
* 只有一个问题，每个子树都必须是平衡的，所以不能只从root的角度看是不是平衡
```java
class Solution {
    public boolean isBalanced(TreeNode root) {
        if (root == null) return true;
        
        int left = getDepth(root.left);
        int right = getDepth(root.right);
        
        if (Math.abs(left - right) > 1) return false;
        
        return isBalanced(root.left) && isBalanced(root.right);
    }
    
    public int getDepth(TreeNode root) {
        if (root == null) return 0;
        
        int left = getDepth(root.left);
        int right = getDepth(root.right);
        
        return Math.max(left, right) + 1;
    }
}
```
