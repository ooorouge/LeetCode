### No.41 First Missing Positive
* 这个题最重要的还是在限定整数范围内的O(n)排序的做法，就是检查每个index是不是值也是index，否则把这个值交换到该在的位置上去，大概是
* 这样做完之后开始遍历，从1开始，因为是正整数，如果发现有哪个数字对不上他的index，那么return这个数字
* 特殊情况，数组长度为0，如果从`k=1`开始，如果数组长度为0，会在循环最开始的时候退出，那么返回1，可以和`k<n`并在一起写
* 特殊情况2，数组长度为1，意味着没办法从`index=1`开始搜，所以检查一下，k是否在0位置上，如果k在，那么missing的树是k+1，否则是k
```java
public int firstMissingPositive(int[] nums) {

	int i = 0, n = nums.length;
	while (i < n) {
		if (nums[i] >= 0 && nums[i] < n && nums[nums[i]] != nums[i])
			swap(nums, i, nums[i]);
		else
			i++;
	}
	int k = 1;
	while (k < n && nums[k] == k)
		k++;
    
	if (n == 0 || k < n)
		return k;
	else   
		return nums[0] == k ? k + 1 : k;

}

private void swap(int[] nums, int i, int j) {
	int temp = nums[i];
	nums[i] = nums[j];
	nums[j] = temp;
}
```
