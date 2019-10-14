### 先序遍历创建，中左右
* 写了一行`private static int index = 0`的时候一直submit不成功，老实一点，不要写了
```java
class Solution {
    int index = 0;
    
    public TreeNode bstFromPreorder(int[] preorder) {
        return getPreOrderNode(preorder, Integer.MIN_VALUE, Integer.MAX_VALUE);
    }
    
    public TreeNode getPreOrderNode(int[] preorder, int min, int max) {
        if(index >= preorder.length) {
            return null;
        }
        
        if(preorder[index] < min || preorder[index] > max) {
            return null;
        }
        
        int val = preorder[index];
        TreeNode node = new TreeNode(val);
        
        index++;
        
        node.left = getPreOrderNode(preorder, min, val);
        node.right = getPreOrderNode(preorder, val, max);
        
        return node;
    }
}
```
