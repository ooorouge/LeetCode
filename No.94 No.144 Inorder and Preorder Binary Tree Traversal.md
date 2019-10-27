### three traversals
* ![image](https://media.geeksforgeeks.org/wp-content/cdn-uploads/2009/06/tree12.gif)
* (a) Inorder (Left, Root, Right) : 4 2 5 1 3
* (b) Preorder (Root, Left, Right) : 1 2 4 5 3
* (c) Postorder (Left, Right, Root) : 4 5 2 3 1
* Breadth First or Level Order Traversal : 1 2 3 4 5
---
* inorder
* 第一可以递归，第二可以用stack，第三可以用Morris Traversal
```java
public List < Integer > inorderTraversal(TreeNode root) {
        List < Integer > res = new ArrayList < > ();
        helper(root, res);
        return res;
    }

    public void helper(TreeNode root, List < Integer > res) {
        if (root != null) {
            if (root.left != null) {
                helper(root.left, res);
            }
            res.add(root.val);
            if (root.right != null) {
                helper(root.right, res);
            }
        }
    }
```
* stack
```java
public List < Integer > inorderTraversal(TreeNode root) {
        List < Integer > res = new ArrayList < > ();
        Stack < TreeNode > stack = new Stack < > ();
        TreeNode curr = root;
        while (curr != null || !stack.isEmpty()) {
            while (curr != null) {
                stack.push(curr);
                curr = curr.left;
            }
            curr = stack.pop();
            res.add(curr.val);
            curr = curr.right;
        }
        return res;
    }
```
* Morris Traversal
```java
public List < Integer > inorderTraversal(TreeNode root) {
        List < Integer > res = new ArrayList < > ();
        TreeNode curr = root;
        TreeNode pre;
        while (curr != null) {
            if (curr.left == null) {
                res.add(curr.val);
                curr = curr.right; // move to next right node
            } else { // has a left subtree
                pre = curr.left;
                while (pre.right != null) { // find rightmost
                    pre = pre.right;
                }
                pre.right = curr; // put cur after the pre node
                TreeNode temp = curr; // store cur node
                curr = curr.left; // move cur to the top of the new tree
                temp.left = null; // original cur left be null, avoid infinite loops
            }
        }
        return res;
    }
```
---
* preorder
* 可以用递归，或者用stack
```java
public List<Integer> preorderTraversal(TreeNode root) {
        List<Integer> ans = new ArrayList<>();
        if (root == null) {
            return ans;
        }
        helper(ans, root);
        return ans;
    }
    public void helper(List<Integer> ans, TreeNode root) {
        if (root != null) {
            ans.add(root.val);
        }
        if (root.left != null) {
            helper(ans, root.left);
        }
        if (root.right != null) {
            helper(ans, root.right);
        }
    }
```
---
```java
public List<Integer> preorderTraversal(TreeNode root) {
    List<Integer> result = new LinkedList<>();
    Deque<TreeNode> stack = new LinkedList<>();
    stack.push(root);
    while (!stack.isEmpty()) {
        TreeNode node = stack.pop();
        if (node != null) {
            result.add(node.val);
            stack.push(node.right);
            stack.push(node.left);
        }
    }
    return result;
}
```
