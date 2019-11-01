### 和另外一个遍历差不多，stackoverflow的问题主要在于无法退出
* 从Postorder找根，post序 left -> right -> root,从inorder找出范围，限定下一步postorder subarray的范围
* postorder最后一个是根，p[end]对应i里的索引,rootloc - istart是左边有多少个，所以ps到pstart + rootloc - istart - 1就是po序列左边subarray
* pstart + rootloc - istart 到 pend-1就是右边的po的subarray
* in定位和之前一样，找到根的位置，根左边是in左subarray,右边是in右subarray
```java
class Solution {
    public TreeNode buildTree(int[] in, int[] po) {
        if (in.length == 0 || po.length == 0) {
            return null;
        }
        Map<Integer, Integer> imap = new HashMap<>();
        for (int i = 0; i < in.length; ++i) {
            imap.put(in[i], i);
        }
        TreeNode root = helper(in, po, 0, po.length-1,0, in.length, imap);
        return root;
    }
    public TreeNode helper(int[] in, int[] po, int pstart, int pend, int istart, int iend, Map<Integer, Integer> imap) {
        if (istart > iend || pstart > pend) {
            return null;
        }
        int rootloc = imap.get(po[pend]);
        TreeNode root = new TreeNode(po[pend]);
        root.left = helper(in, po, pstart, pstart+rootloc-istart-1, istart, rootloc, imap);
        root.right = helper(in, po, pstart+rootloc-istart, pend-1, rootloc+1, iend, imap);
        return root;
    }
}
```
