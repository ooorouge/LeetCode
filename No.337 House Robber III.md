### No.337 House Robber III
* EMMMM有一个思路不一定对，遇到这种树的题，先试一试dfs的思路，搜到底再往上看，搜到底的写法这个题写的很清晰
* 伪代码大概是，先判断这个节点存在？不然返回0；
* 递归调用，参数是这个节点的左右子节点，用两个值接受递归的结果，然后处理当前节点的情况，因为在递归的时候，遇到节点不存在的情况才会第一次返回
* 所以第一次执行到节点内部的时候，应该是叶子节点，然后处理叶子节点，然后逐层向上
```java
class Solution {
    public int rob(TreeNode root) {
    	int[] maxVal = dpRob(root);
    	return Math.max(maxVal[0], maxVal[1]);
	}
	public int[] dpRob(TreeNode root) {
		if (root == null) {
			return new int[2];
		}
		int[] thisval = new int[2];
		int[] l = dpRob(root.left);
		int[] r = dpRob(root.right);
		thisval[0] = Math.max(l[0], l[1]) + Math.max(r[0], r[1]);
		thisval[1] = l[0] + r[0] + root.val;
		return thisval;
	}
}
```
