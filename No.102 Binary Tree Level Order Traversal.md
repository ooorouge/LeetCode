### 思路是对的，就是用一个queue存当前节点的所有子节点，然后按照中左右
* 这个题和迷宫那个题一样，不能简单的
```java
while(!q.isEmpty()) {
  //do something
}
```
* 需要写成
```java
while (!q.isEmpty()) {
  int size = q.size();
  for (int i = 0; i < size; ++i) {
    //do something
  }
}
```
* 不然在同一层就会一直加一直减，起不到分层处理的作用
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
public class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        Queue<TreeNode> queue = new LinkedList<TreeNode>();
        List<List<Integer>> wrapList = new LinkedList<List<Integer>>();
        
        if(root == null) return wrapList;
        
        queue.offer(root);
        while(!queue.isEmpty()){
            int levelNum = queue.size();
            List<Integer> subList = new LinkedList<Integer>();
            for(int i=0; i<levelNum; i++) {
                if(queue.peek().left != null) queue.offer(queue.peek().left);
                if(queue.peek().right != null) queue.offer(queue.peek().right);
                subList.add(queue.poll().val);
            }
            wrapList.add(subList);
        }
        return wrapList;
    }
}
```
