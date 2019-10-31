### 索引的问题
```java
class Solution {
    public TreeNode sortedArrayToBST(int[] nums) {
        if (nums.length == 0) {
            return null;
        }
        TreeNode root = helper(nums);
        return root;
    }
    public TreeNode helper(int[] num) {
        if (num.length == 0) {
            return null;
        }
        int mid = (num.length-1) / 2;
        TreeNode root = new TreeNode(num[mid]);
        root.left = helper(Arrays.copyOfRange(num, 0, mid));
        root.right = helper(Arrays.copyOfRange(num, mid+1, num.length));
        return root;
    }  
    public TreeNode helper(int[] num, int low, int high) {
        if (low > high) {
            return null;
        }
        int mid = low + (high - low) / 2;
        TreeNode root = new TreeNode(num[mid]);
        root.right = helper(num, low, mid-1);
        root.left = helper(num, mid+1, high);
        return root;
    }
}
```
