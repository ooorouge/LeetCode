### No.15 3Sum
* 如果要搜索两个值，并且在成功后两个值同时变动，而且是中心对称变动，非中心对称的数据就扫不到，所以固定两端搜中间就不如固定一端递增，搜剩下两个值好
* 该用sort，不然很难有效的排除重复
* 注释里的一些错误，做题的时候要注意所有数据都扫描到
```java
class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
    	Arrays.sort(nums);
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        for (int i = 0; i < nums.length - 2; ++i) {
            //不能写成 i == i+1 这样nums_i能组成的对就没了
            while (i > 0 && nums[i] == nums[i-1] && i < nums.length - 2) ++i;
         	int mid = i + 1, end = nums.length - 1;
         	int remain = -nums[i];
         	while (mid < end) {
         		if ( remain == (nums[mid] + nums[end])) {
         			res.add(Arrays.asList(nums[i], nums[mid], nums[end]));
         			while (mid < end && nums[mid+1] == nums[mid]) ++mid;
         			while (mid < end && nums[end-1] == nums[end]) --end;
         			++mid;--end;
         		} else if ( remain > (nums[mid] + nums[end])) {
         			++mid;
         		} else {
         			--end;
         		}
         	}	
        }
        return res;
    }
}
```
