### 只知道一种遍历出来的结果构建的二叉树是不准确的，通过两个不同的遍历顺序产生的遍历结果可以正确的还原一个二叉树
* preorder出现的次序是 root -> left -> right，inorder出现的次序是 left -> root -> right
* p序无法知道哪些是左，哪些是右，i序无法知道哪些是根
* 但是无法知道哪些是左子树，哪些是右子树，结合inorder，在preorder里的每个值，出现在inorder里时inorder里这个值的左边就是左子树，右边就是右子树
* map的使用用来定位p里的每个元素在i里的位置，节约遍历浪费的时间，但是多用了空间
```java
class Solution {
    public TreeNode buildTree(int[] p, int[] i) {
        if (p.length == 0 || i.length == 0) {
            return null;
        }
        Map<Integer, Integer> imap = new HashMap<>();
        for (int ii = 0; ii < i.length; ++ii) {
            imap.put(i[ii], ii);
        }
        
        TreeNode root = helper(p, i, 0, 0, i.length, imap);
        return root;
    }
    public TreeNode helper(int[] p, int[] i, int pstart, int istart, int iend, Map<Integer, Integer> imap) {
        if (pstart >= p.length || istart >= i.length || iend < 0) {
            return null;
        }
        if (istart >= iend) {
            return null;
        }
        int rootloc = imap.get(p[pstart]);
        TreeNode root = new TreeNode(p[pstart]);
        root.left = helper(p, i, pstart+1, istart, rootloc, imap);
        root.right = helper(p, i, pstart+rootloc-istart+1, rootloc+1, iend, imap);
        return root;
    }
}
```
