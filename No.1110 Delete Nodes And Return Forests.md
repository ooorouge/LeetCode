### No.1110 Delete Nodes And Return Forests
* DFS的变种题型，主要是需要搜到叶节点才允许返回，所以其中有几行的写法非常重要
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
    List<TreeNode> ans;
    Set<Integer> del;
    public List<TreeNode> delNodes(TreeNode root, int[] to_delete) {  
        List<TreeNode> ans = new ArrayList<TreeNode>();
        Set<Integer> del = new HashSet<Integer>();
        if (root == null) {return ans;}
        for (int i = 0; i < to_delete.length; ++i) {
            del.add(to_delete[i]);
        }
        if (!del.contains(root.val)) ans.add(root);
        dfs(root, ans, del);
        return ans;
    }
    //这个函数是有返回的，不然递归调用的话不会add
    public TreeNode dfs(TreeNode root, List<TreeNode> ans, Set<Integer> del) {
        if (root == null) {return null;}
        root.left = dfs(root.left, ans, del);
        root.right = dfs(root.right, ans, del);
        if (del.contains(root.val)) {
            if (root.right != null) {ans.add(root.right);}        //!!!!!!!
            if (root.left != null) {ans.add(root.left);}          //!!!!!!!
            return null;
        }
        return root;
    }
}
```
